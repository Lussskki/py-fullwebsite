import uvicorn
from fastapi import FastAPI
from methods import router
from database import db_connection
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    db_connection()
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
