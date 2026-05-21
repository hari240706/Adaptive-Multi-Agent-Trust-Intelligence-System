KNOWN_ENTITIES = {

    "nasa": "space_agency",

    "bbc": "news_organization",

    "reuters": "news_organization",

    "india": "country",

    "usa": "country",

    "government": "institution",

    "scientists": "profession"
}


SUSPICIOUS_RELATIONS = [

    ("aliens", "world leaders"),

    ("lizard society", "global elections"),

    ("miracle cure", "all diseases"),

    ("aliens", "global leaders")
]


def analyze_knowledge_graph(text):

    text = text.lower()

    detected_entities = []

    for entity in KNOWN_ENTITIES:

        if entity in text:

            detected_entities.append(entity)

    for relation in SUSPICIOUS_RELATIONS:

        if relation[0] in text and relation[1] in text:

            return {

                "agent": "Knowledge Graph Agent",

                "graph_analysis": "Suspicious Entity Relationship",

                "entities": detected_entities,

                "score": 0.2
            }

    return {

        "agent": "Knowledge Graph Agent",

        "graph_analysis": "No Suspicious Entity Relationship",

        "entities": detected_entities,

        "score": 0.8
    }