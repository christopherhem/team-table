import json
import requests
from fastapi import APIRouter, Depends, Response, Request
from models import *
from typing import Union
from queries import TeamSubQueries, MainSubQueries, MemberSubQueries

router = APIRouter()

@router.post("/api/seps/subscribe/", response_model=Union[SubUrlOut, Error])
def add_team(sub: SubUrlIn, response: Response, repo: TeamSubQueries = Depends()):
    return repo.add_sub(sub)


@router.post("/api/seps/", response_model=Union[bool, Error])
def publish_post(
    body: EventVoIn,
    request: Request,
    response: Response,
    repo: TeamSubQueries = Depends(),
):
    headers = {"Authorization": request.headers["Authorization"]}
    try:
        urls = []
        for sub in repo.get_subs():
            urls.append(sub["url"])
        for url in urls:
            body = json.dumps(dict(body))
            requests.post(url, data=body, headers=headers)
        return True
    except Exception as e:
        return {"message": str(e)}


@router.put("/api/seps/", response_model=bool)
def publish_put(
    body: EventVoIn,
    request: Request,
    response: Response,
    repo: TeamSubQueries = Depends(),
):
    headers = {"Authorization": request.headers["Authorization"]}
    try:
        urls = []
        for sub in repo.get_subs():
            urls.append(sub["url"])
        for url in urls:
            body = json.dumps(dict(body))
            requests.put(url, data=body, headers=headers)
        return True
    except Exception as e:
        return {"message": str(e)}


@router.delete("/api/seps/", response_model=bool)
def publish_delete(
    body: EventVoIn,
    request: Request,
    response: Response,
    repo: TeamSubQueries = Depends(),
):
    headers = {"Authorization": request.headers["Authorization"]}
    try:
        urls = []
        for sub in repo.get_subs():
            urls.append(sub["url"])
        for url in urls:
            body = json.dumps(dict(body))
            requests.delete(url, data=body, headers=headers)
        return True
    except Exception as e:
        return {"message": str(e)}


@router.post("/api/smps/subscribe", response_model=Union[SubUrlOut, Error])
def add_team(sub: SubUrlIn, response: Response, repo: MainSubQueries = Depends()):
    return repo.add_sub(sub)


@router.post("/api/smps/", response_model=Union[bool, Error])
def publish_post(
    body: TeamVoIn,
    request: Request,
    response: Response,
    repo: MainSubQueries = Depends(),
):
    headers = {"Authorization": request.headers["Authorization"]}
    try:
        urls = []
        for sub in repo.get_subs():
            urls.append(sub["url"])
        for url in urls:
            body = json.dumps(dict(body))
            requests.post(url, data = body, headers = headers)
        return True
    except Exception as e:
        return {"message": str(e)}


@router.put("/api/smps/", response_model=bool)
def publish_put(
    body: TeamVoIn,
    request: Request,
    response: Response,
    repo: MainSubQueries = Depends(),
):
    headers = {"Authorization": request.headers["Authorization"]}
    try:
        urls = []
        for sub in repo.get_subs():
            urls.append(sub["url"])
        for url in urls:
            body = json.dumps(dict(body))
            requests.put(url, data=body, headers=headers)
        return True
    except Exception as e:
        return {"message": str(e)}


@router.delete("/api/smps/", response_model=bool)
def publish_delete(
    body: TeamVoIn,
    request: Request,
    response: Response,
    repo: MainSubQueries = Depends(),
):
    headers = {"Authorization": request.headers["Authorization"]}
    try:
        urls = []
        for sub in repo.get_subs():
            urls.append(sub["url"])
        for url in urls:
            body = json.dumps(dict(body))
            requests.delete(url, data=body, headers=headers)
        return True
    except Exception as e:
        return {"message": str(e)}


@router.post("/api/surps/subscribe", response_model=Union[SubUrlOut, Error])
def add_team(sub: SubUrlIn, response: Response, repo: MemberSubQueries = Depends()):
    return repo.add_sub(sub)


@router.post("/api/surps/", response_model=Union[bool, Error])
def publish_post(
    body: MemberIn,
    request: Request,
    response: Response,
    repo: MemberSubQueries = Depends(),
):
    headers = {"Authorization": request.headers["Authorization"]}
    urls = []
    for sub in repo.get_subs():
        urls.append(sub["url"])
    for url in urls:
        body = json.dumps(dict(body))
        requests.post(url, data=body, headers=headers)
    return True


@router.put("/api/surps/", response_model=bool)
def publish_put(
    body: TeamVoIn,
    request: Request,
    response: Response,
    repo: MemberSubQueries = Depends(),
):
    headers = {"Authorization": request.headers["Authorization"]}
    try:
        urls = []
        for sub in repo.get_subs():
            urls.append(sub["url"])
        for url in urls:
            body = json.dumps(dict(body))
            requests.put(url, data=body, headers=headers)
        return True
    except Exception as e:
        return {"message": str(e)}


@router.delete("/api/surps/", response_model=bool)
def publish_delete(
    body: TeamVoIn,
    request: Request,
    response: Response,
    repo: MemberSubQueries = Depends(),
):
    headers = {"Authorization": request.headers["Authorization"]}
    try:
        urls = []
        for sub in repo.get_subs():
            urls.append(sub["url"])
        for url in urls:
            body = json.dumps(dict(body))
            requests.delete(url, data=body, headers=headers)
        return True
    except Exception as e:
        return {"message": str(e)}
