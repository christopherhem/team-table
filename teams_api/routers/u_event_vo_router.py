"""
if data['shift_start']:
    repo = shiftswaprepo
else:
    repo = coverrepo
"""
from .users_dependencies import get_current_user

from fastapi import APIRouter, Depends, Response
from models import EventVoIn, EventVoOut
from typing import Union, List as l
from queries.u_event_vo_queries import SwapEventVoRepository, CoverEventVoRepository

router = APIRouter()

@router.post("/api/teams/events")
def new_event_vo(
    event:EventVoIn,
    response:Response,
    repo,
    user = Depends(get_current_user)
):
    #not sure if this logic will work, we may need to ask a better way to do this, or just make two seperate
    if event['shift_start']:
        repo: SwapEventVoRepository = Depends()
    else:
        repo: CoverEventVoRepository = Depends()
    repo.create(event,user)