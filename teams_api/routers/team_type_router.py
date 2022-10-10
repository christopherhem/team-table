from fastapi import APIRouter, Depends, Response
from models import (
    Error,
    TeamTypeIn,
    TeamTypeOut,
    )
from typing import Union, List as l
from queries.team_type_queries import TeamTypeRepository

router = APIRouter()

@router.get("/api/teams/team_types", response_model = Union[Error, l[TeamTypeOut]])
def get_team_types(
    repo: TeamTypeRepository = Depends()
):
    return {"team_types": repo.get_all()}

@router.get("/api/teams/team_types/{id}", response_model = Union[Error, TeamTypeOut])
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

@router.post("/api/teams/team_types", response_model = Union[Error, TeamTypeOut])
def create_team_type(
    team_type: TeamTypeIn,
    response: Response,
    repo: TeamTypeRepository = Depends()
):
    record = repo.create(team_type)
    if record in None:
        response.status_code = 400
    else:
        return record

@router.put("/api/teams/team_types/{id}", response_model = Union[Error, TeamTypeOut])
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

@router.delete("/api/teams/team_types/{id}", response_model = bool)
def delete_team_type(
    id: int,
    repo: TeamTypeRepository = Depends()
):
    record = repo.delete_team_type(id)
    if record is None:
        return False
    else:
        return record
