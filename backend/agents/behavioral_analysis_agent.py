EMOTIONAL_PATTERNS = [

    "shocking",

    "unbelievable",

    "they don't want you to know",

    "secret truth",

    "must watch",

    "wake up"
]


def analyze_behavior(text):

    text = text.lower()

    detected_patterns = []

    for pattern in EMOTIONAL_PATTERNS:

        if pattern in text:

            detected_patterns.append(pattern)

    if detected_patterns:

        return {

            "agent": "Behavioral Analysis Agent",

            "patterns_detected":
                detected_patterns,

            "behavior_analysis":
                "Manipulative or propaganda-like language detected",

            "score": 0.3
        }

    return {

        "agent": "Behavioral Analysis Agent",

        "patterns_detected": [],

        "behavior_analysis":
            "No strong manipulative patterns detected",

        "score": 0.8
    }