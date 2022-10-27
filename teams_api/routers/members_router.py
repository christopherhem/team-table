from fastapi import APIRouter, Depends, Response, Request
from models import MemberIn, MemberOut, Error
from typing import Union, List as l
from queries.members_queries import MemberRepository
from routers.users_dependencies import get_current_user
import requests, json

router = APIRouter()


@router.post("/api/teams/{id}/members", response_model = MemberOut)
def add_member(
    member:MemberIn,
    response: Response,
    request: Request,
    repo: MemberRepository = Depends(),
    user = Depends(get_current_user)

    ):
    created_member = repo.create(member)
    headers = request.headers
    data = json.dumps(created_member)
    print(data)
    requests.post("http://pubsub:8000/api/surps/", data = data, headers = headers)
    return created_member



@router.get("/api/teams/{tid}/members", response_model = Union[Error, l[MemberOut]])
def get_members(
    tid: int,
    repo : MemberRepository = Depends(),
):
    return repo.get_members_by_team(tid)

@router.get("/api/teams/{id}/members/{uid}", response_model = Union[Error, MemberOut])
def get_member(
    uid : int,
    response : Response,
    repo : MemberRepository = Depends()
):
    record = repo.get_one(uid)
    if record is None:
        response.status_code = 404
    else:
        return record

@router.delete("/api/teams/{id}/members/{uid}", response_model = bool)
def delete_member(
    uid:int,
    repo:MemberRepository = Depends()
):
    repo.delete(uid)
    return True

@router.put("/api/teams/{id}/members/{uid}", response_model = Union[Error, MemberOut])
def edit_member(
    uid:int,
    member:MemberIn,
    repo: MemberRepository = Depends()

):
    return repo.update(uid,member)
