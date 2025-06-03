from pydantic import BaseModel
from typing import List
from .agent import Agent

class EnhancedPrompt(BaseModel):
    original_prompt: str
    improved_prompt: str
    improvements: List[str]

def create_prompt_agent() -> Agent:
    return Agent(
        name="PromptOptimizer",
        instructions="Enhance image generation prompts with vivid descriptions and style details.",
        output_type=EnhancedPrompt,
        model="gpt-4o-mini"
    )
