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
        "VoiceOver": create_vo_agent()
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
    'VoiceOverScript'
]
