from app.core.settings import settings 

from langchain_openai import ChatOpenAI

def get_model() -> ChatOpenAI:
    return ChatOpenAI(
        model="openai/gpt-6-luna",
        api_key=settings.openrouter_api_key,
        base_url="https://openrouter.ai/api/v1",
    )