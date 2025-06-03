from pydantic import BaseModel
from typing import Type

class Agent:
    def __init__(self, name: str, instructions: str, output_type: Type[BaseModel], model: str):
        self.name = name
        self.instructions = instructions
        self.output_type = output_type
        self.model = model