from langchain.chat_models import ChatAnthropic
from app.config import ANTHROPIC_API_KEY

def get_model():
    return ChatAnthropic(
        anthropic_api_key=ANTHROPIC_API_KEY,
        model="claude-2"
    )