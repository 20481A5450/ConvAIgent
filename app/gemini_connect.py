from fastapi import APIRouter, HTTPException
from fastapi import status
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def list_gemini_models():
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            return {"error": "GEMINI_API_KEY not found in environment variables."}
        genai.configure(api_key=api_key)
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

