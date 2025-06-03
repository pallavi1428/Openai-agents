from pydantic import BaseModel
from typing import List
from .agent import Agent

class EngineeredPrompt(BaseModel):
    task_description: str
    optimized_prompt: str
    variations: List[str]

def create_prompt_gen_agent() -> Agent:
    return Agent(
        name="PromptEngineer",
        instructions="Create and optimize prompts for various AI systems.",
        output_type=EngineeredPrompt,
        model="gpt-4o-mini"
    )
