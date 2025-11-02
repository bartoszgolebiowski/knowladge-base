import json
import networkx as nx
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict
from itertools import combinations
import re
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
import numpy as np
from rank_bm25 import BM25Okapi

# Stałe ścieżki
DOCS_DIR = Path("knowladge/sa-prof")
NER_RESULTS_JSON = "ner_results.json"
WEIGHTED_GRAPH_JSON = "weighted_hybrid_graph.json"

# Wybór metody wagowania: "TFIDF" lub "BM25"
METHOD = "BM25"


def load_ner_data():
    """Ładuje dane NER z JSON."""
    try:
        with open(NER_RESULTS_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Błąd: Brak ner_results.json")
        return {}


def load_documents():
    """Ładuje zawartość dokumentów do słownika."""
    corpus = {}
    for doc_path in DOCS_DIR.glob("*.md"):
        try:
            with open(doc_path, "r", encoding="utf-8") as f:
                corpus[doc_path.name] = f.read().lower()
        except Exception as e:
            print(f"Błąd czytania {doc_path.name}: {e}")
    return corpus


def build_cooccurrence_graph(ner_data):
    """Buduje graf współwystępowania encji."""
    entity_docs = {doc: set(entities) for doc, entities in ner_data.items()}
    co_occurrence = defaultdict(int)
    entity_pairs = defaultdict(set)

    counter = 0
    for doc, entities in entity_docs.items():
        for pair in combinations(sorted(entities), 2):
            counter += 1
            co_occurrence[pair] += 1
            entity_pairs[pair].add(doc)

    print(f"Liczba przetworzonych par encji: {counter}")

    # Filtr: min. 2 dokumenty
    filtered_co_occurrence = {
        pair: count for pair, count in co_occurrence.items() if count >= 2
    }

    G = nx.Graph()
    for (ent1, ent2), weight in filtered_co_occurrence.items():
        G.add_edge(ent1, ent2, weight=weight, docs=list(entity_pairs[(ent1, ent2)]))

    return G


def build_hybrid_graph(cooc_graph, ner_data):
    """Buduje hybrydowy graf: encje + dokumenty."""
    G = cooc_graph.copy()  # Kopia grafu encji

    # Dodaj węzły dokumentów
    for doc in ner_data.keys():
        if ner_data[doc]:  # Tylko z encjami
            G.add_node(doc, type="document")

    # Dodaj krawędzie encja-dokument
    for doc, entities in ner_data.items():
        for entity in entities:
            if entity in G.nodes():
                G.add_edge(entity, doc, weight=1, type="entity-document")

    # Statystyki
    entity_nodes = [n for n, d in G.nodes(data=True) if d.get("type") != "document"]
    document_nodes = [n for n, d in G.nodes(data=True) if d.get("type") == "document"]
    print(f"Węzły encji: {len(entity_nodes)}, dokumentów: {len(document_nodes)}")

    return G


def add_weights_to_graph(hybrid_graph, ner_data, corpus):
    """Dodaje wagi do grafu."""
    G = hybrid_graph.copy()

    # Wybór metody wagowania
    if METHOD == "TFIDF":
        scores = compute_tfidf_weights(ner_data, corpus)
    elif METHOD == "BM25":
        scores = compute_bm25_weights(ner_data, corpus)
    else:
        raise ValueError(f"Nieznana metoda: {METHOD}. Wybierz 'TFIDF' lub 'BM25'.")

    # Pozycjonowanie
    position_weights = {}
    for doc, content in corpus.items():
        lines = content.split("\n")
        title = lines[0] if lines else ""
        intro = " ".join(lines[:5])
        position_weights[doc] = {}
        for entity in ner_data.get(doc, []):
            weight = 1.0
            if entity.lower() in title.lower():
                weight *= 5.0
            if entity.lower() in intro.lower():
                weight *= 1.5
            position_weights[doc][entity] = weight

    # Aktualizuj wagi krawędzi
    for u, v, d in list(G.edges(data=True)):
        if d.get("type") == "entity-document":
            entity, doc = (u, v) if G.nodes[u].get("type") != "document" else (v, u)
            content = corpus.get(doc, "")
            occurrence_count = len(
                re.findall(re.escape(entity), content, re.IGNORECASE)
            )
            base_weight = occurrence_count if occurrence_count > 0 else 1
            method_weight = scores.get(doc, {}).get(entity, 0.0)
            pos_weight = position_weights.get(doc, {}).get(entity, 1.0)
            new_weight = base_weight * (1 + method_weight) * pos_weight
            d["weight"] = round(new_weight, 2)
            d[METHOD.lower()] = round(method_weight, 2)
            d["position_weight"] = pos_weight
            d["occurrences"] = occurrence_count

    # Statystyki
    entity_document_edges = [
        e for e in G.edges(data=True) if e[2].get("type") == "entity-document"
    ]
    weights = [d["weight"] for u, v, d in entity_document_edges]
    print(f"Średnia waga: {sum(weights)/len(weights):.2f}, Max: {max(weights):.2f}")

    # Zapis JSON
    weighted_data = {
        "nodes": [
            {"id": n, "type": d.get("type", "entity")} for n, d in G.nodes(data=True)
        ],
        "edges": [
            {
                "source": u,
                "target": v,
                "weight": d["weight"],
                "type": d.get("type"),
                METHOD.lower(): d.get(METHOD.lower(), 0),
                "position_weight": d.get("position_weight", 1),
                "occurrences": d.get("occurrences", 0),
                "docs": d.get("docs", []),
            }
            for u, v, d in G.edges(data=True)
        ],
    }
    with open(WEIGHTED_GRAPH_JSON, "w", encoding="utf-8") as f:
        json.dump(weighted_data, f, indent=4)

    print(f"Ważony graf zapisany: {WEIGHTED_GRAPH_JSON}")
    return G


def merge_similar_entities(ner_data):
    """Łączy podobne encje za pomocą embeddingów i podobieństwa cosinusowego."""
    # Zbierz wszystkie unikalne encje
    all_entities = set()
    for entities in ner_data.values():
        all_entities.update(entities)
    all_entities = list(all_entities)

    if len(all_entities) < 2:
        return ner_data  # Brak potrzeby łączenia

    # Oblicz embeddingi
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(all_entities)

    # Oblicz podobieństwo cosinusowe
    from sklearn.metrics.pairwise import cosine_similarity

    similarity_matrix = cosine_similarity(embeddings)

    # Grupuj encje z podobieństwem > 0.8
    entity_to_representative = {ent: ent for ent in all_entities}
    visited = set()

    for i, ent1 in enumerate(all_entities):
        if ent1 in visited:
            continue
        group = [ent1]
        for j, ent2 in enumerate(all_entities):
            if i != j and similarity_matrix[i][j] > 0.8:
                group.append(ent2)
                visited.add(ent2)
        if len(group) > 1:
            # Wybierz reprezentatywną: najkrótszą
            representative = min(group, key=len)
            for ent in group:
                entity_to_representative[ent] = representative
            print(f"Połączono grupę: {group} -> {representative}")

    # Zaktualizuj ner_data
    merged_ner_data = {}
    for doc, entities in ner_data.items():
        merged_entities = [entity_to_representative.get(ent, ent) for ent in entities]
        # Usuń duplikaty po łączeniu
        merged_ner_data[doc] = list(set(merged_entities))

    unique_representatives = set(entity_to_representative.values())
    print(f"Połączono {len(all_entities)} encji w {len(unique_representatives)} grup.")
    return merged_ner_data


def compute_tfidf_weights(ner_data, corpus):
    """Oblicza wagi TF-IDF dla encji w dokumentach."""
    # Zbierz wszystkie unikalne encje jako vocabulary
    all_entities = set()
    for entities in ner_data.values():
        all_entities.update(entities)
    vocabulary = {
        entity.lower(): idx for idx, entity in enumerate(sorted(all_entities))
    }

    vectorizer = TfidfVectorizer(
        stop_words="english", vocabulary=vocabulary, max_features=None
    )
    tfidf_matrix = vectorizer.fit_transform(corpus.values())
    feature_names = vectorizer.get_feature_names_out()
    doc_names = list(corpus.keys())

    scores = {}
    for i, doc in enumerate(doc_names):
        scores[doc] = {}
        for entity in ner_data.get(doc, []):
            entity_lower = entity.lower()
            if entity_lower in feature_names:
                idx = list(feature_names).index(entity_lower)
                scores[doc][entity] = tfidf_matrix[i, idx]
            else:
                scores[doc][entity] = 0.0

    return scores


def compute_bm25_weights(ner_data, corpus):
    """Oblicza wagi BM25 dla encji w dokumentach."""
    # Tokenizuj dokumenty
    tokenized_corpus = [doc.lower().split() for doc in corpus.values()]
    bm25 = BM25Okapi(tokenized_corpus)
    doc_names = list(corpus.keys())

    bm25_scores = {}
    for doc_idx, doc in enumerate(doc_names):
        bm25_scores[doc] = {}
        for entity in ner_data.get(doc, []):
            # Traktuj encję jako zapytanie (tokenizuj)
            query_tokens = entity.lower().split()
            # Oblicz score BM25 dla tego dokumentu
            scores = bm25.get_scores(query_tokens)
            bm25_scores[doc][entity] = scores[doc_idx]

    return bm25_scores


def main():
    """Główny pipeline."""
    ner_data = load_ner_data()
    if not ner_data:
        return

    # Łączenie podobnych encji
    ner_data = merge_similar_entities(ner_data)

    corpus = load_documents()

    # Krok 1: Współwystępowanie
    cooc_graph = build_cooccurrence_graph(ner_data)

    # Krok 2: Hybrydowy graf
    hybrid_graph = build_hybrid_graph(cooc_graph, ner_data)

    # Krok 3: Wagi
    weighted_graph = add_weights_to_graph(hybrid_graph, ner_data, corpus)

    print("Pipeline zakończony!")


if __name__ == "__main__":
    main()
