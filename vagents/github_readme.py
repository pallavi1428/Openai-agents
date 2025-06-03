from pydantic import BaseModel
from typing import List, Optional
from .agent import Agent

class Readme(BaseModel):
    project_title: str
    description: str
    features: List[str]
    installation: str
    usage: str
    contribution_guidelines: Optional[str] = None
    license_info: Optional[str] = None

def create_readme_agent() -> Agent:
    return Agent(
        name="ReadmeGenerator",
        instructions="Generate comprehensive GitHub README files with clear sections for documentation. Use markdown formatting and include all essential project information.",
        output_type=Readme,
        model="gpt-4o-mini"
    )
