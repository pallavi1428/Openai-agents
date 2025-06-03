from pydantic import BaseModel
from typing import List
from ..agent import Agent

class PersonalityAnalysis(BaseModel):
    traits: List[str]
    strengths: List[str]
    growth_areas: List[str]

def create_personality_agent() -> Agent:
    return Agent(
        name="PersonalityProfiler",
        instructions="Analyze personality traits and provide personalized development recommendations.",
        output_type=PersonalityAnalysis,
        model="gpt-4o-mini"
    )
