SOAP_PROMPT = """You are a clinical documentation assistant.
Convert the following transcript into a SOAP note with headings:
Subjective, Objective, Assessment, Plan.
Keep it concise. Do NOT invent facts. If something is unknown, write "Not stated".

Transcript:
{transcript}
"""

SUMMARY_PROMPT = """Summarize the following clinical transcript into:
- Key complaints / symptoms
- Relevant history
- Medications (if mentioned)
- Tests / results (if mentioned)
- Next steps / follow-ups

Do NOT invent facts.

Transcript:
{transcript}
"""
