SUSPICIOUS_KEYWORDS = [

    "aliens",

    "miracle cure",

    "secret treaty",

    "world leaders",

    "lizard society",

    "hidden satellites",

    "conspiracy",

    "mind control",

    "secret underground"
]


def verify_claim(text):

    text = text.lower()

    for keyword in SUSPICIOUS_KEYWORDS:

        if keyword in text:

            return {
                "agent": "Fact Check Agent",

                "fact_check": "Suspicious Claim",

                "score": 0.2
            }

    return {
        "agent": "Fact Check Agent",

        "fact_check": "No Suspicious Pattern",

        "score": 0.8
    }