from pydantic import BaseModel
from ..agent import Agent

class Transcription(BaseModel):
    text: str
    confidence: float
    speaker_notes: List[str]

def create_transcription_agent() -> Agent:
    return Agent(
        name="AudioTranscriber",
        instructions="Transcribe audio content accurately, identifying different speakers and noting uncertainties.",
        output_type=Transcription,
        model="gpt-4o-mini"
    )
