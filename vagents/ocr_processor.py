from pydantic import BaseModel
from .agent import Agent

class OCRResult(BaseModel):
    extracted_text: str
    confidence_score: float
    file_type: str

def create_ocr_agent() -> Agent:
    return Agent(
        name="OCRExpert",
        instructions="Process images and PDFs to extract text with accuracy estimates.",
        output_type=OCRResult,
        model="gpt-4o-mini"
    )
