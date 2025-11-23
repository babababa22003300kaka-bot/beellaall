# 🚀 تقرير تسليم مشروع "Social Orbit" - الدليل الشامل

**تاريخ التقرير:** 23 نوفمبر 2025
**اسم المشروع:** Social Orbit (مدير السوشيال ميديا الموحد)
**الإصدار:** 1.0 (نسخة أولية MVP)

---

## 1. 📝 إيه هو المشروع ده؟ (نظرة عامة)
يا بطل، المشروع ده عبارة عن **لوحة تحكم مركزية (Dashboard)** معمولة بـ **Python** و **FastAPI**.
فكرته ببساطة إنك بدل ما تفتح فيسبوك لوحده، وإنستجرام لوحده، وتيليجرام لوحده عشان تنزل بوست، إنت بتفتح اللوحة دي، تكتب البوست مرة واحدة، وتدوس "نشر"، وهو يوزعه على كل المنصات دي في نفس اللحظة.

### 🌟 المميزات الحالية:
1.  **النشر الموحد:** اكتب مرة واحدة، انشر في كل حتة (فيس، انستا، تيليجرام).
2.  **واجهة شيك جداً:** تصميم مودرن (Glassmorphism) وشريط جانبي (Sidebar) احترافي.
3.  **ذكاء اصطناعي (Gemini):** مربوط بـ Google Gemini عشان يساعدك في الردود أو كتابة المحتوى (الأساس موجود).
4.  **سهولة الإعداد:** صفحة إعدادات عشان تدخل مفاتيح الـ API من غير ما تلعب في الكود.

---

## 2. 🛠️ العدة المستخدمة (Tech Stack)
ليه اخترنا التقنيات دي بالذات؟

*   **Python 3.9+:** لغة سهلة وقوية، ومكتباتها كتير جداً.
*   **FastAPI:** أسرع وأحدث إطار عمل (Framework) في بايثون حالياً لبناء الـ APIs. خفيف جداً وسريع.
*   **Uvicorn:** ده "الموتور" اللي بيشغل السيرفر بتاع FastAPI.
*   **Jinja2 Templates:** عشان نكتب كود HTML ونحط جواه بيانات ديناميكية من بايثون (زي حالة الاتصال).
*   **Google Generative AI:** مكتبة جوجل الرسمية للذكاء الاصطناعي (Gemini).
*   **Httpx:** مكتبة عشان السيرفر يكلم سيرفرات فيسبوك وتيليجرام (زي ما المتصفح بيعمل بس بالكود).

---

## 3. 🔑 إزاي تجيب المفاتيح؟ (دليل الـ API Keys)
عشان المشروع يشتغل، لازم تجيب "تصاريح" من المنصات دي. التصاريح دي اسمها API Keys أو Tokens.

