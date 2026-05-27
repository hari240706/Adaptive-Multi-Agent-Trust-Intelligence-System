import requests


# =========================
# Trusted Sources
# =========================

TRUSTED_SOURCES = [

    "bbc",

    "reuters",

    "ap",

    "who",

    "nasa",

    "un"
]


# =========================
# Search Agent
# =========================

def search_realtime_sources(text):

    found_sources = []

    text_lower = text.lower()

    for source in TRUSTED_SOURCES:

        if source in text_lower:

            found_sources.append(
                source.upper()
            )

    # Simple confidence logic
    if len(found_sources) >= 2:

        score = 0.9

        analysis = (
            "Multiple trusted sources detected"
        )

    elif len(found_sources) == 1:

        score = 0.7

        analysis = (
            "Trusted source indicator detected"
        )

    else:

        score = 0.4

        analysis = (
            "No trusted source indicators found"
        )

    return {

        "agent":
        "Real-Time Search Agent",

        "sources":
        found_sources,

        "analysis":
        analysis,

        "score":
        score
    }