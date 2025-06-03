from pydantic import BaseModel
from typing import List
from ..agent import Agent

class Report(BaseModel):
    title: str
    executive_summary: str
    sections: List[str]
    conclusions: str

def create_report_agent() -> Agent:
    return Agent(
        name="ReportMaster",
        instructions="Generate professional reports with clear structure, data analysis, and actionable conclusions.",
        output_type=Report,
        model="gpt-4o-mini"
    )
