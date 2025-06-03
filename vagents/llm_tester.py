from pydantic import BaseModel
from typing import List
from .agent import Agent

class TestResult(BaseModel):
    test_cases: List[str]
    passed: List[bool]
    feedback: str

def create_tester_agent() -> Agent:
    return Agent(
        name="ModelValidator",
        instructions="Design and execute test cases for LLMs, evaluating performance.",
        output_type=TestResult,
        model="gpt-4o-mini"
    )
