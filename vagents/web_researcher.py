from pydantic import BaseModel
from typing import List
from .agent import Agent

class ResearchResult(BaseModel):
    sources: List[str]
    key_findings: List[str]
    credibility_score: float

def create_web_research_agent() -> Agent:
    return Agent(
        name="WebSleuth",
        instructions="Conduct web research, summarize findings, and evaluate source credibility.",
        output_type=ResearchResult,
        model="gpt-4o-mini"
    )
