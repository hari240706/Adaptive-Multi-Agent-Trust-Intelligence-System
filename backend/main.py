from fastapi import FastAPI

from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware

# Import orchestrator
from agents.orchestrator import run_agents

# Import analytics system
from agents.analytics_agent import (

    get_system_analytics,

    get_analysis_history
)

# Initialize FastAPI app
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


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
def predict_news(request: NewsRequest):

    # Run multi-agent orchestration
    result = run_agents(
        request.text
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