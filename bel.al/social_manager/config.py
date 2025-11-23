import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Facebook & Instagram
    FB_PAGE_ACCESS_TOKEN = os.getenv("FB_PAGE_ACCESS_TOKEN")
    FB_VERIFY_TOKEN = os.getenv("FB_VERIFY_TOKEN")
    IG_ACCOUNT_ID = os.getenv("IG_ACCOUNT_ID")
    
    # Telegram
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID") # For testing or admin notifications
    
    # AI
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    
    # App
    PORT = int(os.getenv("PORT", 8000))
    HOST = os.getenv("HOST", "0.0.0.0")
