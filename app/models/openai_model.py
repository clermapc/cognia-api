from langchain.chat_models import ChatOpenAI
from app.config import OPENAI_API_KEY, DEFAULT_MODEL

def get_model():
    return ChatOpenAI(
        openai_api_key=OPENAI_API_KEY,
        model_name=DEFAULT_MODEL
    )