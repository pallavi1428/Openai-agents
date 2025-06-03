import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

# Adds root folder to Python path # Absolute import
import os
from dotenv import load_dotenv
import gradio as gr
from vagents.business import BusinessIdea
from vagents.blog import BlogPost
from vagents.stock_analyst import StockAnalysis
from vagents.newsletter import Newsletter
from vagents.github_readme import Readme
from vagents.book_writer import BookOutline
from vagents.therapist import TherapySession
from vagents.sleep_analyzer import SleepAnalysis
from vagents.health_assistant import HealthReport
from vagents.messages_writer import MessageCollection
from vagents.email_writer import Email
from vagents.data_analyst import DataReport
from vagents.song_generator import Song
from vagents.book_summarizer import BookSummary
from vagents.quick_learn import QuickLesson
from vagents.vo_assistant import VoiceOverScript


from vagents.tweet_writer import Tweet
from vagents.thread_writer import Thread
from vagents.travel_planner import TravelPlan
from vagents.fitness_assistant import WorkoutPlan
from vagents.graphic_designer import DesignBrief
from vagents.report_generator import Report
from vagents.friends_checkin import CheckinMessage
from vagents.ocr_processor import OCRResult
from vagents.notes_tagger import TaggedNote
from vagents.web_researcher import ResearchResult
from vagents.deep_researcher import DeepResearch
from vagents.llm_tester import TestResult
from vagents.image_generator import ImagePrompt
from vagents.image_prompt_generator import EnhancedPrompt


from vagents import Agent
from app.runner import Runner
from openai import OpenAI
#from app.utils import load_environment
from typing import Optional, AsyncGenerator, List
from vagents import create_agent
from pathlib import Path
import asyncio
from datetime import datetime
import json
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_environment():
    """Load environment variables from .env file"""
    env_path = Path(__file__).parent.parent / ".env"
    load_dotenv(env_path)
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set")
    return api_key

# Initialize OpenAI client
try:
    client = OpenAI(api_key=load_environment())
    runner = Runner(client)  # Initialize runner with OpenAI client
except Exception as e:
    logger.error(f"Failed to initialize OpenAI client: {e}")
    raise

async def stream_response(agent_choice: str, user_input: str) -> AsyncGenerator[str, None]:
    agent = create_agent(agent_choice)
    if not agent:
        yield "Error: Invalid agent choice"
        return
    
    try:
        async for response in runner.run(agent, user_input):
            yield response
            
    except Exception as e:
        logger.error(f"Error during generation: {e}")
        yield f"Error: {str(e)}"

# Save conversation to file
def save_conversation(history: list, format: str = "txt") -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"conversation_{timestamp}.{format}"
    
    try:
        if format == "txt":
            with open(filename, "w") as f:
                for entry in history:
                    if entry[0]:  # User message
                        f.write(f"You: {entry[0]}\n")
                    if entry[1]:  # Agent response
                        f.write(f"Agent: {entry[1]}\n")
                    f.write("\n")
        elif format == "json":
            with open(filename, "w") as f:
                json.dump(history, f, indent=2)
        else:
            return None
            
        return filename
    except Exception as e:
        logger.error(f"Error saving conversation: {e}")
        return None


