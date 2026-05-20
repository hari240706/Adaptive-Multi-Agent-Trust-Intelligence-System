# AMATIS

# Adaptive Multi-Agent Trust Intelligence System

AMATIS is an AI-powered misinformation detection and trust intelligence platform designed to detect, analyze, explain, and track fake or misleading information using modern NLP, transformer architectures, multi-agent intelligence systems, and scalable AI infrastructure.

---

# 🚀 Project Vision

AMATIS aims to evolve into a next-generation trust intelligence ecosystem capable of:

- Detecting fake or misleading information
- Understanding contextual semantics using transformers
- Analyzing source credibility
- Verifying suspicious claims
- Tracking misinformation propagation
- Explaining AI decisions transparently
- Supporting cooperative multi-agent reasoning
- Scaling like real-world distributed AI systems

This project is being engineered with a production-oriented and MAANG-level system design mindset.

---

# 🎯 Current Development Status

# ✅ Phase 1 — Data Engineering Pipeline (Completed)

## Completed Tasks

- Project environment setup
- Repository structure creation
- Multi-source dataset collection
- Data cleaning and preprocessing
- Schema standardization
- Label normalization
- Dataset merging and deduplication
- Final unified dataset generation

---

# ✅ Phase 2 — Baseline NLP System (Completed)

## Completed Tasks

- TF-IDF vectorization
- Logistic Regression classifier
- Train/test pipeline
- Model evaluation
- Confusion matrix analysis
- Model persistence using joblib
- Real-time prediction pipeline

---

# ✅ Phase 3 — Full-Stack AI Integration (Completed)

## Completed Tasks

- FastAPI backend development
- REST API creation
- Frontend UI integration
- Frontend ↔ Backend communication
- Real-time inference pipeline
- CORS middleware configuration
- End-to-end AI workflow deployment locally

---

# ✅ Phase 4 — Transformer-Based NLP System (Completed)

## Completed Tasks

- DistilBERT fine-tuning
- Transformer tokenization pipeline
- Hugging Face integration
- GPU-based training using Google Colab
- Transformer evaluation pipeline
- DistilBERT inference integration
- Transformer-based FastAPI backend upgrade

---

# ✅ Phase 5 — Multi-Agent Intelligence Architecture (In Progress)

## Completed Tasks

- Modular agent architecture
- NLP Agent implementation
- Credibility Agent implementation
- Fact Check Agent implementation
- Multi-agent orchestrator
- Agent-based trust scoring
- Cooperative AI reasoning workflow
- Multi-agent frontend visualization
- AI trust dashboard integration

---

# 📂 Datasets Used

## 1. FakeNewsNet

Used:

- BuzzFeed fake news dataset
- BuzzFeed real news dataset
- PolitiFact fake news dataset
- PolitiFact real news dataset

---

## 2. LIAR Dataset

Used:

- train.tsv
- test.tsv
- valid.tsv

---

## 3. Dataset 3

Used:

- train.csv
- test.csv
- evaluation.csv

---

# 🧠 Current Multi-Agent Architecture

```text
User Input
    ↓
Frontend Trust Dashboard
    ↓
FastAPI Backend
    ↓
Orchestrator Agent
    ↓
 ┌─────────────────────┬─────────────────────┬─────────────────────┐
 │                     │                     │
 ↓                     ↓                     ↓
NLP Agent      Credibility Agent     Fact Check Agent
 │                     │                     │
 └─────────────────────┴─────────────────────┘
                ↓
        Trust Intelligence
                ↓
      Final Prediction + Trust Score
```

---

# 🧹 Data Cleaning Operations

The preprocessing pipeline performs:

- Null value removal
- Duplicate removal
- URL cleaning
- Lowercase normalization
- Special character removal
- Whitespace normalization
- Label standardization
- Dataset shuffling

---

# 📊 Current Model Performance

## Baseline Logistic Regression Model

| Metric | Score |
|--------|------|
| Accuracy | 87.2% |
| F1-Score | 87% |

---

