from agents.vector_memory_agent import (

    store_claim,

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
# Known Suspicious Claims
# =========================

known_fake_claims = [

    "aliens elected as world leaders",

    "secret underground lizard society controls governments",

    "moon made of cheese",

    "earth is flat and controlled by hidden elites"
]


# Store suspicious claims
for claim in known_fake_claims:

    store_claim(claim)


# =========================
# Semantic Recall Agent
# =========================

def semantic_recall(text):

    # Store incoming claim
    store_claim(text)

    # Search similar claims
    similar_claims = search_similar_claims(
        text
    )

    if len(similar_claims) == 0:

        return {

            "agent":
            "Semantic Memory Agent",

            "matched_claim":
            None,

            "similarity":
            0,

            "semantic_analysis":
            "No semantic memory match",

            "score":
            0.5
        }

    # Compute similarity
    input_embedding = embedding_model.encode(
        text,

        convert_to_tensor=True
    )

    best_match = None

    best_similarity = 0

    for claim in similar_claims:

        claim_embedding = embedding_model.encode(

            claim,

            convert_to_tensor=True
        )

        similarity = util.cos_sim(

            input_embedding,

            claim_embedding
        ).item()

        if similarity > best_similarity:

            best_similarity = similarity

            best_match = claim

    # Decision logic
    if best_similarity > 0.75:

        return {

            "agent":
            "Semantic Memory Agent",

            "matched_claim":
            best_match,

            "similarity":
            round(best_similarity, 2),

            "semantic_analysis":
            "Strong suspicious semantic similarity detected",

            "score":
            0.15
        }

    elif best_similarity > 0.55:

        return {

            "agent":
            "Semantic Memory Agent",

            "matched_claim":
            best_match,

            "similarity":
            round(best_similarity, 2),

            "semantic_analysis":
            "Moderate semantic similarity detected",

            "score":
            0.4
        }

    else:

        return {

            "agent":
            "Semantic Memory Agent",

            "matched_claim":
            best_match,

            "similarity":
            round(best_similarity, 2),

            "semantic_analysis":
            "Weak semantic similarity detected",

            "score":
            0.75
        }