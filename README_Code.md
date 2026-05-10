# 💻 Architectures du Système RAG - Code Fonctionnel

Ce document présente les implémentations Python pour les différentes architectures de réponse aux questions juridiques.

## 1. Baseline (LLM sans RAG)
Simule un modèle répondant uniquement avec sa mémoire interne.
```python
def llm_no_rag(query: str) -> str:
    # Réponse générique basée sur des mots-clés prédéfinis
    knowledge_base = {'سرعة': 'الحد الأقصى للسرعة...', 'طلاق': 'الطلاق في المغرب...'}
    for keyword, response in knowledge_base.items():
        if keyword in query.lower():
            return f"[Baseline] {response}"
    return "Pas d'informations suffisantes."
```

## 2. RAG Naïf (Dense Retrieval)
Utilise FAISS pour une recherche par similarité cosinus sur des embeddings multilingues.
```python
def rag_classic(query: str, k: int = 3):
    query_emb = embedding_model.encode([query]).astype('float32')
    faiss.normalize_L2(query_emb)
    scores, indices = faiss_index.search(query_emb, k)
    # ... augmentation et génération ...
```

## 3. RAG avec Re-ranking
Ajoute une couche de tri combinant score dense, score lexical (Jaccard) et bonus par type de loi.
```python
def rerank(query: str, docs: List[Dict]):
    # Calcul d'un score combiné : 0.6 * dense + 0.3 * lexical + bonus_type
    # ... tri des résultats ...
```

## 4. RAG Hybride (Dense + Sparse)
Combine la recherche sémantique (FAISS) et lexicale (BM25) via la méthode **Reciprocal Rank Fusion (RRF)**.
```python
def hybrid_retrieve(query: str, k: int = 3):
    dense_res = retrieve_dense(query, k=k*2)
    sparse_res = retrieve_sparse_bm25(query, k=k*2)
    return reciprocal_rank_fusion(dense_res, sparse_res)[:k]
```

## 5. Multi-hop RAG
Effectue deux itérations de recherche en enrichissant la requête du deuxième tour avec le contexte du premier.
```python
def multi_hop_rag(query: str, k: int = 3):
    hop1 = hybrid_retrieve(query, k=k)
    enriched_query = reformulate_query(query, hop1)
    hop2 = hybrid_retrieve(enriched_query, k=k)
    return generate_response(query, combined_results)
```

## 6. Graph RAG
Explore un graphe de connaissances (lois, articles, catégories) via un parcours en largeur (BFS) pour trouver des connexions sémantiques et explicites.
```python
def graph_rag(query: str, k: int = 3):
    seed_nodes = retrieve_dense(query, k=2)
    # Exploration BFS du graphe de relations
    visited = explore_graph(seed_nodes, max_hops=2)
    return generate_response(query, results_from_graph)
```

## 7. Agentic RAG
Un agent décisionnel qui choisit la meilleure stratégie (Hybrid, Graph, Multi-hop) selon la complexité de la question.
```python
def agentic_rag(query: str, k: int = 3):
    decision = classify_query(query) # Analyse complexité et types
    # Boucle de raisonnement avec seuil de qualité (Score > 0.4)
    # ... itérations jusqu'à satisfaction ...
```
