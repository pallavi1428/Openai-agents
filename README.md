
```markdown
# AI Agent Chat Interface

A scalable Gradio interface for multiple AI agents with streaming responses.

## 🎥 Live Demo

[![Watch the demo](https://img.youtube.com/vi/GagLu0mnoiU/0.jpg)](https://youtu.be/GagLu0mnoiU)

## Features

- 🚀 **Multi-agent support** (Business, Blog, Songwriter, etc.)
- 💬 **Real-time streaming** responses
- 📂 **Save conversations** in TXT/JSON
- 🛠️ **Easy to extend** with new agents

## Quick Start

1. **Install dependencies**:
   ```bash
   pip install openai python-dotenv gradio
   ```

2. **Set up environment**:
   - Create `.env` file:
     ```ini
     OPENAI_API_KEY=your_openai_key_here
     ```

3. **Run the app**:
   ```bash
   python -m app.main
   ```

4. **Access the UI** at `http://localhost:7860`

## Adding New Agents

1. Create a new file in `vagents/` (e.g., `legal.py`):
   ```python
   from pydantic import BaseModel
   from .agent import Agent

   class LegalDoc(BaseModel):
       summary: str
       clauses: list[str]

   def create_legal_agent() -> Agent:
       return Agent(
           name="LegalAssistant",
           instructions="Generate legal documents...",
           output_type=LegalDoc,
           model="gpt-4o-mini"
       )
   ```

2. Add to `AGENT_MAP` in `vagents/__init__.py`:
   ```python
   from .legal import create_legal_agent

   AGENT_MAP = {
       # ... existing agents
       "Legal": create_legal_agent
   }
   ```

## Project Structure

```
.
├── app/
│   ├── main.py           # Gradio interface
│   └── runner.py         # Streaming logic
├── vagents/
│   ├── __init__.py       # Agent registry
│   ├── agent.py          # Base Agent class
│   ├── business.py       # Business agent
│   └── ...               # Other agents
└── .env                  # API keys
```

## License

MIT © 2023
```
