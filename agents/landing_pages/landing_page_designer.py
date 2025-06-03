from pydantic import BaseModel
from typing import List
from ..agent import Agent

class LandingPage(BaseModel):
    headline: str
    value_propositions: List[str]
    call_to_action: str
    design_notes: List[str]

def create_landing_page_agent() -> Agent:
    return Agent(
        name="PageArchitect",
        instructions="Design effective landing pages with compelling copy, value propositions, and clear CTAs.",
        output_type=LandingPage,
        model="gpt-4o-mini"
    )
