from pydantic import BaseModel
from typing import List, Optional
from .agent import Agent

class WorkoutPlan(BaseModel):
    exercises: List[str]
    duration: str
    difficulty: str
    equipment_needed: Optional[List[str]] = None

def create_fitness_agent() -> Agent:
    return Agent(
        name="FitCoach",
        instructions="Generate personalized workout plans based on user goals and available equipment.",
        output_type=WorkoutPlan,
        model="gpt-4o-mini"
    )
