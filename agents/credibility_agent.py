TRUSTED_SOURCES = [
    "bbc",
    "reuters",
    "the hindu",
    "nature",
    "nasa"
]


def analyze_source(text):

    text = text.lower()

    for source in TRUSTED_SOURCES:

        if source in text:

            return {
                "agent": "Credibility Agent",
                "credibility": "High",
                "score": 0.9
            }

    return {
        "agent": "Credibility Agent",
        "credibility": "Unknown",
        "score": 0.5
    }