## DistilBERT Transformer Model

| Metric | Score |
|--------|------|
| Accuracy | 89.6% |
| F1-Score | 89.7% |

---

# 🧠 Current AI Capabilities

AMATIS currently supports:

- Transformer-based misinformation detection
- Semantic text understanding
- Multi-agent trust reasoning
- Source credibility analysis
- Rule-based fact verification
- Cooperative agent orchestration
- Confidence scoring
- Trust score generation
- Real-time API inference
- Frontend AI interaction
- Explainable multi-agent outputs

---

# 📁 Current Project Structure

```text
Adaptive-Multi-Agent-Trust-Intelligence-System/
│
├── agents/
│   ├── nlp_agent.py
│   ├── credibility_agent.py
│   ├── fact_check_agent.py
│   └── orchestrator.py
│
├── backend/
│   └── main.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── data/
│   ├── raw/
│   └── processed/
│       ├── fakenewsnet_cleaned.csv
│       ├── liar_cleaned.csv
│       └── final_cleaned_dataset.csv
│
├── models/
│   ├── logistic_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_baseline_model.ipynb
│   └── 03_distilbert_training.ipynb
│
├── scripts/
│
├── requirements.txt
├── .gitignore
├── README.md
└── venv/
```

---

# ⚙️ Technologies Used

## Programming Language

- Python

---

## Machine Learning & NLP

- scikit-learn
- transformers
- torch
- Hugging Face
- pandas
- numpy

---

## Backend

- FastAPI
- Uvicorn
- Pydantic

---

## Frontend

- HTML
- CSS
- JavaScript

---

## Development Tools

- Git
- GitHub
- Jupyter Notebook
- Google Colab
- VS Code

---

# 🔥 Current Multi-Agent Components

## NLP Agent

Responsibilities:

- Semantic misinformation classification
- Transformer inference
- Confidence estimation

---

## Credibility Agent

Responsibilities:

- Source trust analysis
- Trusted-domain identification
- Credibility scoring

---

## Fact Check Agent

Responsibilities:

- Suspicious pattern detection
- Rule-based verification
- Claim anomaly analysis

---

## Orchestrator Agent

Responsibilities:

- Agent coordination
- Multi-agent reasoning
- Trust score generation
- Final decision synthesis

---

# 🚀 Upcoming Development Phases

## Future Planned Agents

- Knowledge Graph Agent
- Propagation Analysis Agent
- Web Verification Agent
- Memory Agent
- Adaptive Meta-Agent

---

## Future Planned Features

- Explainable AI (XAI)
- Live web evidence retrieval
- Graph-based misinformation tracking
- Real-time streaming pipeline
- Cloud-native deployment
- Docker containerization
- Kubernetes orchestration
- Distributed AI infrastructure
- Adaptive multi-agent learning

---

# 🧠 Long-Term System Vision

The final system aims to evolve into a:

- Real-time misinformation intelligence platform
- Distributed AI ecosystem
- Multi-agent adaptive trust analysis system
- Scalable cloud-native AI infrastructure
- Intelligent trust reasoning engine

---

# 🎯 Core Objectives

- Build an explainable misinformation detection system
- Create a scalable AI architecture
- Combine NLP, graph intelligence, and behavioral analysis
- Engineer a production-grade AI pipeline
- Develop a MAANG-level system engineering portfolio project
- Research advanced trust intelligence architectures

---

# 📌 Current Milestone

✅ Multi-Agent Trust Intelligence Architecture successfully integrated.

## Current Capabilities

- End-to-end full-stack AI workflow
- Transformer inference API
- Multi-agent orchestration
- AI trust dashboard
- Trust score generation
- Cooperative AI reasoning pipeline
- Explainable agent outputs

---

# 🚀 Next Milestone

- Knowledge graph integration
- Live web verification agents
- Advanced reasoning systems
- Evidence retrieval pipeline
- Adaptive orchestrator intelligence

---

# 📄 License

This project is currently under active development.

---

# 👨‍💻 Author

HARIPRASAD R