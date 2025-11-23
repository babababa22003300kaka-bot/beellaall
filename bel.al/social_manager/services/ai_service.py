from abc import ABC, abstractmethod
import google.generativeai as genai
from ..config import Config

class AIProvider(ABC):
    """
    Abstract Base Class for AI Providers.
    All new providers (OpenAI, Claude, etc.) must inherit from this.
    """
    @abstractmethod
    def generate_reply(self, message: str, context: str = "") -> str:
        pass

class GeminiProvider(AIProvider):
    """
    Implementation for Google Gemini API.
    """
    def __init__(self):
        if not Config.GEMINI_API_KEY:
            print("WARNING: GEMINI_API_KEY is not set.")
        else:
            genai.configure(api_key=Config.GEMINI_API_KEY)
            self.model = genai.GenerativeModel('gemini-pro')

    def generate_reply(self, message: str, context: str = "") -> str:
        if not Config.GEMINI_API_KEY:
            return "Error: AI API Key is missing."
        
        prompt = f"""
        You are a helpful social media assistant.
        Context: {context}
        User Message: {message}
        
        Please generate a polite, engaging, and relevant reply in the same language as the message (mostly Arabic/Egyptian).
        Keep it concise and friendly.
        """
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating reply: {str(e)}"

# Future Providers can be added here:
# class OpenAIProvider(AIProvider): ...
# class ClaudeProvider(AIProvider): ...

class AIService:
    """
    Service to manage AI interactions.
    Currently uses GeminiProvider by default.
    """
    def __init__(self, provider: AIProvider = None):
        self.provider = provider or GeminiProvider()

    def get_reply(self, message: str, context: str = "") -> str:
        return self.provider.generate_reply(message, context)
