import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from methods import router
from database import db_connection
from dotenv import load_dotenv
from fastapi.responses import FileResponse  
import os

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/", response_class=HTMLResponse)
async def serve_index():
    with open(os.path.join("frontend", "index.html"), "r") as f:
        index_html = f.read()
    return HTMLResponse(content=index_html, status_code=200)

@app.get("/style.css")
async def serve_css():
    return FileResponse("frontend/style.css", media_type="text/css")

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
