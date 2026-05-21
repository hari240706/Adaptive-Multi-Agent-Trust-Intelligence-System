from agents.nlp_agent import analyze_text

from agents.credibility_agent import analyze_source

from agents.fact_check_agent import verify_claim

from agents.knowledge_graph_agent import analyze_knowledge_graph

from agents.web_verification_agent import verify_with_web

from agents.explanation_agent import generate_explanation

from agents.memory_agent import remember_analysis

from agents.evidence_retrieval_agent import retrieve_evidence

from agents.semantic_memory_agent import semantic_recall

from agents.reasoning_agent import perform_reasoning

from agents.trust_graph_agent import generate_trust_graph

from agents.live_search_agent import live_search_analysis

from agents.planner_agent import create_execution_plan

from agents.debate_agent import run_debate

from agents.source_reputation_agent import analyze_source_reputation

from agents.behavioral_analysis_agent import analyze_behavior

from agents.temporal_analysis_agent import analyze_temporal_consistency

from agents.rag_agent import retrieve_rag_context


def run_agents(text):

    # =========================
    # Planner Agent
    # =========================

    planner_result = create_execution_plan(text)

    # =========================
    # Core Agent Execution
    # =========================

    nlp_result = analyze_text(text)

    credibility_result = analyze_source(text)

    fact_result = verify_claim(text)

    graph_result = analyze_knowledge_graph(text)

    web_result = verify_with_web(text)

    evidence_result = retrieve_evidence(text)

    semantic_result = semantic_recall(text)

    live_search_result = live_search_analysis(text)

    source_reputation_result = analyze_source_reputation(text)

    behavioral_result = analyze_behavior(text)

    temporal_result = analyze_temporal_consistency(text)

    rag_result = retrieve_rag_context(text)

    # =========================
    # Debate Agent
    # =========================

    debate_result = run_debate(

        nlp_result,

        fact_result,

        graph_result
    )

    # =========================
    # Reasoning Agent
    # =========================

    reasoning_result = perform_reasoning(

        nlp_result,

        credibility_result,

        fact_result,

        graph_result,

        web_result,

        evidence_result,

        semantic_result
    )

    # =========================
    # Trust Graph Agent
    # =========================

    trust_graph_result = generate_trust_graph(

        nlp_result,

        credibility_result,

        fact_result,

        graph_result,

        web_result,

        evidence_result,

        semantic_result
    )

    # =========================
    # Initial Weights
    # =========================

    weights = {

        "nlp_weight": 0.10,

        "credibility_weight": 0.07,

        "fact_weight": 0.10,

        "graph_weight": 0.10,

        "web_weight": 0.08,

        "evidence_weight": 0.10,

        "semantic_weight": 0.10,

        "live_search_weight": 0.07,

        "reputation_weight": 0.07,

        "behavioral_weight": 0.07,

        "temporal_weight": 0.07,

        "rag_weight": 0.07
    }

    # =========================
    # Adaptive Weighting
    # =========================

    if fact_result.get("score", 0) < 0.5:

        weights["fact_weight"] += 0.05

    if graph_result.get("score", 0) < 0.5:

        weights["graph_weight"] += 0.05

    if evidence_result.get("score", 0) < 0.5:

        weights["evidence_weight"] += 0.05

    if semantic_result.get("score", 0) < 0.5:

        weights["semantic_weight"] += 0.05

    if web_result.get("score", 0) > 0.8:

        weights["web_weight"] += 0.05

    if source_reputation_result.get("score", 0) > 0.8:

        weights["reputation_weight"] += 0.05

    if behavioral_result.get("score", 0) < 0.5:

        weights["behavioral_weight"] += 0.05

    # =========================
    # Normalize Weights
    # =========================

    total_weight = sum(
        weights.values()
    )

    for key in weights:

        weights[key] /= total_weight

    # =========================
    # Final Trust Score
    # =========================

    final_score = (

        nlp_result.get(
            "confidence",
            0
        ) * weights["nlp_weight"]

        + credibility_result.get(
            "score",
            0
        ) * weights["credibility_weight"]

        + fact_result.get(
            "score",
            0
        ) * weights["fact_weight"]

        + graph_result.get(
            "score",
            0
        ) * weights["graph_weight"]

        + web_result.get(
            "score",
            0
        ) * weights["web_weight"]

        + evidence_result.get(
            "score",
            0
        ) * weights["evidence_weight"]

        + semantic_result.get(
            "score",
            0
        ) * weights["semantic_weight"]

        + live_search_result.get(
            "score",
            0
        ) * weights["live_search_weight"]

        + source_reputation_result.get(
            "score",
            0
        ) * weights["reputation_weight"]

        + behavioral_result.get(
            "score",
            0
        ) * weights["behavioral_weight"]

        + temporal_result.get(
            "score",
            0
        ) * weights["temporal_weight"]

        + rag_result.get(
            "score",
            0
        ) * weights["rag_weight"]
    )

    # =========================
    # Final Prediction
    # =========================

    if final_score >= 0.6:

        final_prediction = "Likely Real"

    else:

        final_prediction = "Likely Fake"

    # =========================
    # Explanation Agent
    # =========================

    explanation_result = generate_explanation(

        nlp_result,

        credibility_result,

        fact_result,

        graph_result,

        web_result
    )

    # =========================
    # Memory Agent
    # =========================

    memory_result = remember_analysis(

        text,

        final_prediction
    )

    # =========================
    # Final Response
    # =========================

    return {

        "final_prediction": final_prediction,

        "trust_score": round(
            final_score,
            2
        ),

        "agent_weights": {

            key: round(value, 2)

            for key, value in weights.items()
        },

        "agents": [

            planner_result,

            nlp_result,

            credibility_result,

            fact_result,

            graph_result,

            web_result,

            evidence_result,

            semantic_result,

            live_search_result,

            source_reputation_result,

            behavioral_result,

            temporal_result,

            rag_result,

            debate_result,

            reasoning_result,

            trust_graph_result,

            explanation_result,

            memory_result
        ]
    }