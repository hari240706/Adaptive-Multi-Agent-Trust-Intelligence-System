KNOWN_FAKE_CLAIMS = [

    "aliens elected as world leaders",

    "miracle cure removes all diseases",

    "secret underground lizard society"
]

KNOWN_REAL_CLAIMS = [

    "nasa launched satellite",

    "government announced reforms",

    "bbc reported climate agreements"
]


def retrieve_evidence(text):

    text = text.lower()

    # Check fake evidence
    for claim in KNOWN_FAKE_CLAIMS:

        if claim in text:

            return {

                "agent": "Evidence Retrieval Agent",

                "evidence": "Matched Known Fake Claim",

                "score": 0.2
            }

    # Check real evidence
    for claim in KNOWN_REAL_CLAIMS:

        if claim in text:

            return {

                "agent": "Evidence Retrieval Agent",

                "evidence": "Matched Known Real Claim",

                "score": 0.9
            }

    # Unknown evidence
    return {

        "agent": "Evidence Retrieval Agent",

        "evidence": "No Matching Evidence Found",

        "score": 0.5
    }