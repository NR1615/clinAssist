import io
import numpy as np
import soundfile as sf
import librosa

def load_audio_to_16k_mono(file_bytes: bytes):
    """
    Loads audio bytes and converts to 16kHz mono float32 waveform.
    Returns (waveform, sample_rate=16000)
    """
    data, sr = sf.read(io.BytesIO(file_bytes), always_2d=False)
    if data.ndim > 1:
        data = np.mean(data, axis=1)  # stereo -> mono
    # librosa expects float
    data = data.astype(np.float32)
    if sr != 16000:
        data = librosa.resample(data, orig_sr=sr, target_sr=16000)
        sr = 16000
    return data, sr
