from pydantic import BaseModel
from typing import List
from ..agent import Agent

class MemeRecommendation(BaseModel):
    template: str
    caption_options: List[str]
    context: str

def create_meme_agent() -> Agent:
    return Agent(
        name="MemeCurator",
        instructions="Recommend appropriate meme templates and captions based on current trends and contexts.",
        output_type=MemeRecommendation,
        model="gpt-4o-mini"
    )
