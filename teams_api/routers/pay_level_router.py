from fastapi import APIRouter, Depends, Response
from models import PayLevelOut, Error
from typing import Union, List
from queries.pay_level_queries import PayLevelRepository

router = APIRouter()


@router.get("/api/teams/pay_levels/", response_model=Union[Error, List[PayLevelOut]])
def get_all(repo: PayLevelRepository = Depends()):
    return repo.get_all()


@router.get("/api/teams/pay_levels/{id}", response_model=PayLevelOut)
def get_pay_level(id: int, response: Response, repo: PayLevelRepository = Depends()):
    record = repo.get_pay_level(id)
    if record is None:
        response.status_code = 404
    else:
        return record
