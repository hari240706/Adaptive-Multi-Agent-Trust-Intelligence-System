def generate_explanation(

    nlp_result,

    credibility_result,

    fact_result,

    graph_result,

    web_result
):

    explanations = []

    # NLP reasoning
    explanations.append(

        f"NLP Agent predicted "

        f"{nlp_result['prediction']} "

        f"with confidence "

        f"{nlp_result['confidence']}."
    )

    # Credibility reasoning
    explanations.append(

        f"Credibility analysis result: "

        f"{credibility_result['credibility']}."
    )

    # Fact-check reasoning
    explanations.append(

        f"Fact-check analysis: "

        f"{fact_result['fact_check']}."
    )

    # Graph reasoning
    explanations.append(

        f"Knowledge graph analysis: "

        f"{graph_result['graph_analysis']}."
    )

    # Web verification reasoning
    explanations.append(

        f"Web verification result: "

        f"{web_result['verification']}."
    )

    return {

        "agent": "Explanation Agent",

        "explanation": explanations
    }