from fastapi import APIRouter, HTTPException
from fastapi import status
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise {"error": "GEMINI_API_KEY not found in environment variables."}
genai.configure(api_key=api_key)

def list_gemini_models():
    try:
        models = genai.list_models()
        model_list = []
        for m in models:
            model_list.append({
                "name": m.name,
                "display_name": getattr(m, "display_name", "N/A"),
                "generation_methods": getattr(m, "supported_generation_methods", "N/A")
            })
        return {"models": model_list}
    except Exception as e:
        return {"error": str(e)}

async def generate_text(prompt: str) -> str:
    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")
        if not prompt:
            raise ValueError("Prompt cannot be empty.")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
