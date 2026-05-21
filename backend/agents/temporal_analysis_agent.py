CURRENT_YEAR = 2026


def analyze_temporal_consistency(text):

    text = text.lower()

    suspicious = False

    if "2020" in text \
       and "future ai government" in text:

        suspicious = True

    if suspicious:

        return {

            "agent": "Temporal Analysis Agent",

            "temporal_analysis":
                "Timeline inconsistency detected",

            "score": 0.3
        }

    return {

        "agent": "Temporal Analysis Agent",

        "temporal_analysis":
            "Timeline appears consistent",

        "score": 0.8
    }