from pydantic import BaseModel
from typing import List, Optional
from .agent import Agent

class StockAnalysis(BaseModel):
    ticker: str
    summary: str
    key_events: List[str]
    technical_analysis: str
    fundamental_analysis: str
    price_target: Optional[float] = None
    risk_factors: Optional[List[str]] = None

def create_stock_analyst_agent() -> Agent:
    return Agent(
        name="StockNewsAnalyst",
        instructions="Analyze stock news and provide comprehensive reports including technical and fundamental analysis. Identify key events affecting the stock and provide objective analysis suitable for investors.",
        output_type=StockAnalysis,
        model="gpt-4o-mini"
    )
