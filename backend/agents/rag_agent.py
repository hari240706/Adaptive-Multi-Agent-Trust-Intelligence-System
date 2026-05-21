RAG_KNOWLEDGE_BASE = [

    "NASA launched climate monitoring satellites.",

    "BBC published reports about climate agreements.",

    "WHO released healthcare advisories."
]


def retrieve_rag_context(text):

    text = text.lower()

    retrieved_context = []

    for knowledge in RAG_KNOWLEDGE_BASE:

        if any(

            word in knowledge.lower()

            for word in text.split()
        ):

            retrieved_context.append(
                knowledge
            )

    if retrieved_context:

        return {

            "agent": "RAG Agent",

            "retrieved_context":
                retrieved_context,

            "rag_analysis":
                "Relevant contextual knowledge retrieved",

            "score": 0.85
        }

    return {

        "agent": "RAG Agent",

        "retrieved_context": [],

        "rag_analysis":
            "No contextual knowledge retrieved",

        "score": 0.5
    }