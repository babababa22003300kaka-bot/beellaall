from fastapi import FastAPI, Request, BackgroundTasks, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

from .config import Config
from .services.facebook_service import FacebookService
from .services.instagram_service import InstagramService
from .services.telegram_service import TelegramService
from .services.ai_service import AIService

app = FastAPI(title="Social Media Manager")

# Initialize Services
fb_service = FacebookService()
ig_service = InstagramService()
tg_service = TelegramService()
ai_service = AIService()

# Setup Templates
templates = Jinja2Templates(directory="social_manager/templates")

class PostRequest(BaseModel):
    message: str
    platforms: List[str]

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/settings", response_class=HTMLResponse)
async def settings_page(request: Request):
    return templates.TemplateResponse("settings.html", {"request": request})

@app.get("/api/settings")
async def get_settings():
    # Return current config (masked for security in real apps, but here we show for editing)
    return {
        "FB_PAGE_ACCESS_TOKEN": Config.FB_PAGE_ACCESS_TOKEN,
        "FB_VERIFY_TOKEN": Config.FB_VERIFY_TOKEN,
        "IG_ACCOUNT_ID": Config.IG_ACCOUNT_ID,
        "TELEGRAM_BOT_TOKEN": Config.TELEGRAM_BOT_TOKEN,
        "TELEGRAM_CHAT_ID": Config.TELEGRAM_CHAT_ID,
        "GEMINI_API_KEY": Config.GEMINI_API_KEY,
    }

class SettingsModel(BaseModel):
    FB_PAGE_ACCESS_TOKEN: Optional[str] = ""
    FB_VERIFY_TOKEN: Optional[str] = ""
    IG_ACCOUNT_ID: Optional[str] = ""
    TELEGRAM_BOT_TOKEN: Optional[str] = ""
    TELEGRAM_CHAT_ID: Optional[str] = ""
    GEMINI_API_KEY: Optional[str] = ""

@app.post("/api/settings")
async def save_settings(settings: SettingsModel):
    env_content = ""
    # Read existing .env if exists to keep other vars? For now we just rewrite these keys
    # Simple approach: Append/Replace in .env file
    
    env_path = ".env"
    new_lines = []
    
    # Map of key -> value
    settings_dict = settings.dict()
    
    # Create .env content
    for key, value in settings_dict.items():
        if value:
            new_lines.append(f"{key}={value}")
            
    with open(env_path, "w", encoding="utf-8") as f:
        f.write("\n".join(new_lines))
        
    # Note: Config won't update automatically without reload, user needs to restart
    return {"status": "saved", "message": "Please restart server"}

@app.get("/api/status")
async def get_status():
    return {
        "facebook": bool(Config.FB_PAGE_ACCESS_TOKEN),
        "instagram": bool(Config.IG_ACCOUNT_ID),
        "telegram": bool(Config.TELEGRAM_BOT_TOKEN),
        "ai": bool(Config.GEMINI_API_KEY)
    }

@app.post("/publish")
async def publish_post(request: PostRequest):
    results = {}
    
    # Facebook
    if "facebook" in request.platforms:
        if not Config.FB_PAGE_ACCESS_TOKEN:
             results["facebook"] = "Error: Not Configured"
        else:
            try:
                # Note: In a real app, page_id should be dynamic or from config
                # For now, we assume it's set in the service or config
                res = await fb_service.post_to_page(request.message, page_id="me") 
                results["facebook"] = "Success"
            except Exception as e:
                results["facebook"] = f"Failed: {str(e)}"

    # Instagram (Requires Media for posts usually, but we'll assume text caption for now or handle logic)
    if "instagram" in request.platforms:
        if not Config.IG_ACCOUNT_ID:
            results["instagram"] = "Error: Not Configured"
        else:
            results["instagram"] = "Skipped (Instagram API requires image URL for posts)"

    # Telegram
    if "telegram" in request.platforms:
        if not Config.TELEGRAM_BOT_TOKEN:
            results["telegram"] = "Error: Not Configured"
        else:
            try:
                # Chat ID should be from config
                res = await tg_service.send_message(Config.TELEGRAM_CHAT_ID, request.message)
                results["telegram"] = "Success"
            except Exception as e:
                results["telegram"] = f"Failed: {str(e)}"
            
    return results

@app.get("/webhook")
async def verify_webhook(request: Request):
    """
    Verification endpoint for Facebook/Instagram Webhooks
    """
    params = request.query_params
    if params.get("hub.mode") == "subscribe" and params.get("hub.verify_token") == Config.FB_VERIFY_TOKEN:
        return int(params.get("hub.challenge"))
    return JSONResponse(content={"error": "Invalid token"}, status_code=403)

@app.post("/webhook")
async def handle_webhook(request: Request, background_tasks: BackgroundTasks):
    """
    Handle incoming events from Facebook/Instagram
    """
    data = await request.json()
    # Simple logic to detect messages and reply
    # In a real app, we need to parse the complex JSON structure of FB Webhooks
    
    # Example: Check for messaging event
    # This is a simplified placeholder logic
    print(f"Received Webhook: {data}")
    
    # Logic to trigger AI Reply would go here
    # background_tasks.add_task(process_ai_reply, data)
    
    return {"status": "ok"}

async def process_ai_reply(data):
    # Extract message text and sender ID
    # Generate reply using ai_service.get_reply()
    # Send reply using fb_service or ig_service
    pass

if __name__ == "__main__":
    uvicorn.run("social_manager.main:app", host=Config.HOST, port=Config.PORT, reload=True)