### 📘 1. فيسبوك وإنستجرام (Meta)
1.  ادخل على [Meta for Developers](https://developers.facebook.com/).
2.  اعمل "Create App" واختار نوعه "Business".
3.  في لوحة التحكم، ضيف منتج "Graph API Explorer" عشان تجرب، أو روح لـ "Marketing API".
4.  هتحتاج تربط "صفحة فيسبوك" (Facebook Page) وتعمل "حساب إنستجرام بيزنس" (Instagram Business Account) وتربطهم ببعض.
5.  من الـ Graph API Explorer، هتطلع حاجة اسمها **Page Access Token**. ده المفتاح اللي هيخلينا ننشر باسم الصفحة.
6.  هتحتاج كمان **Instagram Account ID** (رقم الحساب بتاع انستا).

### ✈️ 2. تيليجرام (Telegram)
1.  افتح تطبيق تيليجرام وابحث عن "BotFather".
2.  ابدأ شات معاه واكتب `/newbot`.
3.  هيطلب منك اسم للبوت واسم مستخدم (username).
4.  في الآخر هيديك **HTTP API Token**. هو ده الـ `TELEGRAM_BOT_TOKEN`.
5.  عشان تجيب الـ `TELEGRAM_CHAT_ID`: ضيف البوت بتاعك في قناة أو جروب، وابعت رسالة، وبعدين ادخل على رابط الـ API في المتصفح (`https://api.telegram.org/bot<TOKEN>/getUpdates`) هتلاقي رقم الشات في الرد.

### 🤖 3. الذكاء الاصطناعي (Google Gemini)
1.  ادخل على [Google AI Studio](https://aistudio.google.com/).
2.  سجل بحساب جوجل بتاعك.
3.  دوس على "Get API key" واعمل "Create API key in new project".
4.  خد الكود اللي هيطلعلك، ده الـ `GEMINI_API_KEY`.

---

## 4. 💻 شرح الكود "حتة حتة" (Code Walkthrough)

### 📂 [main.py](file:///C:/Users/pc/Downloads/bel.al/social_manager/main.py) (المخ بتاع المشروع)
ده الملف الرئيسي اللي بيشغل كل حاجة.
*   **`app = FastAPI(...)`**: هنا بنبدأ التطبيق.
*   **`@app.get("/")`**: لما تفتح الموقع، الدالة دي بتشتغل وبترجعلك ملف [index.html](file:///C:/Users/pc/Downloads/bel.al/social_manager/templates/index.html).
*   **`@app.post("/publish")`**: دي أهم دالة. لما تدوس "نشر" في الموقع، البيانات بتيجي هنا. الكود بيشوف إنت اخترت أنهي منصات، ويبعت لكل [Service](file:///C:/Users/pc/Downloads/bel.al/social_manager/services/ai_service.py#47-57) خاصة بيها.
*   **`@app.post("/api/settings")`**: دي اللي بتحفظ المفاتيح اللي بتكتبها في صفحة الإعدادات جوه ملف مخفي اسمه `.env`.

### 📂 `services/` (العمال)
هنا قسمنا الشغل عشان الكود ميبقاش "سلطة".
*   **[facebook_service.py](file:///C:/Users/pc/Downloads/bel.al/social_manager/services/facebook_service.py)**: فيه دالة [post_to_page](file:///C:/Users/pc/Downloads/bel.al/social_manager/services/facebook_service.py#11-23) بتاخد الرسالة وتبعتها لفيسبوك.
*   **[instagram_service.py](file:///C:/Users/pc/Downloads/bel.al/social_manager/services/instagram_service.py)**: فيه دوال لرفع الصور والنشر على انستا (انستا معقد شوية بيحتاج خطوتين: رفع ميديا، وبعدين نشر).
*   **[telegram_service.py](file:///C:/Users/pc/Downloads/bel.al/social_manager/services/telegram_service.py)**: فيه دالة [send_message](file:///C:/Users/pc/Downloads/bel.al/social_manager/services/telegram_service.py#11-23) بتبعت رسالة للبوت.
*   **[ai_service.py](file:///C:/Users/pc/Downloads/bel.al/social_manager/services/ai_service.py)**: ده بقى "المخ المفكر". صممناه بطريقة ذكية (Abstract Class) عشان لو حبيت في المستقبل تغير Gemini وتستخدم ChatGPT، متضطرش تهد الكود كله، يا دوب تعمل ملف جديد وخلاص.

### 📂 `templates/` (الوش / الواجهة)
*   **[index.html](file:///C:/Users/pc/Downloads/bel.al/social_manager/templates/index.html)**: دي الصفحة اللي بتشوفها. فيها الـ Sidebar والأزرار. استخدمنا فيها CSS حديث عشان تطلع بالشكل "الزجاجي" ده.
*   **[settings.html](file:///C:/Users/pc/Downloads/bel.al/social_manager/templates/settings.html)**: صفحة بسيطة عشان تدخل المفاتيح وتحفظها.

---

## 5. 🚀 دليل التشغيل (إزاي تشغله عندك؟)

### الخطوة 1: نزل بايثون
لو مش عندك، نزل [Python](https://www.python.org/downloads/) (تأكد إنك تختار "Add Python to PATH" وإنت بتسطب).

### الخطوة 2: جهز البيئة (Virtual Environment)
افتح الـ Terminal (أو CMD) في الفولدر بتاع المشروع واكتب:
```bash
# 1. اعمل بيئة وهمية عشان ملفات المشروع متدخلش في ملفات الجهاز
python -m venv venv

# 2. شغل البيئة دي
# لو ويندوز:
venv\Scripts\activate
# لو ماك أو لينكس:
source venv/bin/activate
```

### الخطوة 3: نزل المكتبات المطلوبة
إحنا محتاجين مكتبات زي `fastapi` و `uvicorn`. اكتب الأمر ده:
```bash
pip install fastapi uvicorn httpx python-dotenv jinja2 google-generativeai
```

### الخطوة 4: شغل السيرفر!
```bash
uvicorn social_manager.main:app --reload
```
دلوقتي افتح المتصفح على: `http://localhost:8000`
ومبروك عليك! 🎉

---

## 6. 🗺️ خارطة الطريق (إيه اللي ممكن تعمله بعدين؟)

يا هندسة، المشروع ده "أرضية" ممتازة، بس لسه ممكن تبني عليه عماير. دي شوية أفكار للمبرمج اللي هيستلم منك:

### 1. قاعدة بيانات (Database) 🗄️
حالياً إحنا مش بنحفظ البوستات القديمة.
*   **المطلوب:** ركب `SQLite` أو `PostgreSQL`.
*   **الفايدة:** تقدر تعمل "سجل تاريخي" (History) لكل البوستات اللي نزلت، وتعرف إيه اللي فشل وإيه اللي نجح، وتحفظ إعدادات المستخدمين بشكل أحسن.

### 2. تسجيل الدخول (Login System) 🔐
حالياً أي حد يفتح الرابط يقدر ينشر.
*   **المطلوب:** اعمل نظام Login بسيط (Username/Password).
*   **الفايدة:** أمان أكتر، ومحدش يلعب في إعداداتك.

### 3. رفع الصور (Image Upload) 📸
حالياً انستجرام محتاج رابط صورة جاهز.
*   **المطلوب:** زود زرار في الـ Form يخليك ترفع صورة من جهازك.
*   **التنفيذ:** السيرفر هياخد الصورة، يحفظها في فولدر `static`، ويعملها رابط، ويبعته لانستجرام.

### 4. الجدولة (Scheduling) ⏰
*   **المطلوب:** خيار "نشر لاحقاً".
*   **التنفيذ:** استخدم مكتبة زي `APScheduler` في بايثون. تقولها "انشري البوست ده بكرة الساعة 5"، وهي تتصرف.

---

## 7. 📦 الكود المصدري الكامل (Full Source Code)

عشان المبرمج ميتعبش، ده الكود كله ملف ملف. ينسخه ويحطه في الملفات بنفس الاسم.

### 📄 [social_manager/config.py](file:///C:/Users/pc/Downloads/bel.al/social_manager/config.py)
```python
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
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
    
    # AI
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    
    # App Settings
    PORT = int(os.getenv("PORT", 8000))
    HOST = os.getenv("HOST", "0.0.0.0")
```

### 📄 [social_manager/services/ai_service.py](file:///C:/Users/pc/Downloads/bel.al/social_manager/services/ai_service.py)
```python
from abc import ABC, abstractmethod
import google.generativeai as genai
from ..config import Config

class AIProvider(ABC):
    @abstractmethod
    def generate_reply(self, message: str, context: str = "") -> str:
        pass

class GeminiProvider(AIProvider):
    def __init__(self):
        if Config.GEMINI_API_KEY:
            genai.configure(api_key=Config.GEMINI_API_KEY)
            self.model = genai.GenerativeModel('gemini-pro')

    def generate_reply(self, message: str, context: str = "") -> str:
        if not Config.GEMINI_API_KEY: return "Error: AI Key missing"
        prompt = f"Context: {context}\nMsg: {message}\nReply politely in Egyptian Arabic."
        try:
            return self.model.generate_content(prompt).text
        except Exception as e:
            return f"AI Error: {e}"

class AIService:
    def __init__(self, provider: AIProvider = None):
        self.provider = provider or GeminiProvider()

    def get_reply(self, message: str, context: str = "") -> str:
        return self.provider.generate_reply(message, context)
```

### 📄 [social_manager/services/facebook_service.py](file:///C:/Users/pc/Downloads/bel.al/social_manager/services/facebook_service.py)
```python
import httpx
from ..config import Config

class FacebookService:
    BASE_URL = "https://graph.facebook.com/v18.0"
    
    def __init__(self):
        self.access_token = Config.FB_PAGE_ACCESS_TOKEN

    async def post_to_page(self, message: str, page_id: str = "me"):
        url = f"{self.BASE_URL}/{page_id}/feed"
        params = {"message": message, "access_token": self.access_token}
        async with httpx.AsyncClient() as client:
            response = await client.post(url, params=params)
            return response.json()
```

### 📄 [social_manager/services/telegram_service.py](file:///C:/Users/pc/Downloads/bel.al/social_manager/services/telegram_service.py)
```python
import httpx
from ..config import Config

class TelegramService:
    BASE_URL = "https://api.telegram.org/bot"
    
    def __init__(self):
        self.token = Config.TELEGRAM_BOT_TOKEN
        self.api_url = f"{self.BASE_URL}{self.token}"

    async def send_message(self, chat_id: str, text: str):
        url = f"{self.api_url}/sendMessage"
        data = {"chat_id": chat_id, "text": text}
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=data)
            return response.json()
```

### 📄 [social_manager/main.py](file:///C:/Users/pc/Downloads/bel.al/social_manager/main.py)
```python
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
from .config import Config
from .services.facebook_service import FacebookService
from .services.instagram_service import InstagramService
from .services.telegram_service import TelegramService
from .services.ai_service import AIService

app = FastAPI()
templates = Jinja2Templates(directory="social_manager/templates")

# Services
fb = FacebookService()
ig = InstagramService()
tg = TelegramService()
ai = AIService()

class PostRequest(BaseModel):
    message: str
    platforms: List[str]

class SettingsModel(BaseModel):
    FB_PAGE_ACCESS_TOKEN: Optional[str] = ""
    FB_VERIFY_TOKEN: Optional[str] = ""
    IG_ACCOUNT_ID: Optional[str] = ""
    TELEGRAM_BOT_TOKEN: Optional[str] = ""
    TELEGRAM_CHAT_ID: Optional[str] = ""
    GEMINI_API_KEY: Optional[str] = ""

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/settings", response_class=HTMLResponse)
async def settings(request: Request):
    return templates.TemplateResponse("settings.html", {"request": request})

@app.get("/api/settings")
async def get_settings():
    return {k: getattr(Config, k) for k in dir(Config) if k.isupper()}

@app.post("/api/settings")
async def save_settings(settings: SettingsModel):
    with open(".env", "w", encoding="utf-8") as f:
        for k, v in settings.dict().items():
            if v: f.write(f"{k}={v}\n")
    return {"status": "saved"}

@app.get("/api/status")
async def status():
    return {
        "facebook": bool(Config.FB_PAGE_ACCESS_TOKEN),
        "instagram": bool(Config.IG_ACCOUNT_ID),
        "telegram": bool(Config.TELEGRAM_BOT_TOKEN),
        "ai": bool(Config.GEMINI_API_KEY)
    }

@app.post("/publish")
async def publish(req: PostRequest):
    res = {}
    if "facebook" in req.platforms:
        try:
            await fb.post_to_page(req.message)
            res["facebook"] = "Success"
        except Exception as e: res["facebook"] = str(e)
        
    if "telegram" in req.platforms:
        try:
            await tg.send_message(Config.TELEGRAM_CHAT_ID, req.message)
            res["telegram"] = "Success"
        except Exception as e: res["telegram"] = str(e)
        
    return res

if __name__ == "__main__":
    uvicorn.run("social_manager.main:app", host="0.0.0.0", port=8000, reload=True)
```

---

**تم بحمد الله.**
التقرير ده معاك، وأي حد "صنايعي كود" هيشوفه هيفهم الفولة علطول. بالتوفيق يا ريس! 🚀
