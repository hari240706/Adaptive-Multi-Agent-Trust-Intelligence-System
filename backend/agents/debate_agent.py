def run_debate(

    nlp_result,

    fact_result,

    graph_result
):

    debate_points = []

    if nlp_result["prediction"] == "Real":

        debate_points.append(

            "NLP Agent believes the text resembles real news."
        )

    if fact_result["score"] < 0.5:

        debate_points.append(

            "Fact Check Agent argues that suspicious claims exist."
        )

    if graph_result["score"] < 0.5:

        debate_points.append(

            "Knowledge Graph Agent detected inconsistent relationships."
        )

    if fact_result["score"] < 0.5 \
       or graph_result["score"] < 0.5:

        final_debate = (

            "Suspicious evidence outweighs linguistic confidence."
        )

    else:

        final_debate = (

            "No major contradictions detected between agents."
        )

    return {

        "agent": "Debate Agent",

        "debate_points": debate_points,

        "debate_conclusion": final_debate
    }