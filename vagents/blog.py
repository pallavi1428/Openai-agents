from pydantic import BaseModel
from typing import List, Optional
from .agent import Agent

class BlogPost(BaseModel):
    title: str
    introduction: str
    sections: List[str]
    conclusion: str
    seo_keywords: Optional[List[str]] = None
    estimated_reading_time: Optional[str] = None

def create_blog_agent() -> Agent:
    return Agent(
        name="BlogWriterPro",
        instructions="Write professional blog posts...",
        output_type=BlogPost,
        model="gpt-4o-mini"
    )