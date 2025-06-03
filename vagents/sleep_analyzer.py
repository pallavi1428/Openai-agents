from pydantic import BaseModel
from typing import List, Optional
from .agent import Agent

class SleepAnalysis(BaseModel):
    sleep_quality: str
    duration_analysis: str
    improvement_recommendations: List[str]
    potential_disruptions: Optional[List[str]] = None
    ideal_sleep_window: Optional[str] = None

def create_sleep_agent() -> Agent:
    return Agent(
        name="SleepAnalyzer",
        instructions="Analyze sleep patterns and provide personalized recommendations. Use sleep science principles and suggest practical improvements.",
        output_type=SleepAnalysis,
        model="gpt-4o-mini"
    )
