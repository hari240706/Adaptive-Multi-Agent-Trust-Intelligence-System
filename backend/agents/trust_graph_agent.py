def generate_trust_graph(

    nlp_result,

    credibility_result,

    fact_result,

    graph_result,

    web_result,

    evidence_result,

    semantic_result
):

    nodes = [

        {
            "id": "NLP Agent",
            "score": nlp_result["confidence"]
        },

        {
            "id": "Credibility Agent",
            "score": credibility_result["score"]
        },

        {
            "id": "Fact Check Agent",
            "score": fact_result["score"]
        },

        {
            "id": "Knowledge Graph Agent",
            "score": graph_result["score"]
        },

        {
            "id": "Web Verification Agent",
            "score": web_result["score"]
        },

        {
            "id": "Evidence Retrieval Agent",
            "score": evidence_result["score"]
        },

        {
            "id": "Semantic Memory Agent",
            "score": semantic_result["score"]
        },

        {
            "id": "Orchestrator",
            "score": 1.0
        }
    ]

    edges = [

        {
            "source": "NLP Agent",
            "target": "Orchestrator"
        },

        {
            "source": "Credibility Agent",
            "target": "Orchestrator"
        },

        {
            "source": "Fact Check Agent",
            "target": "Orchestrator"
        },

        {
            "source": "Knowledge Graph Agent",
            "target": "Orchestrator"
        },

        {
            "source": "Web Verification Agent",
            "target": "Orchestrator"
        },

        {
            "source": "Evidence Retrieval Agent",
            "target": "Orchestrator"
        },

        {
            "source": "Semantic Memory Agent",
            "target": "Orchestrator"
        }
    ]

    return {

        "agent": "Trust Graph Agent",

        "nodes": nodes,

        "edges": edges
    }