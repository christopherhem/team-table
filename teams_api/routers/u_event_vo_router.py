"""
if data['shift_start']:
    repo = shiftswaprepo
else:
    repo = coverrepo
"""

from fastapi import APIRouter, Depends, Response
from models import *
from typing import Union, List as l
from queries.u_event_vo_queries import SwapEventVoRepository, CoverEventVoRepository

router = APIRouter()

@router.post("/api/teams/events"):
def new_event_vo(
    event:EventVoIn,
    response:Response,
    repo
):
    if event['shift_start']:
        repo: SwapEventVoRepository = Depends()
    else:
        repo: CoverEventVoRepository = Depends()
    repo.create(event)