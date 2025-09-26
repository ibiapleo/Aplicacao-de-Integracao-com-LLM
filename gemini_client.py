import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("⚠️ GEMINI_API_KEY não encontrada no .env")

client = genai.Client(api_key=api_key)

def send_prompt(history: list[dict], prompt: str) -> str:
    full_prompt = ""
    for msg in history:
        if msg["role"] == "user":
            full_prompt += f"Usuário: {msg['content']}\n"
        else:
            full_prompt += f"Gemini: {msg['content']}\n"
    response = client.models.generate_content(
        model=os.getenv("GEMINI_MODEL"),
        contents=full_prompt
    )
    return response.text
