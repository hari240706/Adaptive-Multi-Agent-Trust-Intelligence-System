from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

import sys
import os

# Add agents folder to path
sys.path.append(
    os.path.abspath("../agents")
)

# Import orchestrator
from orchestrator import run_agents

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


# Request schema
class NewsRequest(BaseModel):
    text: str


# Home route
@app.get("/")
def home():

    return {
        "message": "AMATIS Multi-Agent API Running Successfully"
    }


# Prediction route
@app.post("/predict")
def predict_news(request: NewsRequest):

    # Run all agents
    result = run_agents(
        request.text
    )

    # Return multi-agent result
    return result