from pydantic import BaseModel
from typing import List, Optional
from .agent import Agent

class TherapySession(BaseModel):
    summary: str
    key_insights: List[str]
    coping_strategies: List[str]
    recommended_exercises: Optional[List[str]] = None
    follow_up_topics: Optional[List[str]] = None

def create_therapist_agent() -> Agent:
    return Agent(
        name="TherapeuticAssistant",
        instructions="Provide supportive, professional therapeutic responses. Focus on active listening and evidence-based coping strategies. Maintain strict confidentiality boundaries.",
        output_type=TherapySession,
        model="gpt-4o-mini"
    )
