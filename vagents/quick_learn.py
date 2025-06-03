from pydantic import BaseModel
from typing import List, Optional
from .agent import Agent

class QuickLesson(BaseModel):
    topic: str
    key_concepts: List[str]
    analogies: List[str]
    practical_examples: List[str]
    common_misconceptions: Optional[List[str]] = None

def create_quicklearn_agent() -> Agent:
    return Agent(
        name="QuickLearn",
        instructions="Break down complex topics into 20-minute learning modules. Focus on key concepts with clear explanations and practical examples.",
        output_type=QuickLesson,
        model="gpt-4o-mini"
    )
