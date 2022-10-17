from fastapi import APIRouter, Depends, Response
from fastapi.middleware.cors import CORSMiddleware
import os
from queries.teamvo_queries import TeamVORepository
from routers.models import (
    TeamVoOut,
    TeamVoIn
)

router = APIRouter()

@router.get("/api/table/teams", response_model=TeamVoOut)
def get_all(repo: TeamVORepository = Depends()):
    return repo.get_all()

@router.post("/api/main/teams", response_model = TeamVoOut)
def new_team_vo(team:TeamVoIn, repo:TeamVORepository = Depends()):
    return repo.create(team)

@router.get("/api/table/teams/{id}", response_model=TeamVoOut)
def get_team(
    id: int,
    response: Response,
    repo: TeamVORepository = Depends()
):
    record = repo.get_team(id)
    if record is None:
        response.status_code = 404
    else:
        return record
