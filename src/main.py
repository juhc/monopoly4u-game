from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from rooms.routes import router as rooms_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(rooms_router)

@app.get('/')
async def index():
    return {"data": "hello world!!!"}