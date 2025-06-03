from pydantic import BaseModel
from typing import List
from .agent import Agent

class Greeting(BaseModel):
    message: str
    tone: str
    length: str

def create_greeting_agent() -> Agent:
    return Agent(
        name="GreetingCraft",
        instructions="Write appropriate greetings for cards, emails, and messages.",
        output_type=Greeting,
        model="gpt-4o-mini"
    )
