from pydantic import BaseModel
from typing import List, Optional
from .agent import Agent

class BookOutline(BaseModel):
    title: str
    chapters: List[str]
    character_descriptions: Optional[List[str]] = None
    plot_summary: str
    target_audience: str
    genre: str

def create_book_agent() -> Agent:
    return Agent(
        name="BookWriterPro",
        instructions="Develop complete book outlines including chapters, characters, and plot. Adapt style to specified genre and target audience.",
        output_type=BookOutline,
        model="gpt-4o-mini"
    )
