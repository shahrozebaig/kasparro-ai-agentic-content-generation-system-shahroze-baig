import requests
from config import settings

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

def llm_generate(prompt: str, max_tokens: int = 300, temperature: float = 0.3) -> str:
    if not settings.groq_api_key:
        raise RuntimeError("GROQ_API_KEY not set")
    headers = {
        "Authorization": f"Bearer {settings.groq_api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": settings.llm_model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": max_tokens,
        "temperature": temperature
    }
    response = requests.post(GROQ_URL, json=payload, headers=headers)
    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"].strip()
