from pydantic import BaseModel
from typing import List, Optional
from .agent import Agent

class Song(BaseModel):
    title: str
    lyrics: List[str]
    genre: str
    mood: str
    song_structure: List[str]
    themes: Optional[List[str]] = None

def create_song_agent() -> Agent:
    return Agent(
        name="SongWriter",
        instructions="Create original song lyrics with specified style, mood, and structure. Include verses, chorus, and bridge sections as appropriate.",
        output_type=Song,
        model="gpt-4o-mini"
    )
