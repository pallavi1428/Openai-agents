from pydantic import BaseModel
from typing import List
from ..agent import Agent

class VideoScript(BaseModel):
    title: str
    scenes: List[str]
    duration_estimate: str

def create_video_agent() -> Agent:
    return Agent(
        name="VideoScriptor",
        instructions="Generate engaging video scripts with scene descriptions and timing estimates.",
        output_type=VideoScript,
        model="gpt-4o-mini"
    )
