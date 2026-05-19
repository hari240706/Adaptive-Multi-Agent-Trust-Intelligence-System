from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

import torch

from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification
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

# Load DistilBERT model and tokenizer
MODEL_PATH = "../models/distilbert_model"

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_PATH
)

model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_PATH
)

# Set model to evaluation mode
model.eval()


# Request schema
class NewsRequest(BaseModel):
    text: str


# Home route
@app.get("/")
def home():

    return {
        "message": "AMATIS Transformer API Running Successfully"
    }


# Prediction route
@app.post("/predict")
def predict_news(request: NewsRequest):

    # Tokenize input text
    inputs = tokenizer(
        request.text,

        return_tensors="pt",

        truncation=True,

        padding=True,

        max_length=256
    )

    # Disable gradient calculation
    with torch.no_grad():

        outputs = model(**inputs)

    # Get logits
    logits = outputs.logits

    # Convert logits to probabilities
    probabilities = torch.softmax(
        logits,
        dim=1
    )

    # Get predicted class
    prediction = torch.argmax(
        probabilities,
        dim=1
    ).item()

    # Get confidence score
    confidence = torch.max(
        probabilities
    ).item()

    # Label mapping
    if prediction == 1:
        label = "Real News"
    else:
        label = "Fake News"

    # Return response
    return {
        "prediction": label,
        "confidence": round(confidence, 2)
    }