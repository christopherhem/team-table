from fastapi import APIRouter, Depends, Response, HTTPException
from typing import List, Optional, Union
from models import *
from queries.permissions_queries import PermissionsQueries

router = APIRouter()

@router.post("/api/teams/{team_id}/roles", response_model=Union[PermissionsOut, Error])
def add_permission(
    team_id: int,
    role: RolesIn,
    q: PermissionsQueries = Depends(),
):
    roles = q.get_all()
    for r in roles:
        if role.name == r.name:
            raise HTTPException(status_code=409, detail=f'Role name duplicate error: {role.name} already exists...')
    return q.create(role)

@router.get("/api/teams/{team_id}/roles", response_model=PermissionsOut)
def get_permissions(
    team_id: int,
    q: PermissionsQueries = Depends()
):
    return {"roles": [q.get_all()]}

@router.get("/api/teams/{team_id}/roles/{role_id}", response_model=Optional[PermissionsOut])
def get_permission(
    team_id: int,
    role_id: int,
    response: Response,
    repo: PermissionsQueries = Depends(),
    ):
    record = repo.get_one(role_id)
    if record is None:
        response.status_code = 404
    else:
        return record

@router.put("/api/teams/{team_id}/roles/{role_id}", response_model = PermissionsOut)
def update_permission(
    role_id: int,
    team_id: int,
    role: RolesIn,
    response: Response,
    repo: PermissionsQueries = Depends()
):
    record = repo.update(role_id, role)
    if record is None:
        response.status_code = 404
    else:
        return record

@router.delete("/api/teams/{team_id}/roles/{role_id}", response_model = bool)
def delete_permission(
    team_id: int,
    role_id: int,
    repo: PermissionsQueries = Depends()):
    repo.delete(id)
    return True


    


