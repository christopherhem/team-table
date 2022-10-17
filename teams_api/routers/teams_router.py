from fastapi import APIRouter, Depends, status, Response, HTTPException, Request
from models import *
import json, requests
from .users_dependencies import get_current_user
from typing import Union, List as l
from queries.teams_queries import TeamRepository

router = APIRouter()

@router.get("/api/teams", response_model = l[TeamOut])
def get_teams(
    repo: TeamRepository = Depends()
):
    return repo.get_all()

@router.get("/api/teams/{id}", response_model = TeamOut)
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

@router.get("/api/teams/{id}/events")
def get_events():
    pass


# Lines 56-64 weas a test to make sure we wer able to access User, Delete when done.
@router.post("/api/teams", response_model = TeamOut)
def add_team(
    request: Request,
    team : TeamIn,
    response : Response,
    repo : TeamRepository = Depends(),
    user = Depends(get_current_user)
    ):
    created_team = repo.create(team)
    print("created_team", created_team)
    headers = request.headers
    print("headers", headers)
    data = json.dumps(created_team)
    print("data", data)
    requests.post("http://pubsub:8000/api/smps", data = data, headers = headers)
    return created_team

@router.put("/api/teams/{id}/events/swap")
def event_swap(
):
    pass
