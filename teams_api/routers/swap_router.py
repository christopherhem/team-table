from fastapi import APIRouter, Depends, status, Response, HTTPException, Request
from models import ValidCoverUserListOut, ValidUserCoverListOut, ValidSwapListOut
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
    pass

@router.get("/api/usercovers/", response_model = ValidUserCoverListOut)
def get_valid_covers(
    response:Response,
    request:Request,
    repo: SwapRepository = Depends(),
    user = Depends(get_current_user)
):
    pass

@router.get("/api/coveruser/", response_model = ValidCoverUserListOut)
def get_valid_covers(
    response:Response,
    request:Request,
    repo: SwapRepository = Depends(),
    user = Depends(get_current_user)
):
    pass