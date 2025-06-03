from pydantic import BaseModel
from typing import List
from .agent import Agent

class GiftRecommendations(BaseModel):
    ideas: List[str]
    price_ranges: List[str]
    personalization_tips: List[str]

def create_gift_agent() -> Agent:
    return Agent(
        name="GiftGenius",
        instructions="Generate personalized gift ideas based on recipient interests and budgets.",
        output_type=GiftRecommendations,
        model="gpt-4o-mini"
    )
