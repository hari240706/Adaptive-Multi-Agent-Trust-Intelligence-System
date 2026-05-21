async function analyzeNews() {

    const text = document.getElementById(
        "newsInput"
    ).value;

    if (text.trim() === "") {

        alert(
            "Please enter news content."
        );

        return;
    }

    // =========================
    // Loading State
    // =========================

    document.getElementById(
        "finalPrediction"
    ).innerHTML = "Analyzing...";

    document.getElementById(
        "trustScore"
    ).innerHTML = "Trust Score: --";

    document.getElementById(
        "agentsContainer"
    ).innerHTML = "";

    document.getElementById(
        "agentWeights"
    ).innerHTML = "";

    document.getElementById(
        "trustGraph"
    ).innerHTML = "";

    try {

        // =========================
        // API Request
        // =========================

        const response = await fetch(

            "http://127.0.0.1:8000/predict",

            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({
                    text: text
                })
            }
        );

        const data = await response.json();

        console.log(data);

        // =========================
        // Prediction
        // =========================

        document.getElementById(
            "finalPrediction"
        ).innerHTML =

            data.final_prediction ||
            "Unknown";

        document.getElementById(
            "trustScore"
        ).innerHTML =

            `Trust Score: ${data.trust_score || "--"}`;

        // =========================
        // Agent Weights
        // =========================

        let weightsHTML = "";

        if (data.agent_weights) {

            for (const key in data.agent_weights) {

                const weight =
                    data.agent_weights[key];

                const percentage =
                    Math.round(weight * 100);

                weightsHTML += `

                    <div class="weight-item">

                        <div class="weight-header">

                            <span>
                                ${key}
                            </span>

                            <span>
                                ${percentage}%
                            </span>

                        </div>

                        <div class="weight-bar">

                            <div
                                class="weight-fill"

                                style="
                                    width:
                                    ${percentage}%;
                                "
                            ></div>

                        </div>

                    </div>
                `;
            }
        }

        document.getElementById(
            "agentWeights"
        ).innerHTML = weightsHTML;

        // =========================
        // Agent Outputs
        // =========================

        let agentsHTML = "";

        if (data.agents) {

            data.agents.forEach(agent => {

                agentsHTML += `

                    <div class="agent-card">

                        <h3>
                            ${agent.agent}
                        </h3>

                        <div class="agent-output">

<pre>
${JSON.stringify(agent, null, 2)}
</pre>

                        </div>

                    </div>
                `;
            });
        }

        document.getElementById(
            "agentsContainer"
        ).innerHTML = agentsHTML;

        // =========================
        // Trust Graph
        // =========================

        if (data.agents) {

            const trustGraphAgent = data.agents.find(

                agent =>

                agent.agent === "Trust Graph Agent"
            );

            if (
                trustGraphAgent &&
                trustGraphAgent.nodes &&
                trustGraphAgent.edges
            ) {

                const nodes = trustGraphAgent.nodes.map(

                    node => ({

                        data: {

                            id: node.id,

                            label:
                                `${node.id}\nScore: ${node.score}`
                        }
                    })
                );

                const edges = trustGraphAgent.edges.map(

                    edge => ({

                        data: {

                            source: edge.source,

                            target: edge.target
                        }
                    })
                );

                cytoscape({

                    container:
                        document.getElementById(
                            "trustGraph"
                        ),

                    elements: [

                        ...nodes,

                        ...edges
                    ],

                    style: [

                        {

                            selector: "node",

                            style: {

                                "background-color":
                                    "#38bdf8",

                                "label":
                                    "data(label)",

                                "text-valign":
                                    "center",

                                "text-halign":
                                    "center",

                                "color":
                                    "#ffffff",

                                "font-size":
                                    "10px",

                                "text-wrap":
                                    "wrap",

                                "text-max-width":
                                    "80px"
                            }
                        },

                        {

                            selector: "edge",

                            style: {

                                "width": 3,

                                "line-color":
                                    "#94a3b8",

                                "target-arrow-color":
                                    "#94a3b8",

                                "target-arrow-shape":
                                    "triangle",

                                "curve-style":
                                    "bezier"
                            }
                        }
                    ],

                    layout: {

                        name: "circle"
                    }
                });
            }
        }

    } catch (error) {

        console.error(error);

        document.getElementById(
            "finalPrediction"
        ).innerHTML =

            "Error during analysis";

        document.getElementById(
            "trustScore"
        ).innerHTML =

            "Backend connection failed";
    }
}