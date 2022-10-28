from fastapi import APIRouter, Depends, status, Response, HTTPException, Request
from models import ValidCoverUserListOut, ValidUserCoverListOut, ValidSwapListOut, EventVoIn
from typing import Union, List
from queries.swap_queries import SwapRepository
from .users_dependencies import get_current_user
import requests, json

router = APIRouter()


@router.get("/api/swaps/", response_model = ValidSwapListOut)
def get_valid_swaps(
    response:Response,
    request:Request,
    repo: SwapRepository = Depends(),
    user = Depends(get_current_user)
):
    return repo.get_valid_swaps(user)

@router.get("/api/usercovers/", response_model = ValidUserCoverListOut)
def get_valid_user_covers(
    response:Response,
    request:Request,
    repo: SwapRepository = Depends(),
    user = Depends(get_current_user)
):
    return repo.get_user_covers(user)

@router.get("/api/coveruser/", response_model = ValidCoverUserListOut)
def get_valid_covers_for_user(
    response:Response,
    request:Request,
    repo: SwapRepository = Depends(),
    user = Depends(get_current_user)
):
    return repo.get_valid_covers(user)

@router.get("/api/swapbyswap/{event_id}")
def get_valid_swaps_for_single_swap(
    response:Response,
    request:Request,
    repo:SwapRepository = Depends(),
    user = Depends(get_current_user),
    event_id = int
):
    return repo.get_swaps_for_single_swap(user, event_id)

@router.get("/api/swapbycover/")
def get_valid_swaps_for_single_cover(
    response: Response,
    request: Request,
    repo:SwapRepository=Depends(),
    user = Depends(get_current_user),
    user_cover = EventVoIn
):
    return repo.get_swaps_for_single_cover(user, user_cover)
