import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi import status

from app.gemini_connect import list_gemini_models
# app/main.py

app = FastAPI()
# app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Application startup!"}

@app.get("/models")
async def get_models():
    try:
        models = list_gemini_models()
        return {"models": models}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
