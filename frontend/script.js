async function analyzeNews() {

    const text = document.getElementById(
        "newsInput"
    ).value;

    const response = await fetch(
        "http://127.0.0.1:8000/predict",

        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                text: text
            })
        }
    );

    const data = await response.json();

    let agentHTML = "";

    data.agents.forEach(agent => {

        agentHTML += `

            <div class="agent-card">

                <h3>${agent.agent}</h3>

                <pre>
${JSON.stringify(agent, null, 2)}
                </pre>

            </div>
        `;
    });

    document.getElementById(
        "result"
    ).innerHTML = `

        <div class="result-card">

            <h2>
                Final Prediction:
                ${data.final_prediction}
            </h2>

            <h3>
                Trust Score:
                ${data.trust_score}
            </h3>

            <hr>

            ${agentHTML}

        </div>
    `;
}