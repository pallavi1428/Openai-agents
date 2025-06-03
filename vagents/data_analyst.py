from pydantic import BaseModel
from typing import List, Optional
from .agent import Agent

class DataReport(BaseModel):
    insights: List[str]
    visualizations_suggested: List[str]
    trends_identified: List[str]
    recommendations: List[str]
    limitations: Optional[List[str]] = None

def create_data_agent() -> Agent:
    return Agent(
        name="DataAnalyst",
        instructions="Analyze provided datasets and generate meaningful insights. Suggest appropriate visualizations and identify key trends.",
        output_type=DataReport,
        model="gpt-4o-mini"
    )
