from typing import AsyncGenerator
from vagents import Agent
import asyncio

class Runner:
    def __init__(self, client):
        self.client = client

    async def run(self, agent: Agent, input: str) -> AsyncGenerator[str, None]:
        try:
            # Create the stream
            stream = self.client.chat.completions.create(
                model=agent.model,
                messages=[
                    {"role": "system", "content": agent.instructions},
                    {"role": "user", "content": input}
                ],
                stream=True
            )
            
            # Convert sync stream to async iterator
            async def stream_to_async():
                for chunk in stream:
                    yield chunk
            
            # Process the stream
            full_response = ""
            async for chunk in stream_to_async():
                content = chunk.choices[0].delta.content or ""
                full_response += content
                yield full_response
                
        except Exception as e:
            raise Exception(f"AI generation failed: {str(e)}")