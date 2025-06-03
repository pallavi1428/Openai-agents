from pydantic import BaseModel
from typing import List
from .agent import Agent

class ImagePrompt(BaseModel):
    description: str
    style: str
    elements: List[str]

def create_image_agent() -> Agent:
    return Agent(
        name="ImageCreator",
        instructions="Generate detailed image generation prompts with style specifications.",
        output_type=ImagePrompt,
        model="gpt-4o-mini"
    )
