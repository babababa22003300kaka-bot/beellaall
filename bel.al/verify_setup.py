import os
import sys
import asyncio

# Add current directory to path
sys.path.append(os.getcwd())

def check_file(path):
    if os.path.exists(path):
        print(f"[OK] Found {path}")
        return True
    else:
        print(f"[FAIL] Missing {path}")
        return False

async def test_ai():
    print("\nTesting AI Service Import...")
    try:
        from social_manager.services.ai_service import AIService, GeminiProvider
        service = AIService()
        print("[OK] AI Service Imported")
        # We won't call the API without a key, but we check the object
        if isinstance(service.provider, GeminiProvider):
            print("[OK] Default provider is Gemini")
    except ImportError as e:
        print(f"[FAIL] Import Error: {e}")
    except Exception as e:
        print(f"[FAIL] Error: {e}")

def verify():
    print("--- Verifying Project Setup ---\n")
    
    files = [
        "social_manager/main.py",
        "social_manager/config.py",
        "social_manager/services/ai_service.py",
        "social_manager/services/facebook_service.py",
        "social_manager/services/instagram_service.py",
        "social_manager/services/telegram_service.py",
        "social_manager/templates/index.html"
    ]
    
    all_exist = all(check_file(f) for f in files)
    
    if all_exist:
        print("\n[OK] All core files present.")
    else:
        print("\n[FAIL] Some files are missing.")
        
    asyncio.run(test_ai())

if __name__ == "__main__":
    verify()
