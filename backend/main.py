from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Initialize FastAPI app
app = FastAPI()

# Load trained model and vectorizer
model = joblib.load("../models/logistic_model.pkl")
vectorizer = joblib.load("../models/tfidf_vectorizer.pkl")


# Request schema
class NewsRequest(BaseModel):
    text: str


# Home route
@app.get("/")
def home():
    return {
        "message": "AMATIS API Running Successfully"
    }


# Prediction route
@app.post("/predict")
def predict_news(request: NewsRequest):

    # Transform input text
    transformed_text = vectorizer.transform(
        [request.text]
    )

    # Predict class
    prediction = model.predict(
        transformed_text
    )[0]

    # Prediction probability
    probability = model.predict_proba(
        transformed_text
    )[0]

    confidence = max(probability)

    # Label mapping
    if prediction == 1:
        label = "Real News"
    else:
        label = "Fake News"

    # Return response
    return {
        "prediction": label,
        "confidence": round(float(confidence), 2)
    }