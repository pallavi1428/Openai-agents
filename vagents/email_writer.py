from pydantic import BaseModel
from typing import List, Optional
from .agent import Agent

class Email(BaseModel):
    subject: str
    body: str
    tone: str
    key_points: List[str]
    call_to_action: Optional[str] = None

def create_email_agent() -> Agent:
    return Agent(
        name="EmailWriterPro",
        instructions="Compose professional emails tailored to specific purposes and recipients. Include clear structure and appropriate tone matching the context.",
        output_type=Email,
        model="gpt-4o-mini"
    )
