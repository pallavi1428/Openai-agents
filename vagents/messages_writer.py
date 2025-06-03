from pydantic import BaseModel
from typing import List, Optional
from .agent import Agent

class MessageCollection(BaseModel):
    professional_messages: List[str]
    casual_messages: List[str]
    romantic_messages: Optional[List[str]] = None
    key_phrases: List[str]

def create_messages_agent() -> Agent:
    return Agent(
        name="MessageWriter",
        instructions="Generate appropriate messages for various contexts and relationships. Adapt tone based on recipient and communication purpose.",
        output_type=MessageCollection,
        model="gpt-4o-mini"
    )
