from pydantic import BaseModel
from typing import List
from .agent import Agent

class EmailSummary(BaseModel):
    key_points: List[str]
    action_items: List[str]
    sentiment: str

def create_email_agent() -> Agent:
    return Agent(
        name="InboxAnalyst",
        instructions="Summarize emails by extracting key points and action items.",
        output_type=EmailSummary,
        model="gpt-4o-mini"
    )
