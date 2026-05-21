SOURCE_REPUTATION = {

    "bbc": 0.95,

    "reuters": 0.96,

    "nature": 0.97,

    "the hindu": 0.85,

    "random_blog": 0.30
}


def analyze_source_reputation(text):

    text = text.lower()

    detected_sources = []

    reputation_scores = []

    for source in SOURCE_REPUTATION:

        if source in text:

            detected_sources.append(source)

            reputation_scores.append(
                SOURCE_REPUTATION[source]
            )

    if reputation_scores:

        avg_score = sum(
            reputation_scores
        ) / len(reputation_scores)

        return {

            "agent": "Source Reputation Agent",

            "sources": detected_sources,

            "average_reputation":
                round(avg_score, 2),

            "score": round(avg_score, 2)
        }

    return {

        "agent": "Source Reputation Agent",

        "sources": [],

        "average_reputation": 0.5,

        "score": 0.5
    }