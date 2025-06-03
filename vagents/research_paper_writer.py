from pydantic import BaseModel
from typing import List
from .agent import Agent

class ResearchPaper(BaseModel):
    title: str
    abstract: str
    sections: List[str]
    references: List[str]

def create_paper_agent() -> Agent:
    return Agent(
        name="PaperComposer",
        instructions="Write academic research papers with proper structure and citations.",
        output_type=ResearchPaper,
        model="gpt-4o-mini"
    )
