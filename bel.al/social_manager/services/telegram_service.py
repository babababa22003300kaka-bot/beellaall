import httpx
from ..config import Config

class TelegramService:
    BASE_URL = "https://api.telegram.org/bot"
    
    def __init__(self):
        self.token = Config.TELEGRAM_BOT_TOKEN
        self.api_url = f"{self.BASE_URL}{self.token}"

    async def send_message(self, chat_id: str, text: str):
        """
        Sends a text message to a chat or channel.
        """
        url = f"{self.api_url}/sendMessage"
        data = {
            "chat_id": chat_id,
            "text": text
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=data)
            return response.json()
            
    async def set_webhook(self, webhook_url: str):
        """
        Sets the webhook URL for the bot.
        """
        url = f"{self.api_url}/setWebhook"
        data = {"url": webhook_url}
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=data)
            return response.json()
