from fastapi import APIRouter, Depends, Response, Request
from typing import List, Union
import requests, json
from queries.events_queries import EventQueries
from authenticator import authenticator
from models import (
    UserCoverEventOut,
    UserShiftSwapEventOut,
    CoverEventIn,
    CoverEventUpdateIn,
    CoverEventOut,
    ShiftSwapEventOut,
    ShiftSwapEventIn,
    ShiftSwapEventUpdateIn,
    EventTypeOut,
)
from datetime import datetime

router = APIRouter()


@router.get(
    "/api/table/cover_events/", response_model=Union[CoverEventOut, List[CoverEventOut]]
)
def get_cover_event_table(queries: EventQueries = Depends()):
    return queries.get_cover_event_table()


@router.get(
    "/api/table/shift_swap_events/",
    response_model=Union[CoverEventOut, List[ShiftSwapEventOut]],
)
def get_shift_swap_event_table(queries: EventQueries = Depends()):
    return queries.get_shift_swap_event_table()


@router.get(
    "/api/table/user/cover_events/",
    response_model=Union[UserCoverEventOut, List[UserCoverEventOut]],
)
def get_user_cover_events(
    user=Depends(authenticator.get_current_account_data),
    queries: EventQueries = Depends(),
):
    return queries.get_user_cover_events(user)


@router.get(
    "/api/table/user/shift_swap_events/",
    response_model=Union[UserShiftSwapEventOut, List[UserShiftSwapEventOut]],
)
def get_user_shift_swap_events(
    user=Depends(authenticator.get_current_account_data),
    queries: EventQueries = Depends(),
):
    return queries.get_user_shift_swap_events(user)


@router.get("/api/table/cover_events/{id}", response_model=CoverEventOut)
def get_cover_event(
    id: int,
    response: Response,
    queries: EventQueries = Depends(),
):
    record = queries.get_cover_event(id)
    if record is None:
        response.status_code = 404
    else:
        return record


@router.get("/api/table/shift_swap_events/{id}", response_model=ShiftSwapEventOut)
def get_shift_swap_event(
    id: int,
    response: Response,
    queries: EventQueries = Depends(),
):
    record = queries.get_shift_swap_event(id)
    if record is None:
        response.status_code = 404
    else:
        return record


@router.post("/api/table/cover_events/", response_model=CoverEventOut)
def create_cover_event(
    request: Request,
    event: CoverEventIn,
    queries: EventQueries = Depends(),
    user=Depends(authenticator.get_current_account_data),
):
    headers = request.headers
    pushevent = {}
    created_event = queries.create_cover_event(event, user)
    for key in created_event:
        if type(created_event[key]) == datetime:
            pushevent[key] = str(created_event[key])
        else:
            pushevent[key] = created_event[key]
    data = json.dumps(pushevent)
    requests.post("http://pubsub:8000/api/seps/", data=data, headers=headers)
    return created_event


@router.post("/api/table/shift_swap_events/", response_model=ShiftSwapEventOut)
def create_shift_swap_event(
    request: Request,
    event: ShiftSwapEventIn,
    queries: EventQueries = Depends(),
    user=Depends(authenticator.get_current_account_data),
):
    headers = request.headers
    pushevent = {}
    created_event = queries.create_shift_swap_event(event, user)
    for key in created_event:
        if type(created_event[key]) == datetime:
            pushevent[key] = str(created_event[key])
        else:
            pushevent[key] = created_event[key]
    data = json.dumps(pushevent)
    requests.post("http://pubsub:8000/api/seps/", data=data, headers=headers)
    return created_event


@router.put("/api/table/cover_events/{id}", response_model=CoverEventOut)
def update_cover_event(
    id: int,
    event: CoverEventUpdateIn,
    response: Response,
    repo: EventQueries = Depends(),
):
    record = repo.update_cover_event(id, event)
    if record is None:
        response.status_code = 404
    else:
        return record


@router.put("/api/table/shift_swap_events/{id}", response_model=ShiftSwapEventOut)
def update_shift_swap_event(
    id: int,
    event: ShiftSwapEventUpdateIn,
    response: Response,
    repo: EventQueries = Depends(),
):
    record = repo.update_shift_swap_event(id, event)
    if record is None:
        response.status_code = 404
    else:
        return record


@router.delete("/api/table/cover_events/{id}", response_model=bool)

def delete_cover_event(
    id: int,
    repo: EventQueries = Depends()
):
    repo.delete_cover_event(id)
    return True


@router.delete("/api/table/shift_swap_events/{id}", response_model=bool)
def delete_cover_event(id: int, repo: EventQueries = Depends()):
    record = repo.delete_shift_swap_event(id)
def delete_cover_event(
    id: int,
    repo: EventQueries = Depends()
):
    repo.delete_shift_swap_event(id)
    return True


@router.get("/api/table/event_types", response_model=List[EventTypeOut])
def get_event_types(repo: EventQueries = Depends()):
    return repo.get_event_types()


@router.get("/api/table/event_types/{id}", response_model=EventTypeOut)
def get_event_type(
    id: int,
    response: Response,
    repo: EventQueries = Depends(),
):
    record = repo.get_event_type(id)
    if record is None:
        response.status_code = 404
    else:
        return record
