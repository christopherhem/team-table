"""
if data['shift_start']:
    repo = shiftswaprepo
else:
    repo = coverrepo
"""
from .users_dependencies import get_current_user

from fastapi import APIRouter, Depends, Response
from models import EventVoIn, EventsOut
from queries.u_event_vo_queries import EventVoRepository

router = APIRouter()


@router.post("/api/teams/events/")
def new_event_vo(
    event: EventVoIn,
    response: Response,
    repo: EventVoRepository = Depends(),
    user=Depends(get_current_user),
):
    if not event.user_id or event.user_id == None:
        validated_id = user["account"]["id"]
    else:
        validated_id = event.user_id
    if not event.shift_start or event.shift_start == None:
        record = repo.create_cover_event(event, validated_id)
    else:
        record = repo.create_swap_event(event, validated_id)
    if record is None:
        response.status_code = 404
    else:
        return record


@router.delete("/api/teams/events/")
def delete_event_vo(
    event: EventVoIn,
    response: Response,
    repo: EventVoRepository = Depends(),
    user=Depends(get_current_user),
):
    if not event.shift_start or event.shift_start == None:
        record = repo.delete_cover_event(event)
    else:
        record = repo.delete_swap_event(event)
    if record is None:
        response.status_code = 404
    else:
        return record


@router.get("/api/teams/{id}/events/", response_model=EventsOut)
def get_events_by_team(
    id: int,
    response: Response,
    user=Depends(get_current_user),
    repo: EventVoRepository = Depends(),
):
    return repo.get_events(id)
