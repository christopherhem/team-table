from fastapi import APIRouter, Depends, Response, Request
from queries.swap_queries import SwapRepository
from typing import Union, List
from authenticator import authenticator
import requests, json
from models import ShiftSwapEventOut, CoverEventOut, Error
from datetime import datetime

router = APIRouter()


@router.post("/api/main/swap/", response_model=Union[Error, bool])
def swap_for_swap(
    request: Request,
    swaps: List[ShiftSwapEventOut],
    response: Response,
    user=Depends(authenticator.get_current_account_data),
    repo: SwapRepository = Depends(),
):
    for swap in swaps:
        if user["id"] == swap.user_id:
            result = repo.perform_swap(swaps)
            if result == True:
                headers = request.headers
                for swap in list(swaps):
                    temp = dict(swap)
                    for key in temp:
                        if type(temp[key]) == datetime:
                            temp[key] = str(temp[key])
                    data = json.dumps(temp)
                    requests.delete(
                        "http://pubsub:8000/api/seps/", data=data, headers=headers
                    )
                return True
            return False
    return {"message": "Current user id does not match id of either event"}


@router.post("/api/main/cover/", response_model=CoverEventOut)
def cover_for_swap(
    request: Request,
    cover: CoverEventOut,
    swap: ShiftSwapEventOut,
    response: Response,
    user=Depends(authenticator.get_current_account_data),
    repo: SwapRepository = Depends(),
):
    if user["id"] == cover.user_id or user["id"] == swap.user_id:
        result = repo.perform_cover(cover, swap)
        if result:
            headers = request.headers
            tempcover = dict(cover)
            for key in tempcover:
                if type(tempcover[key]) == datetime:
                    tempcover[key] = str(tempcover[key])
            tempswap = dict(swap)
            for key in tempswap:
                if type(tempswap[key]) == datetime:
                    tempswap[key] = str(tempswap[key])
            data1 = json.dumps(tempswap)
            data2 = json.dumps(tempcover)
            requests.delete("http://pubsub:8000/api/seps/", data=data1, headers=headers)
            requests.delete("http://pubsub:8000/api/seps/", data=data2, headers=headers)
            pushevent = {}
            for key in result:
                if type(result[key]) == datetime:
                    pushevent[key] = str(result[key])
                else:
                    pushevent[key] = result[key]
            data = json.dumps(pushevent)
            requests.post("http://pubsub:8000/api/seps/", data=data, headers=headers)
            return result
        return {"message": "Failed to carry out all or part of cover swap"}
    return {"message": "Current user id does not match id of either event"}
