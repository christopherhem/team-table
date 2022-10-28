from fastapi import APIRouter, Depends, Response
from fastapi.middleware.cors import CORSMiddleware
import os
from queries.teamvo_queries import TeamVORepository
from models import TeamVoOut, TeamVoIn, MemberIn
from typing import List, Union
from authenticator import authenticator

router = APIRouter()


@router.get("/api/main/teams/", response_model=List[TeamVoOut])
def get_all(repo: TeamVORepository = Depends()):
    return repo.get_all()


@router.post("/api/main/teams/", response_model=TeamVoOut)
def new_team_vo(
    team: TeamVoIn,
    repo: TeamVORepository = Depends(),
    user=Depends(authenticator.get_current_account_data),
):
    return repo.create(team, user)


@router.get("/api/main/teams/{id}", response_model=TeamVoOut)
def get_by_id(id: int, response: Response, repo: TeamVORepository = Depends()):
    return repo.get_team(id)


@router.get("/api/main/teams/byuser/", response_model=List[TeamVoOut])
def get_by_user(
    user=Depends(authenticator.get_current_account_data),
    repo: TeamVORepository = Depends(),
):
    return repo.get_user_teams(user)


@router.post("/api/main/teams/members/")
def add_user_team_relation(
    member: MemberIn,
    user=Depends(authenticator.get_current_account_data),
    repo: TeamVORepository = Depends(),
):
    return repo.create_user_relation(member)
