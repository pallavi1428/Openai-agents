from .agent import Agent
from .business import create_business_agent, BusinessIdea
from .blog import create_blog_agent, BlogPost
from .stock_analyst import create_stock_analyst_agent, StockAnalysis
from .newsletter import create_newsletter_agent, Newsletter
from .github_readme import create_readme_agent, Readme
from .book_writer import create_book_agent, BookOutline
from .therapist import create_therapist_agent, TherapySession
from .sleep_analyzer import create_sleep_agent, SleepAnalysis
from .health_assistant import create_health_agent, HealthReport
from .messages_writer import create_messages_agent, MessageCollection
from .email_writer import create_email_agent, Email
from .data_analyst import create_data_agent, DataReport
from .song_generator import create_song_agent, Song
from .book_summarizer import create_summary_agent, BookSummary
from .quick_learn import create_quicklearn_agent, QuickLesson
from .vo_assistant import create_vo_agent, VoiceOverScript

# NEW AGENTS
from .tweet_writer import create_tweet_agent, Tweet
from .thread_writer import create_thread_agent, Thread
from .travel_planner import create_travel_agent, TravelPlan
from .fitness_assistant import create_fitness_agent, WorkoutPlan
from .graphic_designer import create_design_agent, DesignBrief
from .report_generator import create_report_agent, Report
from .friends_checkin import create_checkin_agent, CheckinMessage
from .ocr_processor import create_ocr_agent, OCRResult
from .notes_tagger import create_tagger_agent, TaggedNote
from .web_researcher import create_web_research_agent, ResearchResult
from .deep_researcher import create_deep_research_agent, DeepResearch
from .llm_tester import create_tester_agent, TestResult
from .image_generator import create_image_agent, ImagePrompt
from .image_prompt_generator import create_prompt_agent, EnhancedPrompt

def create_agent(agent_type: str) -> Agent:
    agents = {
        "Business": create_business_agent(),
        "Blog": create_blog_agent(),
        "StockAnalyst": create_stock_analyst_agent(),
        "Newsletter": create_newsletter_agent(),
        "Readme": create_readme_agent(),
        "BookWriter": create_book_agent(),
        "Therapist": create_therapist_agent(),
        "SleepAnalyzer": create_sleep_agent(),
        "HealthAssistant": create_health_agent(),
        "MessageWriter": create_messages_agent(),
        "EmailWriter": create_email_agent(),
        "DataAnalyst": create_data_agent(),
        "SongWriter": create_song_agent(),
        "BookSummarizer": create_summary_agent(),
        "QuickLearn": create_quicklearn_agent(),
        "VoiceOver": create_vo_agent(),
        'Tweet': create_tweet_agent(),
        "Thread": create_thread_agent(),
        "TravelPlanner": create_travel_agent(),
        "FitnessAssistant": create_fitness_agent(),
        "GraphicDesigner": create_design_agent(),
        "ReportGenerator": create_report_agent(),
        "FriendsCheckin": create_checkin_agent(),
        "OcrProcessor": create_ocr_agent(),
        "NotesTagger": create_tagger_agent(),
        "WebResearcher": create_web_research_agent(),
        "DeepResearcher": create_deep_research_agent(),
        "LlmTester": create_tester_agent(),
        "ImageGenerator": create_image_agent(),
        "ImagePromptGenerator": create_prompt_agent(),

        
    }
    return agents.get(agent_type)

__all__ = [
    'Agent',
    'create_agent',
    'BusinessIdea',
    'BlogPost',
    'StockAnalysis',
    'Newsletter',
    'Readme',
    'BookOutline',
    'TherapySession',
    'SleepAnalysis',
    'HealthReport',
    'MessageCollection',
    'Email',
    'DataReport',
    'Song',
    'BookSummary',
    'QuickLesson',
    'VoiceOverScript',
    'Tweet',
    'Thread',
    'TravelPlan',
    'WorkoutPlan',
    'DesignBrief',
    'Report',
    'CheckinMessage',
    'OCRResult',
    'TaggedNote',
    'ResearchResult',
    'DeepResearch',
    'TestResult',
    'ImagePrompt',
    'EnhancedPrompt'
]
