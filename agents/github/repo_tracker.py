from pydantic import BaseModel
from typing import List
from ..agent import Agent

class RepoAnalysis(BaseModel):
    activity_summary: str
    recent_commits: List[str]
    issue_highlights: List[str]

def create_repo_agent() -> Agent:
    return Agent(
        name="CodeTracker",
        instructions="Analyze GitHub repositories, summarizing activity, recent commits, and important issues.",
        output_type=RepoAnalysis,
        model="gpt-4o-mini"
    )
