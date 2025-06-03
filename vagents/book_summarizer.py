from pydantic import BaseModel
from typing import List, Optional
from .agent import Agent

class BookSummary(BaseModel):
    title: str
    author: str
    key_ideas: List[str]
    chapter_summaries: List[str]
    main_arguments: List[str]
    practical_applications: Optional[List[str]] = None

def create_summary_agent() -> Agent:
    return Agent(
        name="BookSummarizer",
        instructions="Create comprehensive book summaries capturing key ideas and arguments. Maintain original meaning while condensing content.",
        output_type=BookSummary,
        model="gpt-4o-mini"
    )
