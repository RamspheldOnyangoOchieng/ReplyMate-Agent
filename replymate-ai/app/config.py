import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = os.getenv("DEBUG", True)
    VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
    WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
    WHATSAPP_API_URL = os.getenv("WHATSAPP_API_URL")
    DATABASE_URL = os.getenv("DATABASE_URL")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    APP_URL = os.getenv("APP_URL")
