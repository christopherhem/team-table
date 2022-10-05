from fastapi import APIRouter, Depends, Response
from fastapi.middleware.cors import CORSMiddleware
import os
from queries.table import EventQueries
from routers.models import (
    EventIn,
    EventOut,
    TableOut,
    UserVoOut,
    TeamVoOut
)

router = APIRouter()

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

@router.get("/api/table", response_model=TableOut)
def get_table(queries: EventQueries = Depends()):
    return {"events": queries.get_table()}
