from pydantic import BaseModel
from typing import List
from .agent import Agent

class Thread(BaseModel):
    tweets: List[str]
    overall_theme: str

def create_thread_agent() -> Agent:
    return Agent(
        name="ThreadWeaver",
        instructions="Create coherent Twitter threads with 3-10 connected tweets that maintain logical flow.",
        output_type=Thread,
        model="gpt-4o-mini"
    )
