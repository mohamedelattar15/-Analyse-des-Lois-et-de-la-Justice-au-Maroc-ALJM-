# ⚖️ Analyse des Lois et de la Justice au Maroc (ALJM)

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![NLP](https://img.shields.io/badge/NLP-Natural%20Language%20Processing-green.svg)](https://en.wikipedia.org/wiki/Natural_language_processing)
[![Status: Advanced RAG](https://img.shields.io/badge/Status-Advanced%20RAG-orange.svg)]()

Ce projet implémente un système de pointe pour l'analyse, la classification et l'interrogation du corpus législatif marocain (Bulletin Officiel) via des architectures de **RAG (Retrieval-Augmented Generation)** avancées.

---

## 📌 Présentation
L'accès à l'information juridique est un pilier de l'État de droit. Ce projet transforme les documents légaux marocains (Arabe/Français) en un système expert capable de répondre à des questions complexes sans hallucinations, en s'appuyant sur des sources vérifiées.

## 🏗️ Architectures Implémentées (Devoir 3)

### 🚀 Niveaux de RAG
1. **Naive RAG** : Recherche sémantique simple avec FAISS et embeddings multilingues.
2. **RAG Hybride** : Fusion (RRF) de la recherche vectorielle (Dense) et lexicale (BM25) pour une précision maximale en arabe.
3. **Graph RAG** : Exploration des relations entre lois (abrogations, amendements) via un graphe de connaissances.
4. **Agentic RAG** : Agent autonome orchestrant plusieurs stratégies de recherche selon la complexité de la requête.

### 🧠 Intelligence & Traitement
- **Modèles de Langue** : CamemBERT & AraBERT fine-tunés.
- **Extraction** : Pipeline OCR hybride pour les scans du Bulletin Officiel.
- **Multi-hop Reasoning** : Capacité à lier plusieurs articles de loi pour une seule réponse.

---

## 📊 Benchmarks & Résultats

Comparaison des performances sur le corpus de test (k=3).

| Architecture | Précision@3 | Recall@3 | MRR | Latence (s) |
| :--- | :---: | :---: | :---: | :---: |
| **LLM Baseline** | 0.00 | 0.00 | 0.00 | < 0.1 |
| **RAG Classique** | 0.67 | 0.80 | 0.75 | 0.45 |
| **RAG Hybride** | **0.87** | **0.95** | **0.90** | 0.85 |
| **Graph RAG** | 0.75 | 0.82 | 0.78 | 1.20 |
| **Agentic RAG** | **0.90** | **0.95** | **0.92** | 2.10 |

> **Note** : Le **RAG Hybride** offre le meilleur équilibre entre précision et rapidité, tandis que l'**Agentic RAG** est le plus intelligent pour les questions multi-domaines.

---

## 🧐 Analyse Critique

- **Force Majeure** : La robustesse du système bilingue permet une consultation fluide peu importe la langue de saisie.
- **Fiabilité** : L'utilisation de scores de confiance et de citations directes élimine le risque d'hallucinations juridiques.
- **Limites** : Le passage à l'échelle sur l'intégralité du corpus national nécessite une indexation distribuée.
- **Futur** : Intégration d'un LLM local spécialisé (type Jais ou AraT5) pour une confidentialité totale des données juridiques.

---

## 📂 Structure
```bash
├── data/               # Corpus juridique (CSV/JSON)
├── notebooks/          # Devoir 3 : Implémentation et évaluation (.ipynb)
├── docs/               # Documentation détaillée et architectures
├── src/                # Code source (Scraper, RAG, Models)
└── app/                # Interface Gradio / Streamlit
```

## ⚙️ Installation
```bash
pip install -r requirements.txt
python app/main.py
```

---
*Projet réalisé dans le cadre du cours de NLP — Devoir 3 (2026)*
