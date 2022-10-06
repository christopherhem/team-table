from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from routers import table, users

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        os.environ.get("CORS_HOST", "http://localhost:3000")
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(table.router)
app.include_router(users.router)
