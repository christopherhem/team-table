from fastapi import APIRouter
from models import *
from queries.teams_queries import TeamRepository

router = APIRouter()

@router.get("/api/teams")
def get_teams():
    pass

@router.get("/api/teams/INT:PK")
def get_team():
    pass

@router.get("/api/teams/INT:PK/roles")
def get_roles():
    pass

@router.get("/api/teams/INT:PK/members")
def get_members():
    pass

@router.get("/api/teams/INT:PK/events")
def get_events():
    pass

@router.post("/api/teams", response_model = TeamOut)
def add_team(
    team : TeamIn, 
    repo : TeamRepository = Depends()
    ):
    return repo.create(team)

@router.post("/api/teams/INT:PK/roles")
def add_role():
    pass

@router.post("/api/teams/INT:PK/members")
def add_member():
    pass

#this would probably be an internal call
@router.post("/api/teams/types")
def add_team_type():
    pass

@router.put("/api/teams/INT:PK/events/swap")
def event_swap():
    pass