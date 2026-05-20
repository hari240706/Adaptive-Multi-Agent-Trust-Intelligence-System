from nlp_agent import analyze_text

from credibility_agent import analyze_source

from fact_check_agent import verify_claim


def run_agents(text):

    nlp_result = analyze_text(text)

    credibility_result = analyze_source(text)

    fact_result = verify_claim(text)

    final_score = (
        nlp_result["confidence"]
        + credibility_result["score"]
        + fact_result["score"]
    ) / 3

    if final_score >= 0.6:
        final_prediction = "Likely Real"
    else:
        final_prediction = "Likely Fake"

    return {
        "final_prediction": final_prediction,
        "trust_score": round(final_score, 2),

        "agents": [
            nlp_result,
            credibility_result,
            fact_result
        ]
    }