from pydantic import BaseModel
from typing import List
from .agent import Agent

class WaitlistPage(BaseModel):
    value_proposition: str
    benefits_list: List[str]
    signup_form_fields: List[str]

def create_waitlist_agent() -> Agent:
    return Agent(
        name="WaitlistCreator",
        instructions="Design compelling waitlist pages that explain product benefits.",
        output_type=WaitlistPage,
        model="gpt-4o-mini"
    )
