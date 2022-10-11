import json
import requests
from fastapi import APIRouter, Depends, Response
from models import *
from typing import Union, List
from queries import SubQueries

router = APIRouter()


"""
* request
    set request json as variable
    get list of subs from table
    for sub in list
        send * request with json as body

"""

@router.post("/api/seps/subscribe", response_model = Union[SubUrlOut,Error])
def add_team(
    sub : SubUrlIn,
    response : Response,
    repo : SubQueries = Depends()
    ):
    return repo.add_sub(sub)

@router.post("/api/seps", response_model = bool)
def publish_post(
    body:json,
    response: Response,
    repo:SubQueries = Depends()
    ):
    try:
        urls = []
        for sub in repo.get_subs():
            urls.append(sub.url)
        for url in urls:
            requests.post(url, data = body)
        return True
    except:
        return False

@router.put("/api/seps", response_model = bool)
def publish_post(
    body:json,
    response: Response,
    repo:SubQueries = Depends()
    ):
    try:
        urls = []
        for sub in repo.get_subs():
            urls.append(sub.url)
        for url in urls:
            requests.put(url, data = body)
        return True
    except:
        return False

@router.delete("/api/seps", response_model = bool)
def publish_post(
    body:json,
    response: Response,
    repo:SubQueries = Depends()
    ):
    try:
        urls = []
        for sub in repo.get_subs():
            urls.append(sub.url)
        for url in urls:
            requests.delete(url, data = body)
        return True
    except:
        return False