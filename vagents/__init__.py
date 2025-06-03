from .agent import Agent
from .business import create_business_agent, BusinessIdea
from .blog import create_blog_agent, BlogPost

def create_agent(agent_type: str) -> Agent:
    agents = {
        "Business": create_business_agent(),
        "Blog": create_blog_agent()
    }
    return agents.get(agent_type)

__all__ = ['Agent', 'create_agent', 'BusinessIdea', 'BlogPost']