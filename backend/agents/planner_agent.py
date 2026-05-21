def create_execution_plan(text):

    text = text.lower()

    selected_agents = [

        "NLP Agent",

        "Credibility Agent"
    ]

    if "alien" in text \
       or "conspiracy" in text \
       or "secret" in text:

        selected_agents.append(
            "Fact Check Agent"
        )

        selected_agents.append(
            "Knowledge Graph Agent"
        )

    if "bbc" in text \
       or "reuters" in text \
       or "nasa" in text:

        selected_agents.append(
            "Web Verification Agent"
        )

    return {

        "agent": "Planner Agent",

        "execution_plan": selected_agents
    }