from fastapi import APIRouter, Depends, Response, HTTPException
from typing import Optional, Union
from models import *
from queries.permissions_queries import PermissionsQueries

router = APIRouter()

@router.post("/api/teams/{team_id}/roles/{role_id}/permissions", response_model=Union[PermissionsOut, Error])
def add_permission(
    team_id: int,
    role_id: int,
    permission: PermissionsIn,
    q: PermissionsQueries = Depends(),
):
    return q.create(permission)

@router.get("/api/teams/{team_id}/roles/{role_id}/permissions", response_model=PermissionsOut)
def get_permissions(
    team_id: int,
    role_id: int,
    q: PermissionsQueries = Depends()
):
    return {"permissions": [q.get_all()]}

@router.get("/api/teams/{team_id}/roles/{role_id}/permissions/{perm_id}", response_model=Optional[PermissionsOut])
def get_permission(
    team_id: int,
    role_id: int,
    perm_id: int,
    response: Response,
    repo: PermissionsQueries = Depends(),
    ):
    record = repo.get_one(perm_id)
    if record is None:
        response.status_code = 404
    else:
        return record

@router.put("/api/teams/{team_id}/roles/{role_id}/permissions/{perm_id}", response_model = PermissionsOut)
def update_permission(
    team_id: int,
    role_id: int,
    perm_id: int,
    permission: PermissionsIn,
    response: Response,
    repo: PermissionsQueries = Depends()
):
    record = repo.update(perm_id, permission)
    if record is None:
        response.status_code = 404
    else:
        return record

@router.delete("/api/teams/{team_id}/roles/{role_id}/permissions/{perm_id}", response_model = bool)
def delete_permission(
    team_id: int,
    role_id: int,
    perm_id: int,
    repo: PermissionsQueries = Depends()):
    repo.delete(perm_id)
    return True


    


