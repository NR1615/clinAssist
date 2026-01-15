from functools import lru_cache
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Replace with actual MedGemma model id (e.g., a MedGemma 1.5 4B instruct/checkpoint)
MEDGEMMA_MODEL_ID = "google/medgemma-1.5-4b"

@lru_cache(maxsize=1)
def get_llm():
    tokenizer = AutoTokenizer.from_pretrained(MEDGEMMA_MODEL_ID, use_fast=True)
    model = AutoModelForCausalLM.from_pretrained(
        MEDGEMMA_MODEL_ID,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        device_map="auto" if torch.cuda.is_available() else None,
    )
    return tokenizer, model

def generate_text(prompt: str, max_new_tokens: int = 512) -> str:
    tokenizer, model = get_llm()
    inputs = tokenizer(prompt, return_tensors="pt")
    if torch.cuda.is_available():
        inputs = {k: v.to("cuda") for k, v in inputs.items()}

    with torch.no_grad():
        out = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
        )
    text = tokenizer.decode(out[0], skip_special_tokens=True)
    # crude: strip original prompt if it echoes
    if text.startswith(prompt):
        text = text[len(prompt):]
    return text.strip()
