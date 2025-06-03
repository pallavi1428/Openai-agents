from pydantic import BaseModel
from typing import Optional
from ..agent import Agent

class DesignBrief(BaseModel):
    concept: str
    color_palette: List[str]
    style_references: List[str]
    dimensions: Optional[str] = None

def create_design_agent() -> Agent:
    return Agent(
        name="DesignGenius",
        instructions="Generate creative design concepts with color palettes and style references for various media.",
        output_type=DesignBrief,
        model="gpt-4o-mini"
    )
