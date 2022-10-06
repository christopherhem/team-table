from fastapi import APIRouter, Depends, Response
from models import PayLevelOut, PayLevelsOut
from typing import Union, List as l
from queries.pay_level_queries import PayLevelRepository

router = APIRouter()

@router.get("/api/teams/pay_levels/", response_model = PayLevelsOut)
def get_all(repo: PayLevelRepository = Depends()):
    return {"pay_levels": [repo.get_all()]}

@router.get("/api/teams/pay_levels/{id}", response_model = PayLevelOut)
def get_pay_level(
    id: int,
    response: Response,
    repo: PayLevelRepository = Depends()
):
    record = repo.get_pay_level(id)
    if record is None:
        response.status_code = 404
    else:
        return record
