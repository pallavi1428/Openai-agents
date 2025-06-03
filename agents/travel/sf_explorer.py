from pydantic import BaseModel
from typing import List
from ..agent import Agent

class TravelPlan(BaseModel):
    itinerary: List[str]
    recommended_spots: List[str]
    travel_tips: List[str]

def create_travel_agent() -> Agent:
    return Agent(
        name="SFExplorer",
        instructions="Create detailed San Francisco travel plans including itineraries, must-see locations, and local tips.",
        output_type=TravelPlan,
        model="gpt-4o-mini"
    )
