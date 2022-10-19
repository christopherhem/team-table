"""
if data['shift_start']:
    repo = shiftswaprepo
else:
    repo = coverrepo
"""
from .users_dependencies import get_current_user

from fastapi import APIRouter, Depends, Response
from models import EventVoIn, SwapEventVoOut,CoverEventVoOut
from typing import Union, List as l
from queries.u_event_vo_queries import EventVoRepository

router = APIRouter()

@router.post("/api/teams/events/")
def new_event_vo(
    event:EventVoIn,
    response:Response,
    repo: EventVoRepository = Depends(),
    user = Depends(get_current_user)
):
    if event.shift_start:
        record = repo.create_swap_event(event,user)
    else:
        record = repo.create_cover_event(event,user)
    if record is None:
        response.status_code = 404
    else:
        return record