import torch

from transformers import (

    AutoTokenizer,

    AutoModelForSequenceClassification
)


# =========================
# Load Model
# =========================

MODEL_PATH = "models/distilbert_model"

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_PATH
)

model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_PATH
)

model.eval()


# =========================
# NLP Analysis Agent
# =========================

def analyze_text(text):

    # Tokenize input
    inputs = tokenizer(

        text,

        return_tensors="pt",

        truncation=True,

        padding=True,

        max_length=256
    )

    # Remove token_type_ids
    # DistilBERT does not support them
    if "token_type_ids" in inputs:

        del inputs["token_type_ids"]

    # Disable gradients
    with torch.no_grad():

        outputs = model(**inputs)

    # Get logits
    logits = outputs.logits

    # Probabilities
    probabilities = torch.softmax(

        logits,

        dim=1
    )

    # Prediction
    prediction = torch.argmax(

        probabilities,

        dim=1
    ).item()

    # Confidence
    confidence = torch.max(
        probabilities
    ).item()

    # Label mapping
    if prediction == 1:

        label = "Real"

    else:

        label = "Fake"

    return {

        "agent":
        "NLP Agent",

        "prediction":
        label,

        "confidence":
        round(confidence, 2)
    }