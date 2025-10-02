from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

MODEL_NAME = "distilgpt2"  # small, free, offline
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

def ask_ai(prompt: str, max_length=100):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(
        inputs,
        max_length=max_length,
        do_sample=True,
        top_p=0.9,
        top_k=50
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response
