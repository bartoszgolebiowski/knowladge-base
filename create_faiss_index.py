import os
import os
import json
import numpy as np
import requests
import time
from sentence_transformers import SentenceTransformer
import faiss

# Ścieżka do folderu z dokumentami
DOCUMENTS_DIR = "knowladge/sa-prof"

# Parametry chunkowania
CHUNK_SIZE = 512  # Długość chunku w tokenach (zmniejszono dla lepszej precyzji)
OVERLAP = 64  # Overlap między chunkami (zmniejszono proporcjonalnie)

# Model embeddingów (ten sam co w projekcie)
MODEL_NAME = "all-mpnet-base-v2"
OPENROUTER_API_KEY = "your_openrouter_api_key_here"
OPENROUTER_MODEL = "x-ai/grok-3-mini"


def enrich_document_with_openrouter(doc_text):
    """Wzbogaca cały dokument metadanymi używając OpenRouter API z Grok. Zwraca dict z metadanymi."""
    if not OPENROUTER_API_KEY:
        raise ValueError(
            "Brak OPENROUTER_API_KEY. Ustaw zmienną środowiskową: export OPENROUTER_API_KEY=your_key"
        )

    prompt = f"""
    Analyze the following document and return a JSON object with the following keys:
    "chain_of_thought": detailed reasoning process,
    "summary": short summary (1-2 sentences),
    "tags": list of keywords,
    "context": thematic context (1 sentence),


    Document: {doc_text} 

    Respond only with the JSON object, no additional text.
    """
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": OPENROUTER_MODEL,
                "messages": [{"role": "user", "content": prompt}],
            },
            timeout=60,
        )

        response.raise_for_status()
        content = response.json()["choices"][0]["message"]["content"]
        enriched_dict = json.loads(content.strip())
        return enriched_dict
    except Exception as e:
        print(f"Błąd wzbogacania dokumentu via OpenRouter: {e}")
        return {
            "summary": f"{doc_text[:100]}...",
            "tags": ["unknown"],
            "context": "unknown",
        }


def load_documents():
    """Ładuje dokumenty Markdown z folderu."""
    documents = []

    for filename in os.listdir(DOCUMENTS_DIR):
        if filename.endswith(".md"):
            filepath = os.path.join(DOCUMENTS_DIR, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                # Wyciągnij tytuł z pierwszego wiersza (zakładając, że zaczyna się od #)
                lines = content.split("\n")
                title = (
                    lines[0].strip("# ").strip()
                    if lines[0].startswith("#")
                    else filename
                )
                documents.append(
                    {
                        "filename": filename,
                        "filepath": filepath,
                        "title": title,
                        "content": content,
                    }
                )
    return documents


def chunk_text(text, chunk_size=CHUNK_SIZE, overlap=OVERLAP):
    """Dzieli tekst na chunki po znakach z overlap."""
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
        if start >= len(text):
            break
    return chunks


def create_embeddings_and_index():
    """Tworzy embeddingi dla chunków i indeks FAISS."""
    print("Rozpoczynam tworzenie indeksu FAISS...")

    # Ładuj model
    print(f"Ładowanie modelu embeddingów: {MODEL_NAME}")
    model = SentenceTransformer(MODEL_NAME)
    print(".2f")
    print(f"Urządzenie: {model.device}")

    # Ładuj dokumenty
    print(f"Ładowanie dokumentów z katalogu: {DOCUMENTS_DIR}")
    documents = load_documents()
    print(f"Załadowano {len(documents)} dokumentów.")

    # Chunkuj i twórz embeddingi
    all_chunks = []
    metadata = []  # Przechowuje informacje o chunkach (filename, chunk_id)
    total_chunks = 0

    process_start = time.time()
    for doc_idx, doc in enumerate(documents):
        doc_start = time.time()
        print(
            f"Przetwarzanie dokumentu {doc_idx + 1}/{len(documents)}: {doc['filename']}"
        )

        # Wzbogac cały dokument metadanymi
        print("  Wzbogacanie dokumentu...")
        enrich_start = time.time()
        enriched_doc = enrich_document_with_openrouter(doc["content"])
        print(".2f")
        print(
            f"    Dokument wzbogacony: summary='{enriched_doc.get('summary', '')}', tags={enriched_doc.get('tags', [])}, context='{enriched_doc.get('context', '')}'"
        )

        chunks = chunk_text(doc["content"])
        print(f"  Podzielono na {len(chunks)} chunków.")

        for i, chunk in enumerate(chunks):
            print(f"    Przetwarzanie chunku {i + 1}/{len(chunks)}...")

            # Łącz oryginalny chunk z wzbogaconymi danymi dokumentu dla lepszych embeddingów
            enriched_chunk = f"{chunk} {enriched_doc.get('summary', '')} {' '.join(enriched_doc.get('tags', []))} {enriched_doc.get('context', '')}"
            print(f"      Połączony chunk: {len(enriched_chunk)} znaków.")

            all_chunks.append(enriched_chunk)
            metadata.append(
                {
                    "filename": doc["filename"],
                    "filepath": doc["filepath"],
                    "document_title": doc["title"],
                    "chunk_id": i,
                    "chunk_text": chunk,
                    "enriched_metadata": enriched_doc,  # Metadane dokumentu
                }
            )
            total_chunks += 1
            print(f"      Chunk {total_chunks} dodany do listy.")

        print(".2f")

    print(f"Łącznie {total_chunks} chunków do embeddingów.")
    print(".2f")

    # Twórz embeddingi
    print(f"Tworzenie embeddingów dla {len(all_chunks)} chunków...")
    encode_start = time.time()
    embeddings = model.encode(all_chunks, show_progress_bar=True)
    print(".2f")

    # Konwertuj na numpy array
    embeddings = np.array(embeddings).astype("float32")
    print(f"Embeddingi skonwertowane na numpy array: shape {embeddings.shape}")

    # Twórz indeks FAISS (L2 distance)
    dimension = embeddings.shape[1]
    print(f"Tworzenie indeksu FAISS z wymiarem {dimension}...")
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    print("Indeks FAISS utworzony i wypełniony.")

    # Zapisz indeks i metadane
    print("Zapisywanie indeksu FAISS...")
    faiss.write_index(index, "faiss_index.idx")
    print("Indeks FAISS zapisany.")

    print("Zapisywanie metadanych...")
    with open("chunk_metadata.json", "w", encoding="utf-8") as f:
        json.dump(metadata, f, ensure_ascii=False, indent=4)
    print("Metadane zapisane.")

    print(
        f"Proces zakończony. Indeks FAISS z {len(all_chunks)} chunkami zapisany jako 'faiss_index.idx'."
    )
    print("Metadane zapisane jako 'chunk_metadata.json'.")
    print(".2f")


if __name__ == "__main__":
    create_embeddings_and_index()
