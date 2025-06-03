from pydantic import BaseModel
from typing import List, Dict
from .agent import Agent

class Dataset(BaseModel):
    fields: Dict[str, str]
    sample_data: List[Dict]
    description: str

def create_data_agent() -> Agent:
    return Agent(
        name="DataFactory",
        instructions="Generate realistic sample datasets with field definitions and example records.",
        output_type=Dataset,
        model="gpt-4o-mini"
    )
