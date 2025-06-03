from pydantic import BaseModel
from typing import List, Optional
from ..agent import Agent

class Tweet(BaseModel):
    content: str
    hashtags: Optional[List[str]] = None
    character_count: int

def create_tweet_agent() -> Agent:
    return Agent(
        name="TweetCraft",
        instructions="Generate engaging tweets under 280 characters. Include relevant hashtags and maintain a conversational tone.",
        output_type=Tweet,
        model="gpt-4o-mini"
    )
