from fastapi import FastAPI

from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware

# Import orchestrator
from agents.orchestrator import run_agents

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

        "message":
        "AMATIS Multi-Agent API Running Successfully"
    }


# Prediction route
@app.post("/predict")
def predict_news(request: NewsRequest):

    # Run all agents
    result = run_agents(
        request.text
    )

    # Return orchestrated result
    return result