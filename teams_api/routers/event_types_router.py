from fastapi import APIRouter, Depends, Response
from models import (
    Error,
    EventTypeIn,
    EventTypeOut,
    )
from typing import Union, List as l
from queries.event_type_queries import EventTypeRepository

router = APIRouter()

@router.get("/api/teams/event_types/", response_model = Union[Error, l[EventTypeOut]])
def get_event_types(
    repo: EventTypeRepository = Depends()
):
    return repo.get_all()

@router.get("/api/teams/event_types/{id}", response_model = Union[Error, EventTypeOut])
def get_event_type(
    id: int,
    response: Response,
    repo: EventTypeRepository = Depends()
):
    record = repo.get_event_type(id)
    if record is None:
        response.status_code = 404
    else:
        return record
