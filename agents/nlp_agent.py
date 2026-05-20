import torch

from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification
)

MODEL_PATH = "../models/distilbert_model"

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_PATH
)

model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_PATH
)

model.eval()


def analyze_text(text):

    inputs = tokenizer(
        text,

        return_tensors="pt",

        truncation=True,

        padding=True,

        max_length=256
    )

    with torch.no_grad():

        outputs = model(**inputs)

    logits = outputs.logits

    probabilities = torch.softmax(
        logits,
        dim=1
    )

    prediction = torch.argmax(
        probabilities,
        dim=1
    ).item()

    confidence = torch.max(
        probabilities
    ).item()

    if prediction == 1:
        label = "Real"
    else:
        label = "Fake"

    return {
        "agent": "NLP Agent",
        "prediction": label,
        "confidence": round(confidence, 2)
    }