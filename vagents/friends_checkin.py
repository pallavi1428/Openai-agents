from pydantic import BaseModel
from .agent import Agent

class CheckinMessage(BaseModel):
    message: str
    tone: str

def create_checkin_agent() -> Agent:
    return Agent(
        name="MessageCraft",
        instructions="Write warm, personal check-in messages for friends and family.",
        output_type=CheckinMessage,
        model="gpt-4o-mini"
    )
