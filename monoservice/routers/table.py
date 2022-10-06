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


@router.get("/api/table", response_model=TableOut)
def get_table(queries: EventQueries = Depends()):
    return {"events": queries.get_table()}

@router.get("/api/table/{event_id}", response_model=EventOut)
def get_event(
    event_id: int,
    response: Response,
    queries: EventQueries = Depends(),
):
    record = queries.get_event(event_id)
    if record is None:
        response.status_code = 404
    else:
        return record

@router.post("/api/table", response_model=EventOut)
def create_event(
    event: EventIn,
    queries: EventQueries = Depends(),
):
    return queries.create_event(event)
