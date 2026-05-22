let trustChartInstance = null;

let websocket = null;


// =========================
// Initialize WebSocket
// =========================

function initializeWebSocket() {

    websocket = new WebSocket(
        "ws://127.0.0.1:8000/ws"
    );

    websocket.onopen = () => {

        console.log(
            "AMATIS Live Stream Connected"
        );

        websocket.send(
            "Frontend Connected"
        );
    };

    websocket.onmessage = (event) => {

        const data = JSON.parse(
            event.data
        );

        console.log(
            "Live Update:",
            data
        );

        // =========================
        // Live Telemetry Notification
        // =========================

        if (
            data.type === "live_analysis"
        ) {

            showLiveNotification(

                `New Analysis → ${data.final_prediction}
                 | Trust Score: ${data.trust_score}`
            );
        }
    };

    websocket.onerror = (error) => {

        console.error(
            "WebSocket Error:",
            error
        );
    };

    websocket.onclose = () => {

        console.warn(
            "WebSocket Disconnected"
        );

        // Reconnect automatically
        setTimeout(() => {

            initializeWebSocket();

        }, 3000);
    };
}


// =========================
// Live Notification
// =========================

function showLiveNotification(message) {

    const notification = document.createElement(
        "div"
    );

    notification.className =
        "live-notification";

    notification.innerHTML = message;

    document.body.appendChild(
        notification
    );

    setTimeout(() => {

        notification.remove();

    }, 4000);
}


// =========================
// Analyze News
// =========================

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

        // =========================
        // Error Handling
        // =========================

        if (!response.ok) {

            throw new Error(
                "Backend request failed"
            );
        }

        const data = await response.json();

        console.log(data);

        // =========================
        // Final Prediction
        // =========================

        document.getElementById(
            "finalPrediction"
        ).innerHTML =

            data.final_prediction ||
            "Unknown";

        // Prediction color
        if (
            data.final_prediction ===
            "Likely Real"
        ) {

            document.getElementById(
                "finalPrediction"
            ).style.color = "#22c55e";

        } else {

            document.getElementById(
                "finalPrediction"
            ).style.color = "#ef4444";
        }

        // =========================
        // Trust Score
        // =========================

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

                agent.agent ===
                "Trust Graph Agent"
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
                                    "90px",

                                "width":
                                    "75px",

                                "height":
                                    "75px",

                                "border-width":
                                    2,

                                "border-color":
                                    "#0ea5e9"
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

        // =========================
        // Refresh Analytics
        // =========================

        loadAnalytics();

        loadHistory();

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


// =========================
// Load Analytics
// =========================

async function loadAnalytics() {

    try {

        const response = await fetch(

            "http://127.0.0.1:8000/analytics"
        );

        const data = await response.json();

        document.getElementById(
            "analytics"
        ).innerHTML = `

            <div class="analytics-card">

                <h3>
                    Total Analyses:
                    ${data.database_stats.total_analyses}
                </h3>

                <h3>
                    Stored Claims:
                    ${data.vector_memory_stats.stored_claims}
                </h3>

                <h3>
                    Vector Dimension:
                    ${data.vector_memory_stats.vector_dimension}
                </h3>

            </div>
        `;

    } catch (error) {

        console.error(error);
    }
}


// =========================
// Load History
// =========================

async function loadHistory() {

    try {

        const response = await fetch(

            "http://127.0.0.1:8000/history"
        );

        const data = await response.json();

        let historyHTML = "";

        let trustScores = [];

        let labels = [];

        data.recent_analyses.forEach((item, index) => {

            historyHTML += `

                <div class="history-card">

                    <h3>
                        ${item.prediction}
                    </h3>

                    <p>
                        Trust Score:
                        ${item.trust_score}
                    </p>

                    <p>
                        ${item.timestamp}
                    </p>

                </div>
            `;

            trustScores.push(
                item.trust_score
            );

            labels.push(
                `Analysis ${index + 1}`
            );
        });

        document.getElementById(
            "history"
        ).innerHTML = historyHTML;

        // Destroy previous chart
        if (trustChartInstance) {

            trustChartInstance.destroy();
        }

        const ctx = document.getElementById(
            "trustChart"
        );

        trustChartInstance = new Chart(ctx, {

            type: "line",

            data: {

                labels: labels,

                datasets: [

                    {

                        label:
                        "Trust Scores",

                        data:
                        trustScores,

                        borderWidth: 3,

                        tension: 0.4,

                        fill: true
                    }
                ]
            },

            options: {

                responsive: true,

                plugins: {

                    legend: {

                        display: true
                    }
                },

                scales: {

                    y: {

                        beginAtZero: true,

                        max: 1
                    }
                }
            }
        });

    } catch (error) {

        console.error(error);
    }
}


// =========================
// Initialize Dashboard
// =========================

initializeWebSocket();

loadAnalytics();

loadHistory();