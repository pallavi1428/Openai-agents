from pydantic import BaseModel
from typing import List, Optional
from .agent import Agent

class Newsletter(BaseModel):
    title: str
    introduction: str
    featured_articles: List[str]
    industry_updates: List[str]
    subscriber_spotlight: Optional[str] = None
    call_to_action: str

def create_newsletter_agent() -> Agent:
    return Agent(
        name="NewsletterWriterPro",
        instructions="Create engaging newsletters for business professionals. Include industry updates, featured articles, and maintain a professional yet approachable tone.",
        output_type=Newsletter,
        model="gpt-4o-mini"
    )
