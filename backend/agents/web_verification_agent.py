TRUSTED_DOMAINS = [

    "bbc",

    "reuters",

    "nasa",

    "nature",

    "the hindu"
]


def verify_with_web(text):

    text = text.lower()

    for domain in TRUSTED_DOMAINS:

        if domain in text:

            return {

                "agent": "Web Verification Agent",

                "verification": "Trusted Reference Found",

                "score": 0.9
            }

    return {

        "agent": "Web Verification Agent",

        "verification": "No Trusted Evidence Found",

        "score": 0.4
    }