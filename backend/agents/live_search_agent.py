TRUSTED_NEWS_SOURCES = [

    "bbc",

    "reuters",

    "associated press",

    "the hindu",

    "nature"
]


def live_search_analysis(text):

    text = text.lower()

    matched_sources = []

    for source in TRUSTED_NEWS_SOURCES:

        if source in text:

            matched_sources.append(source)

    if matched_sources:

        return {

            "agent": "Live Search Agent",

            "sources_found": matched_sources,

            "search_analysis":
                "Trusted live references detected",

            "score": 0.9
        }

    return {

        "agent": "Live Search Agent",

        "sources_found": [],

        "search_analysis":
            "No trusted live references found",

        "score": 0.4
    }