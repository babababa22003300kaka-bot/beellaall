import httpx
from ..config import Config

class FacebookService:
    BASE_URL = "https://graph.facebook.com/v18.0"
    
    def __init__(self):
        self.access_token = Config.FB_PAGE_ACCESS_TOKEN
        self.page_id = None # Should be fetched or set in config

    async def post_to_page(self, message: str, page_id: str):
        """
        Publishes a text post to the Facebook Page.
        """
        url = f"{self.BASE_URL}/{page_id}/feed"
        params = {
            "message": message,
            "access_token": self.access_token
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(url, params=params)
            return response.json()

    async def reply_to_comment(self, comment_id: str, message: str):
        """
        Replies to a specific comment.
        """
        url = f"{self.BASE_URL}/{comment_id}/comments"
        params = {
            "message": message,
            "access_token": self.access_token
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(url, params=params)
            return response.json()
