import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import streamlit as st

from utils.audio import load_audio_to_16k_mono
from services.asr import transcribe
from services.prompts import SOAP_PROMPT, SUMMARY_PROMPT
from services.llm import generate_text

st.set_page_config(page_title="ClinAssist (Demo)", page_icon="🩺", layout="centered")

st.title("🩺 ClinAssist (Demo)")
st.caption("Research/demo only. Not medical advice. Do not upload PHI.")

uploaded = st.file_uploader("Upload audio (wav/mp3/m4a). We'll convert to 16kHz mono.", type=["wav","mp3","m4a","flac","ogg"])

if uploaded:
    st.audio(uploaded)

    if st.button("1) Transcribe with MedASR"):
        with st.spinner("Transcribing..."):
            waveform, sr = load_audio_to_16k_mono(uploaded.read())
            text = transcribe(waveform, sr)
        st.session_state["transcript"] = text

if "transcript" in st.session_state:
    st.subheader("Transcript")
    st.text_area("Transcribed text", st.session_state["transcript"], height=160)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("2) Generate SOAP note"):
            with st.spinner("Generating SOAP note..."):
                prompt = SOAP_PROMPT.format(transcript=st.session_state["transcript"])
                soap = generate_text(prompt, max_new_tokens=600)
            st.session_state["soap"] = soap

    with col2:
        if st.button("3) Summarize"):
            with st.spinner("Summarizing..."):
                prompt = SUMMARY_PROMPT.format(transcript=st.session_state["transcript"])
                summary = generate_text(prompt, max_new_tokens=450)
            st.session_state["summary"] = summary

if "soap" in st.session_state:
    st.subheader("SOAP Note")
    st.text_area("SOAP", st.session_state["soap"], height=260)

if "summary" in st.session_state:
    st.subheader("Summary")
    st.text_area("Summary", st.session_state["summary"], height=220)
