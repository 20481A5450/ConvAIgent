import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi import status
# app/main.py

app = FastAPI()
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Application startup!"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
