from pydantic import BaseModel
from typing import List
from .agent import Agent

class Advice(BaseModel):
    situation: str
    advice_points: List[str]
    communication_tips: List[str]

def create_love_coach_agent() -> Agent:
    return Agent(
        name="RelationshipGuide",
        instructions="Provide thoughtful relationship advice with communication strategies.",
        output_type=Advice,
        model="gpt-4o-mini"
    )
