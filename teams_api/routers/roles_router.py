from fastapi import APIRouter, Depends, Response, HTTPException
from typing import List, Optional, Union
from models import RolesOut, RolesIn, Error
from queries.roles_queries import RolesQueries

router = APIRouter()

@router.post("/api/teams/roles", response_model=Union[RolesOut, Error])
def add_role(
    role: RolesIn,
    q: RolesQueries = Depends(),
):
    return q.create(role)

@router.get("/api/teams/{team_id}/roles", response_model= List[RolesOut])
def get_roles(
    team_id: int,
    q: RolesQueries = Depends()
):
    return q.get_all(team_id)

@router.get("/api/teams/{team_id}/roles/{role_id}", response_model=RolesOut)
def get_role(
    team_id: int,
    role_id: int,
    response: Response,
    repo: RolesQueries = Depends(),
    ):
    record = repo.get_one(role_id)
    if record is None:
        response.status_code = 404
    else:
        return record

@router.put("/api/teams/{team_id}/roles/{role_id}", response_model = RolesOut)
def update_role(
    role_id: int,
    team_id: int,
    role: RolesIn,
    response: Response,
    repo: RolesQueries = Depends()
):
    record = repo.update(role_id, role)
    if record is None:
        response.status_code = 404
    else:
        return record

@router.delete("/api/teams/{team_id}/roles/{role_id}", response_model = bool)
def delete_role(
    team_id: int,
    role_id: int,
    repo: RolesQueries = Depends()):
    repo.delete(role_id)
    return True


    


