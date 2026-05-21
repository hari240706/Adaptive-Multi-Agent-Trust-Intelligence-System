from sentence_transformers import SentenceTransformer

from sklearn.metrics.pairwise import cosine_similarity

import numpy as np


# Load embedding model
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# Semantic memory database
memory_claims = [

    "aliens elected as world leaders",

    "miracle cure removes all diseases",

    "secret underground lizard society controls elections",

    "nasa launched a climate satellite",

    "government announced infrastructure reforms"
]


# Generate embeddings
memory_embeddings = model.encode(
    memory_claims
)


def semantic_recall(text):

    query_embedding = model.encode(
        [text]
    )

    similarities = cosine_similarity(

        query_embedding,

        memory_embeddings
    )[0]

    best_match_index = np.argmax(
        similarities
    )

    best_score = similarities[
        best_match_index
    ]

    matched_claim = memory_claims[
        best_match_index
    ]

    # Semantic interpretation
    if best_score > 0.60:

        if "alien" in matched_claim \
           or "miracle" in matched_claim \
           or "lizard" in matched_claim:

            return {

                "agent": "Semantic Memory Agent",

                "matched_claim": matched_claim,

                "similarity": round(
                    float(best_score),
                    2
                ),

                "semantic_analysis":
                    "Matched Suspicious Semantic Pattern",

                "score": 0.2
            }

        else:

            return {

                "agent": "Semantic Memory Agent",

                "matched_claim": matched_claim,

                "similarity": round(
                    float(best_score),
                    2
                ),

                "semantic_analysis":
                    "Matched Trusted Semantic Pattern",

                "score": 0.9
            }

    return {

        "agent": "Semantic Memory Agent",

        "matched_claim": None,

        "similarity": round(
            float(best_score),
            2
        ),

        "semantic_analysis":
            "No Strong Semantic Match",

        "score": 0.5
    }