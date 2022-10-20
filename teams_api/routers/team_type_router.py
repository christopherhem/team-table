from fastapi import APIRouter, Depends, Response
from models import (
    Error,
    TeamTypeIn,
    TeamTypeOut,
    )
from typing import Union, List
from queries.team_type_queries import TeamTypeRepository

router = APIRouter()

@router.get("/api/teams/types/", response_model = Union[Error, List[TeamTypeOut]])
def get_team_types(
    response: Response,
    repo: TeamTypeRepository = Depends()
):
    print('router called')
    record = repo.get_all()
    if record is None:
        response.status_code = 404
    else:
        return record

@router.get("/api/teams/types/{id}", response_model = Union[Error, TeamTypeOut])
def get_team_type(
    id: int,
    response: Response,
    repo: TeamTypeRepository = Depends()
):
    record = repo.get_team_type(id)
    if record is None:
        response.status_code = 404
    else:
        return record

@router.post("/api/teams/types/", response_model = Union[Error, TeamTypeOut])
def create_team_type(
    team_type: TeamTypeIn,
    event_types:List[int],
    response: Response,
    repo: TeamTypeRepository = Depends()
):
    record = repo.create(team_type,event_types)
    if record is None:
        response.status_code = 400
    else:
        return record

@router.put("/api/teams/types/{id}", response_model = Union[Error, TeamTypeOut])
def update_team_type(
    id: int,
    team_type: TeamTypeIn,
    response: Response,
    repo: TeamTypeRepository = Depends()
):
    record = repo.update_team_type(id, team_type)
    if record is None:
        response.status_code = 404
    else:
        return record

@router.delete("/api/teams/types/{id}", response_model = bool)
def delete_team_type(
    id: int,
    repo: TeamTypeRepository = Depends()
):
    record = repo.delete_team_type(id)
    if record is None:
        return False
    else:
        return record
