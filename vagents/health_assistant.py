from pydantic import BaseModel
from typing import List, Optional
from .agent import Agent

class HealthReport(BaseModel):
    current_status: str
    nutrition_advice: List[str]
    exercise_recommendations: List[str]
    wellness_tips: List[str]
    warning_signs: Optional[List[str]] = None

def create_health_agent() -> Agent:
    return Agent(
        name="HealthAssistant",
        instructions="Provide general health and wellness advice based on user input. Focus on evidence-based recommendations and always suggest consulting a doctor for medical issues.",
        output_type=HealthReport,
        model="gpt-4o-mini"
    )
