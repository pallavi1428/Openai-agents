from pydantic import BaseModel
from typing import List, Optional
from ..agent import Agent

class BusinessIdea(BaseModel):
    name: str
    target_audience: str
    revenue_model: str
    key_features: List[str]
    potential_challenges: Optional[List[str]] = None
    competitive_advantage: Optional[str] = None

def create_business_agent() -> Agent:
    return Agent(
        name="BusinessIdeaPro",
        instructions="Generate comprehensive business ideas with clear value propositions, target markets, and revenue models.",
        output_type=BusinessIdea,
        model="gpt-4o-mini"
    )
