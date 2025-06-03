from pydantic import BaseModel
from typing import List, Optional
from .agent import Agent

class VoiceOverScript(BaseModel):
    title: str
    script: List[str]
    tone_guidance: str
    pacing_notes: str
    emphasis_points: Optional[List[str]] = None

def create_vo_agent() -> Agent:
    return Agent(
        name="VoiceOverAssistant",
        instructions="Generate professional voice-over scripts with tone guidance and pacing notes. Adapt style to specified purpose (commercial, narrative, etc.).",
        output_type=VoiceOverScript,
        model="gpt-4o-mini"
    )
