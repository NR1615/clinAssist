ClinAssist

Medical Speech → Structured Clinical Notes (Research Demo)

Welcome to ClinAssist! This project is a demonstration of how AI can transform medical speech dictation into structured clinical documentation. Whether you're exploring AI in healthcare or building your portfolio, ClinAssist showcases the potential of open medical AI models.

Disclaimer
This project is for research and learning purposes only. It is not intended for real clinical use. Please do not upload real patient data or any personally identifiable health information (PHI).

Features

Upload medical-style audio dictation
Medical-domain speech recognition (ASR)
Automatic generation of:
  - SOAP notes (Subjective / Objective / Assessment / Plan)
  - Concise clinical summaries
Simple and intuitive web interface
Local-first processing to ensure data privacy

How It Works

Audio Upload: Users upload a short audio file containing medical dictation.
Audio Preprocessing: The audio is converted to mono, resampled to 16 kHz, and normalized for compatibility with medical ASR models.
Medical Speech Recognition: The processed audio is transcribed using MedASR, a model optimized for clinical vocabulary.
Prompt-Based Medical Reasoning: The transcript is processed by a medical language model to ensure factual accuracy and structured output.
Structured Output: The system generates SOAP notes and concise summaries for quick review.

Tools and Technologies

Frontend: Streamlit for an interactive user interface
Models: MedASR for speech recognition, MedGemma for medical reasoning
Audio Processing: Librosa, SoundFile
ML Frameworks: PyTorch, Hugging Face Transformers

Getting Started

Set up the environment:
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

Run the app:
   streamlit run app/streamlit_app.py

Optional: Add a Hugging Face token in a .env file for enhanced model access.

Future Plans

PHI detection and masking
Support for longer dictations
Dockerized deployment
Automated testing
Multimodal extensions (e.g., image + text)

Thank you for exploring ClinAssist! Feel free to contribute or reach out with feedback.