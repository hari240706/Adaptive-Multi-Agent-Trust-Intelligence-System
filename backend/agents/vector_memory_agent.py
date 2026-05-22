import os

import faiss

import pickle

import numpy as np

from sentence_transformers import (
    SentenceTransformer
)


# =========================
# Paths
# =========================

VECTOR_DB_PATH = "vector_store/faiss_index.bin"

CLAIMS_PATH = "vector_store/claims.pkl"

# Create directory
os.makedirs(
    "vector_store",
    exist_ok=True
)

# =========================
# Load Embedding Model
# =========================

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# =========================
# Vector Dimension
# =========================

dimension = 384

# =========================
# Load Existing Index
# =========================

if os.path.exists(VECTOR_DB_PATH):

    index = faiss.read_index(
        VECTOR_DB_PATH
    )

else:

    index = faiss.IndexFlatL2(
        dimension
    )

# =========================
# Load Existing Claims
# =========================

if os.path.exists(CLAIMS_PATH):

    with open(
        CLAIMS_PATH,
        "rb"
    ) as f:

        stored_claims = pickle.load(f)

else:

    stored_claims = []


# =========================
# Save Database
# =========================

def save_vector_database():

    faiss.write_index(
        index,
        VECTOR_DB_PATH
    )

    with open(
        CLAIMS_PATH,
        "wb"
    ) as f:

        pickle.dump(
            stored_claims,
            f
        )


# =========================
# Store Claim
# =========================

def store_claim(text):

    # Prevent duplicates
    if text in stored_claims:

        return

    embedding = embedding_model.encode(
        [text]
    )

    vector = np.array(
        embedding,
        dtype=np.float32
    )

    index.add(vector)

    stored_claims.append(text)

    save_vector_database()


# =========================
# Semantic Search
# =========================

def search_similar_claims(

    text,

    top_k=5
):

    if len(stored_claims) == 0:

        return []

    embedding = embedding_model.encode(
        [text]
    )

    query_vector = np.array(
        embedding,
        dtype=np.float32
    )

    distances, indices = index.search(

        query_vector,

        top_k
    )

    results = []

    for idx in indices[0]:

        if idx < len(stored_claims):

            results.append(
                stored_claims[idx]
            )

    return results


# =========================
# Database Statistics
# =========================

def get_vector_database_stats():

    return {

        "stored_claims":
        len(stored_claims),

        "vector_dimension":
        dimension
    }