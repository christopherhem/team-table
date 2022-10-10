from fastapi import APIRouter, Depends, Response
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

@router.post("/api/teams", response_model = Union[TeamOut,Error])
def add_team(
    team : TeamIn,
    response : Response,
    repo : TeamRepository = Depends()
    ):
    response.status_code = 400
    return repo.create(team)

#this would probably be an internal call
@router.post("/api/teams/types")
def add_team_type():
    pass

@router.put("/api/teams/{id}/events/swap")
def event_swap():
    pass
