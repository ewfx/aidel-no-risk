# Load model directly
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("msr2903/mrm8488-distilroberta-fine-tuned-financial-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("msr2903/mrm8488-distilroberta-fine-tuned-financial-sentiment")

import torch
import scipy

preds = []
preds_proba = []
tokenizer_kwargs = {"padding": True, "truncation": True, "max_length": 512}

def evaluate(queries):
    with torch.no_grad():
        input_sequence = tokenizer(queries, return_tensors="pt", **tokenizer_kwargs)
        logits = model(**input_sequence).logits
        scores = {
        k: v
        for k, v in zip(
            model.config.id2label.values(),
            scipy.special.softmax(logits.numpy().squeeze()),
        )
    }
    sentimentFinbert = max(scores, key=scores.get)
    probabilityFinbert = max(scores.values())
    preds.append(sentimentFinbert)
    preds_proba.append(probabilityFinbert)
    return preds_proba.mean()