import json
import faiss
import numpy as np
import os
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Tuple


# Model dla zapytania
class SearchQuery(BaseModel):
    query: str
    k: int = 10
    alpha: float = 0.7  # Waga dla BM25
    beta: float = 0.3  # Waga dla semantic


class HybridSearch:
    def __init__(self):
        self.bm25 = None
        self.semantic_model = None
        self.faiss_index = None
        self.documents = {}
        self.metadata = []
        self.doc_to_idx = {}

    def load_indexes(self):
        """Ładuje indeks FAISS i metadane chunków oraz buduje BM25 na pełnych dokumentach."""
        self.semantic_model = SentenceTransformer("all-mpnet-base-v2")
        # Ładuj indeks FAISS (dla chunków)
        self.faiss_index = faiss.read_index("faiss_index.idx")

        # Ładuj metadane chunków
        with open("chunk_metadata.json", "r", encoding="utf-8") as f:
            self.metadata = json.load(f)

        # Grupuj chunki po dokumentach dla pełnych tekstów
        self.documents = {}
        for meta in self.metadata:
            filepath = meta["filepath"]
            if filepath not in self.documents:
                # Ładuj pełny tekst dokumentu
                with open(filepath, "r", encoding="utf-8") as f:
                    full_text = f.read()
                self.documents[filepath] = {
                    "title": meta["filename"],
                    "full_text": full_text,
                    "chunks": [],
                }
            self.documents[filepath]["chunks"].append(meta)

        # Build BM25 na pełnych dokumentach
        doc_texts = [doc["full_text"] for doc in self.documents.values()]
        tokenized_corpus = [text.lower().split() for text in doc_texts]
        self.bm25 = BM25Okapi(tokenized_corpus)

        # Mapowanie filepath -> doc_idx dla BM25
        self.doc_to_idx = {fp: idx for idx, fp in enumerate(self.documents.keys())}

    def search_bm25(self, query: str, k: int = 10) -> List[Tuple[str, float]]:
        """BM25 wyszukiwanie na pełnych dokumentach. Zwraca: [(filepath, score), ...]"""
        query_tokens = query.lower().split()
        scores = self.bm25.get_scores(query_tokens)

        # Mapuj na filepath
        results = [(fp, float(scores[idx])) for fp, idx in self.doc_to_idx.items()]

        # Sort i top-k
        results.sort(key=lambda x: x[1], reverse=True)
        return results[:k]

    def search_semantic(self, query: str, k: int = 10) -> List[Tuple[str, float]]:
        """Semantic search na chunkach, agregowane na dokumenty. Zwraca: [(filepath, max_similarity), ...]"""
        query_embedding = self.semantic_model.encode(
            [query], convert_to_numpy=True, normalize_embeddings=True
        )

        distances, indices = self.faiss_index.search(
            query_embedding, k * 2
        )  # Więcej, bo agregujemy

        # Agreguj po dokumentach (maksymalna similarity per document)
        doc_scores = {}
        for idx, dist in zip(indices[0], distances[0]):
            meta = self.metadata[idx]
            filepath = meta["filepath"]
            if filepath not in doc_scores:
                doc_scores[filepath] = float(dist)
            else:
                doc_scores[filepath] = max(doc_scores[filepath], float(dist))

        # Sort
        results = sorted(doc_scores.items(), key=lambda x: x[1], reverse=True)
        return results[:k]

    def hybrid_search(
        self, query: str, k: int = 10, alpha: float = 0.4, beta: float = 0.6
    ) -> List[Dict]:
        """Hybrydowe wyszukiwanie na poziomie dokumentów."""
        # Wyniki z obu metod
        bm25_results = self.search_bm25(query, k=20)
        semantic_results = self.search_semantic(query, k=20)

        print(f"BM25 results: {bm25_results[:5]}")
        print(f"Semantic results: {semantic_results[:5]}")

        # Normalize scores
        bm25_scores = dict(bm25_results)
        semantic_scores = dict(semantic_results)

        bm25_norm = self._normalize_scores(bm25_scores)
        semantic_norm = self._normalize_scores(semantic_scores)

        # Combine
        combined_scores = {}
        all_docs = set(bm25_scores.keys()) | set(semantic_scores.keys())

        for filepath in all_docs:
            bm25_score = bm25_norm.get(filepath, 0)
            semantic_score = semantic_norm.get(filepath, 0)
            combined = alpha * bm25_score + beta * semantic_score
            combined_scores[filepath] = combined

        # Sort
        sorted_results = sorted(
            combined_scores.items(), key=lambda x: x[1], reverse=True
        )[:k]

        # Return with metadata
        results = []
        for filepath, score in sorted_results:
            doc = self.documents[filepath]
            results.append(
                {
                    "filename": os.path.basename(filepath),
                    "document_title": doc["title"],
                    "score": float(score),
                    "bm25_score": float(bm25_norm.get(filepath, 0)),
                    "semantic_score": float(semantic_norm.get(filepath, 0)),
                }
            )

        return results

    def _normalize_scores(self, scores_dict: Dict[int, float]) -> Dict[int, float]:
        """Min-max normalization."""
        scores = list(scores_dict.values())
        if not scores:
            return {}

        min_score = min(scores)
        max_score = max(scores)

        if max_score == min_score:
            return {idx: 1.0 for idx in scores_dict.keys()}

        return {
            idx: (score - min_score) / (max_score - min_score)
            for idx, score in scores_dict.items()
        }


# Inicjalizacja
search = HybridSearch()
search.load_indexes()

# FastAPI app
app = FastAPI(
    title="Hybrid Search API",
    description="Hybrydowe wyszukiwanie BM25 + Semantic na chunkach dokumentów",
)

# Wyłącz CORS (pozwól na wszystkie origins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Zezwól na wszystkie origins
    allow_credentials=True,
    allow_methods=["*"],  # Zezwól na wszystkie metody (GET, POST, OPTIONS itp.)
    allow_headers=["*"],  # Zezwól na wszystkie headers
)


@app.post("/search", response_model=List[Dict])
async def search_endpoint(request: SearchQuery):
    """Endpoint do hybrydowego wyszukiwania."""
    results = search.hybrid_search(
        query=request.query, k=request.k, alpha=request.alpha, beta=request.beta
    )
    return results


@app.get("/")
async def root():
    return {"message": "Hybrid Search API is running. Use POST /search with query."}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
