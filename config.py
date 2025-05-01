import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
    DATABASE_URL = os.getenv("DATABASE_URL")
    VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
