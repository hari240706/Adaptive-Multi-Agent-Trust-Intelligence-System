from fastapi import FastAPI

from fastapi import WebSocket

from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware

# Import orchestrator
from agents.orchestrator import run_agents

# Import analytics system
from agents.analytics_agent import (

    get_system_analytics,

    get_analysis_history
)

# =========================
# Initialize FastAPI App
# =========================

app = FastAPI()

# =========================
# Enable CORS
# =========================

app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

# =========================
# Active WebSocket Clients
# =========================

active_connections = []

# =========================
# Request Schema
# =========================

class NewsRequest(BaseModel):

    text: str


# =========================
# Home Route
# =========================

@app.get("/")
def home():

    return {

        "message":
        "AMATIS Multi-Agent API Running Successfully"
    }


# =========================
# Prediction Route
# =========================

@app.post("/predict")
async def predict_news(request: NewsRequest):

    # Run multi-agent orchestration
    result = run_agents(
        request.text
    )

    # =========================
    # Broadcast Live Update
    # =========================

    disconnected_connections = []

    for connection in active_connections:

        try:

            await connection.send_json({

                "type":
                "live_analysis",

                "final_prediction":
                result.get(
                    "final_prediction"
                ),

                "trust_score":
                result.get(
                    "trust_score"
                )
            })

        except:

            disconnected_connections.append(
                connection
            )

    # Remove disconnected sockets
    for connection in disconnected_connections:

        if connection in active_connections:

            active_connections.remove(
                connection
            )

    # Return orchestrated response
    return result


# =========================
# Analytics Route
# =========================

@app.get("/analytics")
def analytics():

    return get_system_analytics()


# =========================
# History Route
# =========================

@app.get("/history")
def history():

    return get_analysis_history()


# =========================
# WebSocket Endpoint
# =========================

@app.websocket("/ws")
async def websocket_endpoint(

    websocket: WebSocket
):

    # Accept connection
    await websocket.accept()

    # Store active connection
    active_connections.append(
        websocket
    )

    print(
        "WebSocket Client Connected"
    )

    try:

        while True:

            # Receive frontend message
            data = await websocket.receive_text()

            print(
                "Live Message:",
                data
            )

            # Send heartbeat response
            await websocket.send_json({

                "type":
                "connection",

                "status":
                "active",

                "message":
                "AMATIS live telemetry connected"
            })

    except Exception as error:

        print(
            "WebSocket Disconnected:",
            error
        )

        if websocket in active_connections:

            active_connections.remove(
                websocket
            )