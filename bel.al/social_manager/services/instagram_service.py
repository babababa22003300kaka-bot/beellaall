import httpx
from ..config import Config

class InstagramService:
    BASE_URL = "https://graph.facebook.com/v18.0"
    
    def __init__(self):
        self.access_token = Config.FB_PAGE_ACCESS_TOKEN
        self.account_id = Config.IG_ACCOUNT_ID

    async def create_media_object(self, image_url: str, caption: str):
        """
        Step 1: Create a media container.
        """
        url = f"{self.BASE_URL}/{self.account_id}/media"
        params = {
            "image_url": image_url,
            "caption": caption,
            "access_token": self.access_token
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(url, params=params)
            return response.json()

    async def publish_media(self, creation_id: str):
        """
        Step 2: Publish the media container.
        """
        url = f"{self.BASE_URL}/{self.account_id}/media_publish"
        params = {
            "creation_id": creation_id,
            "access_token": self.access_token
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(url, params=params)
            return response.json()

    async def reply_to_comment(self, comment_id: str, message: str):
        """
        Replies to an Instagram comment.
        """
        url = f"{self.BASE_URL}/{comment_id}/replies"
        params = {
            "message": message,
            "access_token": self.access_token
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(url, params=params)
            return response.json()