def create_interface() -> gr.Blocks:
    """Create the Gradio interface"""
    with gr.Blocks(
        theme=gr.themes.Soft(primary_hue="emerald"),
        title="AI Agent Chat",
        css="""
        .loading {
            animation: pulse 1.5s infinite;
        }
        @keyframes pulse {
            0% { opacity: 1; }
            50% { opacity: 0.5; }
            100% { opacity: 1; }
        }
        """
    ) as app:
        chat_history = gr.State([])
        current_agent = gr.State("Business")

        with gr.Row():
            # Sidebar
            with gr.Column(scale=1, min_width=250):
                agent_selector = gr.Dropdown(
                    choices=["Business", "Blog", "StockAnalyst",
                            "Newsletter",
                            "Readme",
                            "BookWriter",
                            "Therapist",
                            "SleepAnalyzer",
                            "HealthAssistant",
                            "MessageWriter",
                            "EmailWriter",
                            "DataAnalyst",
                            "SongWriter",
                            "BookSummarizer",
                            "QuickLearn",
                            "VoiceOver",
                            "TweetWriter",
                            "ThreadWriter",
                            "TravelPlanner",
                            "FitnessAssistant",
                            "GraphicDesigner",
                            "ReportGenerator",
                            "FriendsCheckin",
                            "OCRProcessor",
                            "NotesTagger",
                            "WebResearcher",
                            "DeepResearcher",
                            "LLMTester",
                            "ImageGenerator",
                            "ImagePromptGenerator"
                        ], 
                    label="Select Agent Type",
                    value="Business"
                )

                gr.Markdown("### Business Examples")
                business_examples = gr.Dataset(
                    components=[gr.Textbox(visible=False)],
                    samples=[
                        ["Sustainable fashion tech for Gen Z"],
                        ["AI-powered local service marketplace"],
                        ["Subscription box for pet owners"]
                    ],
                    label="Business Ideas"
                )

                gr.Markdown("### Blog Examples")
                blog_examples = gr.Dataset(
                    components=[gr.Textbox(visible=False)],
                    samples=[
                        ["How AI is transforming healthcare"],
                        ["Beginner's guide to sustainable investing"],
                        ["Top productivity tools for remote teams"]
                    ],
                    label="Blog Ideas"
                )

            # Main Chat Interface
            with gr.Column(scale=4):
                chatbot = gr.Chatbot(
                    height=500,
                    bubble_full_width=True,
                    show_copy_button=True
                )
                
                loading_indicator = gr.HTML(
                    "<div class='loading' style='text-align: center; display: none;'>"
                    "⏳ Generating response...</div>"
                )

                with gr.Row():
                    msg = gr.Textbox(
                        show_label=False,
                        placeholder="Type your message here...",
                        scale=8
                    )
                    submit_btn = gr.Button("Send", variant="primary", scale=1)
                    stop_btn = gr.Button("Stop", variant="stop", scale=1)
                    clear_btn = gr.Button("Clear", scale=1)
                    save_btn = gr.Button("💾 Save", scale=1)

                # Save options
                with gr.Row(visible=False) as save_options:
                    with gr.Column():
                        save_format = gr.Radio(
                            ["txt", "json"],
                            label="Save Format",
                            value="txt"
                        )
                        save_status = gr.HTML()
                        save_download = gr.File(interactive=False, visible=False)

        # Event Logic
        def select_agent(agent_name: str, history: list):
            greeting = f"Hello! I'm your {agent_name} Expert. How can I help?"
            return (history + [(None, greeting)]) if not history else history, agent_name

        async def respond(agent_name: str, message: str, history: list):
            if not message.strip():
                raise gr.Error("Please enter a message")

            history.append((message, None))
            yield {
                chatbot: history,
                loading_indicator: gr.update(visible=True),
                submit_btn: gr.update(interactive=False)
            }

            full_response = ""
            async for chunk in stream_response(agent_name, message):
                full_response = chunk
                history[-1] = (message, full_response)
                yield {
                    chatbot: history,
                    loading_indicator: gr.update(visible=True)
                }

            yield {
                chatbot: history,
                loading_indicator: gr.update(visible=False),
                submit_btn: gr.update(interactive=True)
            }

        def clear_chat():
            return [], "Business"

        def toggle_save_options():
            return gr.update(visible=True)

        def handle_save(history, format):
            if not history:
                return {
                    save_status: "<div style='color: red'>No conversation to save!</div>",
                    save_download: gr.update(visible=False)
                }
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"conversation_{timestamp}.{format}"
            
            try:
                if format == "txt":
                    with open(filename, "w") as f:
                        for entry in history:
                            if entry[0]:  # User message
                                f.write(f"You: {entry[0]}\n")
                            if entry[1]:  # Agent response
                                f.write(f"Agent: {entry[1]}\n")
                            f.write("\n")
                elif format == "json":
                    with open(filename, "w") as f:
                        json.dump(history, f, indent=2)
                else:
                    return None
                    
                return {
                    save_status: "<div style='color: green'>Conversation saved!</div>",
                    save_download: gr.update(value=filename, visible=True)
                }
            except Exception as e:
                logger.error(f"Error saving conversation: {e}")
                return {
                    save_status: "<div style='color: red'>Error saving conversation</div>",
                    save_download: gr.update(visible=False)
                }

        # Component Connections
        agent_selector.change(
            select_agent,
            [agent_selector, chat_history],
            [chatbot, current_agent]
        )

        submit_event = msg.submit(
            respond,
            [current_agent, msg, chat_history],
            [chatbot, loading_indicator, submit_btn],
            api_name="chat"
        ).then(lambda: "", None, msg)

        btn_click = submit_btn.click(
            respond,
            [current_agent, msg, chat_history],
            [chatbot, loading_indicator, submit_btn]
        ).then(lambda: "", None, msg)

        stop_btn.click(
            None,
            None,
            None,
            cancels=[submit_event, btn_click]
        )

        clear_btn.click(
            clear_chat,
            None,
            [chat_history, current_agent]
        ).then(lambda: None, None, chatbot)

        save_btn.click(
            toggle_save_options,
            None,
            [save_options]
        )

        save_format.change(
            handle_save,
            [chat_history, save_format],
            [save_status, save_download]
        )

        # Load example on click
        def load_example(example):
            return example[0]

        business_examples.click(load_example, [business_examples], [msg])
        blog_examples.click(load_example, [blog_examples], [msg])

    return app

if __name__ == "__main__":
    app = create_interface()
    app.launch(server_name="0.0.0.0", server_port=7860, share=True)