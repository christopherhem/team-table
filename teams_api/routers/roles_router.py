from fastapi import APIRouter, Depends, Response, HTTPException
from typing import List, Optional, Union
from models import *
from queries.roles_queries import RolesQueries

router = APIRouter()

@router.post("/api/teams/{team_id}/roles", response_model=Union[RolesOut, Error])
def add_role(
    team_id: int,
    role: RolesIn,
    q: RolesQueries = Depends(),
):
    roles = q.get_all()
    for r in roles:
        if role.name == r.name:
            raise HTTPException(status_code=409, detail=f'Role name duplicate error: {role.name} already exists...')
    return q.create(role)

@router.get("/api/teams/{team_id}/roles", response_model=RolesOut)
def get_roles(
    team_id: int,
    q: RolesQueries = Depends()
):
    return {"roles": [q.get_all()]}

@router.get("/api/teams/{team_id}/roles/{role_id}", response_model=Optional[RolesOut])
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


    


