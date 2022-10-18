from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from routers import events_router, team_vo_router, users_router
from authenticator import authenticator

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

app.include_router(events_router.router)
app.include_router(users_router.router)
app.include_router(team_vo_router.router)
app.include_router(authenticator.router)
