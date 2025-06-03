from pydantic import BaseModel
from ..agent import Agent

class ImagePrompt(BaseModel):
    description: str
    style: str
    elements: List[str]

def create_image_agent() -> Agent:
    return Agent(
        name="ImageCreator",
        instructions="Generate detailed image generation prompts for DALL-E, Stable Diffusion, etc. with style specifications.",
        output_type=ImagePrompt,
        model="gpt-4o-mini"
    )
