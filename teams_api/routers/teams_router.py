from fastapi import APIRouter, Depends, status, Response, HTTPException, Request
from models import TeamIn, TeamOut,Error
from typing import Union, List as l
from queries.teams_queries import TeamRepository
from .users_dependencies import get_current_user
import requests, json

router = APIRouter()

@router.get("/api/teams/", response_model = Union[TeamOut, l[TeamOut]])
def get_teams(
    repo: TeamRepository = Depends()
):
    return repo.get_all()

@router.get("/api/teams/{id}")
def get_team(id: int,
    response: Response,
    repo: TeamRepository = Depends(),
    ):
    record = repo.get_team(id)
    if record is None:
        response.status_code = 404
    else:
        return record

@router.delete("/api/teams/{id}", response_model = bool)
def delete_team(id: int,
repo: TeamRepository = Depends()):
    repo.delete_team(id)
    return True

@router.put("/api/teams/{id}", response_model = TeamOut)
def update_team(
    id: int,
    team_in: TeamIn,
    response: Response,
    repo: TeamRepository = Depends()
):
    record = repo.update_team(id, team_in)
    if record is None:
        response.status_code = 404
    else:
        return record

@router.post("/api/teams/", response_model = Union[TeamOut,Error])
def add_team(
    request:Request,
    team : TeamIn,
    response : Response,
    repo : TeamRepository = Depends(),
    user = Depends(get_current_user)
    ):
    record = repo.create(team)
    headers = request.headers
    data = json.dumps(record)
    requests.post("http://pubsub:8000/api/smps/", data = data, headers = headers)
    return record
