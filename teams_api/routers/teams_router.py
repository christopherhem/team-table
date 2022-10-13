from fastapi import APIRouter, Depends, status, Response, HTTPException
from models import *
from typing import Union, List as l
from queries.teams_queries import TeamRepository

router = APIRouter()

@router.get("/api/teams", response_model = TeamsOut)
def get_teams(
    repo: TeamRepository = Depends()
):
    return {"teams": [repo.get_all()]}

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

@router.get("/api/teams/{id}/events")
def get_events():
    pass


# Lines 56-64 weas a test to make sure we wer able to access User, Delete when done. 
@router.post("/api/teams", response_model = Union[TeamOut,Error])
def add_team(
    team : TeamIn,
    response : Response,
    repo : TeamRepository = Depends()
    ):
    return repo.create(team)

@router.put("/api/teams/{id}/events/swap")
def event_swap(
):
    pass
