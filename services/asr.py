from functools import lru_cache
import torch
from transformers import pipeline

# Replace this with the exact MedASR model id from Hugging Face
# Example placeholder: "google/medasr"
MEDASR_MODEL_ID = "google/medasr"

@lru_cache(maxsize=1)
def get_asr_pipe():
    device = 0 if torch.cuda.is_available() else -1
    return pipeline(
        task="automatic-speech-recognition",
        model=MEDASR_MODEL_ID,
        device=device,
    )

def transcribe(waveform, sample_rate: int = 16000) -> str:
    asr = get_asr_pipe()
    out = asr({"array": waveform, "sampling_rate": sample_rate})
    # Transformers returns dict with 'text' in most ASR pipelines
    return out.get("text", "").strip()
