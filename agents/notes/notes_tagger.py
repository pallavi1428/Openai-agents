from pydantic import BaseModel
from typing import List
from ..agent import Agent

class TaggedNote(BaseModel):
    content: str
    tags: List[str]
    summary: str

def create_tagger_agent() -> Agent:
    return Agent(
        name="NoteOrganizer",
        instructions="Analyze notes, extract key tags, and generate summaries for better organization and retrieval.",
        output_type=TaggedNote,
        model="gpt-4o-mini"
    )
