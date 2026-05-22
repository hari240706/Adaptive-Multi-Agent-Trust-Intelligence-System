from agents.vector_memory_agent import (

    search_similar_claims
)

from sentence_transformers import (

    SentenceTransformer,

    util
)


# =========================
# Load Embedding Model
# =========================

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# =========================
# RAG Retrieval Agent
# =========================

def retrieve_rag_context(text):

    # Retrieve similar contexts
    retrieved_claims = search_similar_claims(

        text,

        top_k=5
    )

    # No retrieval case
    if len(retrieved_claims) == 0:

        return {

            "agent":
            "RAG Agent",

            "retrieved_context":
            [],

            "rag_analysis":
            "No contextual knowledge retrieved",

            "score":
            0.5
        }

    # Input embedding
    input_embedding = embedding_model.encode(

        text,

        convert_to_tensor=True
    )

    best_similarity = 0

    best_context = None

    # Find strongest context
    for context in retrieved_claims:

        context_embedding = embedding_model.encode(

            context,

            convert_to_tensor=True
        )

        similarity = util.cos_sim(

            input_embedding,

            context_embedding
        ).item()

        if similarity > best_similarity:

            best_similarity = similarity

            best_context = context

    # =========================
    # Decision Logic
    # =========================

    if best_similarity > 0.80:

        return {

            "agent":
            "RAG Agent",

            "retrieved_context":
            retrieved_claims,

            "best_context":
            best_context,

            "context_similarity":
            round(best_similarity, 2),

            "rag_analysis":
            "Highly relevant contextual knowledge retrieved",

            "score":
            0.2
        }

    elif best_similarity > 0.60:

        return {

            "agent":
            "RAG Agent",

            "retrieved_context":
            retrieved_claims,

            "best_context":
            best_context,

            "context_similarity":
            round(best_similarity, 2),

            "rag_analysis":
            "Moderately relevant contextual knowledge retrieved",

            "score":
            0.5
        }

    else:

        return {

            "agent":
            "RAG Agent",

            "retrieved_context":
            retrieved_claims,

            "best_context":
            best_context,

            "context_similarity":
            round(best_similarity, 2),

            "rag_analysis":
            "Weak contextual similarity detected",

            "score":
            0.8
        }