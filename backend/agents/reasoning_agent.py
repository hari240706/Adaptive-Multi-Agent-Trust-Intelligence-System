def perform_reasoning(

    nlp_result,

    credibility_result,

    fact_result,

    graph_result,

    web_result,

    evidence_result,

    semantic_result
):

    reasoning_steps = []

    # NLP reasoning
    if nlp_result["confidence"] > 0.75:

        reasoning_steps.append(

            "NLP Agent detected strong linguistic confidence."
        )

    else:

        reasoning_steps.append(

            "NLP Agent confidence is moderate or weak."
        )

    # Credibility reasoning
    if credibility_result["score"] > 0.8:

        reasoning_steps.append(

            "Trusted source indicators detected."
        )

    else:

        reasoning_steps.append(

            "Source credibility remains uncertain."
        )

    # Fact-check reasoning
    if fact_result["score"] < 0.5:

        reasoning_steps.append(

            "Fact-check system detected suspicious claims."
        )

    # Knowledge graph reasoning
    if graph_result["score"] < 0.5:

        reasoning_steps.append(

            "Knowledge graph found suspicious entity relationships."
        )

    # Web verification reasoning
    if web_result["score"] > 0.8:

        reasoning_steps.append(

            "Web verification found trusted references."
        )

    # Evidence retrieval reasoning
    if evidence_result["score"] < 0.5:

        reasoning_steps.append(

            "Evidence retrieval matched known misinformation patterns."
        )

    # Semantic reasoning
    if semantic_result["score"] < 0.5:

        reasoning_steps.append(

            "Semantic memory detected similarity to suspicious claims."
        )

    # Final reasoning synthesis
    if (
        fact_result["score"] < 0.5
        or graph_result["score"] < 0.5
        or evidence_result["score"] < 0.5
        or semantic_result["score"] < 0.5
    ):

        conclusion = (

            "Multiple agents detected suspicious patterns. "
            "Overall trust level is reduced."
        )

    else:

        conclusion = (

            "Most agents detected consistent and trustworthy patterns."
        )

    return {

        "agent": "Reasoning Agent",

        "reasoning_steps": reasoning_steps,

        "conclusion": conclusion
    }