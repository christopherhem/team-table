from fastapi import APIRouter, Depends, Response
from models import MemberIn, MemberOut, Error
from typing import Union, List as l
from queries.members_queries import MemberRepository

router = APIRouter()


@router.post("/api/teams/{id}/members")
def add_member(id: int,
    member:MemberIn,
    response: Response,
    repo: MemberRepository = Depends(),
    ):
    response.status_code = 400
    return repo.create(member, id)
    

@router.get("/api/teams/{id}/members", reponse_model = Union[Error, l[MemberOut]])
def get_members(
    repo : MemberRepository = Depends(),
):
    return {"members": [repo.get_all()]}

@router.get("/api/teams/{id}/members/{uid}", response_model = Union[Error, MemberOut])
def get_member(
    uid:int,
    response:Response,
    repo:MemberRepository = Depends()
):
    record = repo.get_one(uid)
    if record is None:
        response.status_code = 404
    else:
        return record

@router.delete("/api/teams/{id}/members/{uid}", response_model = bool)
def delete_member(
    uid:int,
    repo:MemberRepository
):
    repo.delete(uid)
    return True

@router.put("/api/teams/{}/members/{uid}", response_model = Union[Error, MemberOut])
def edit_member(
    uid:int,
    repo:MemberRepository,
    member:MemberIn
):
    return repo.update(uid,member)


@router.put("/api/teams/{id}/members/{uid}")
def edit_member():
    pass