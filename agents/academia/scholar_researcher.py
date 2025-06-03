from pydantic import BaseModel
from typing import List
from ..agent import Agent

class LiteratureReview(BaseModel):
    key_papers: List[str]
    research_gap: str
    citations: List[str]

def create_scholar_agent() -> Agent:
    return Agent(
        name="AcademicSleuth",
        instructions="Conduct academic literature reviews identifying key papers and research gaps in scholarly topics.",
        output_type=LiteratureReview,
        model="gpt-4o-mini"
    )
