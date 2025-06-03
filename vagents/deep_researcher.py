from pydantic import BaseModel
from typing import List
from .agent import Agent

class DeepResearch(BaseModel):
    hypothesis: str
    methodology: str
    findings: List[str]
    conclusions: str

def create_deep_research_agent() -> Agent:
    return Agent(
        name="ResearchAnalyst",
        instructions="Conduct in-depth research with clear methodology and evidence-based conclusions.",
        output_type=DeepResearch,
        model="gpt-4o-mini"
    )
