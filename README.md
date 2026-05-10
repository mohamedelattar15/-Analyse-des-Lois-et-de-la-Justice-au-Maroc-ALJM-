# ⚖️ Analyse des Lois et de la Justice au Maroc (ALJM)

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![NLP](https://img.shields.io/badge/NLP-Natural%20Language%20Processing-green.svg)](https://en.wikipedia.org/wiki/Natural_language_processing)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Ce projet vise à appliquer les techniques avancées du **Traitement du Langage Naturel (NLP)** pour analyser, classifier et explorer le corpus législatif marocain, principalement extrait du **Bulletin Officiel (BO)**.

---

## 📌 Présentation du Projet

L'accès à l'information juridique est un pilier de l'État de droit. Au Maroc, le Bulletin Officiel constitue la source primaire de la législation. Ce projet propose une plateforme intelligente capable de transformer ces documents (souvent au format PDF) en données structurées et exploitables pour :
- **Identifier les tendances** législatives par période.
- **Classifier automatiquement** les lois par secteur (Civil, Pénal, Administratif, etc.).
- **Extraire des entités nommées** (Dates, Articles, Autorités citées).
- **Faciliter la recherche sémantique** dans le corpus juridique.

## 🏗️ Architectures du Système

Le projet repose sur une synergie de quatre architectures majeures pour traiter la complexité du domaine juridique marocain.

### 1. Architecture de Traitement de Données (Pipeline ETL)
- **Collecte** : Scraping asynchrone des Bulletins Officiels (SGG).
- **Extraction** : Pipeline OCR hybride (Tesseract pour le texte clair, PaddleOCR pour les documents complexes/scannés).
- **Nettoyage** : Normalisation du texte arabe (retrait des diacritiques, normalisation des alefs) et français juridique.

### 2. Architecture de Compréhension (ML/Deep Learning)
- **Modèle de Langue** : Utilisation de **CamemBERT** (Français) et **AraBERT** (Arabe) fine-tunés sur des corpus légaux.
- **Classification Sectorielle** : Réseau de neurones pour catégoriser les lois (ex: Droit des Affaires vs Droit Civil).
- **NER (Named Entity Recognition)** : Modèle Bi-LSTM-CRF ou Transformer pour l'extraction des numéros d'articles et des dates de décret.

### 3. Architecture RAG Avancée (Retrieval-Augmented Generation)
- **Naive RAG** : Indexation vectorielle simple (ChromaDB) pour les recherches rapides.
- **Graph RAG** : Modélisation des relations inter-textuelles (abrogations, amendements) via un graphe de connaissances.
- **Agentic RAG** : Orchestration via un agent autonome capable de raisonner sur plusieurs documents pour répondre à une question juridique complexe.

### 4. Architecture de Visualisation
- **Dashboard** : Interface Streamlit permettant une exploration interactive des statistiques de la justice marocaine et un chat intelligent.

---

## 🛠️ Stack Technologique

| Catégorie | Outils |
| :--- | :--- |
| **Langage** | Python 3.9+ |
| **NLP** | Hugging Face (Transformers), Spacy, NLTK, CamelTools |
| **Data & OCR** | Pandas, BeautifulSoup, PyMuPDF, Tesseract |
| **ML/DL** | Scikit-learn, PyTorch |
| **Visualisation** | Streamlit / Plotly |

## 📂 Structure du Projet

```bash
├── docs/               # Documentation détaillée et Architecture
├── data/               # Corpus de textes (Bulletins Officiels)
├── notebooks/          # Exploratory Data Analysis (EDA)
├── src/
│   ├── scraper/        # Scripts de collecte des données
│   ├── processing/     # Pipeline de nettoyage et OCR
│   ├── rag/            # Moteur RAG (Indexing, Retrieval, Generation)
│   ├── models/         # Entraînement et inférence NLP
│   └── utils/          # Fonctions utilitaires
├── app/                # Interface utilisateur (Streamlit)
├── README.md           # Documentation principale
└── requirements.txt    # Dépendances du projet
```

## ⚙️ Installation

1. **Cloner le repository** :
   ```bash
   git clone https://github.com/votre-user/analyse-lois-maroc.git
   cd analyse-lois-maroc
   ```

2. **Créer un environnement virtuel** :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows: venv\Scripts\activate
   ```

3. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

## 📊 Méthodologie

Le projet suit une approche rigoureuse en 4 étapes :
1. **Acquisition** : Extraction des métadonnées et des PDF depuis `sgg.gov.ma`.
2. **Prétraitement** : Nettoyage du texte, suppression des bruits d'OCR, et tokenisation adaptée au domaine juridique.
3. **Modélisation** : Fine-tuning de modèles pré-entraînés pour la tâche de classification sectorielle.
4. **Analyse** : Application de l'analyse thématique (LDA) pour découvrir les sujets émergents.

## ⚖️ Mentions Légales
Ce projet est réalisé dans un but académique/recherche. L'utilisation des données doit respecter les conditions d'utilisation du Secrétariat Général du Gouvernement (SGG) et la loi n° 31.13 relative au droit d'accès à l'information au Maroc.

---
*Développé dans le cadre du Devoir 3 - NLP.*
