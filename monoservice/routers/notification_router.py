from fastapi import APIRouter, Depends, status, Response, HTTPException, Request
from queries.notification_queries import NotificationRepository
from typing import Union, List
from authenticator import authenticator
from models import NotificationOut

router = APIRouter()


@router.get("/api/notifications/", response_model=List[NotificationOut])
def get_user_notifications(
    request: Request,
    response: Response,
    user=Depends(authenticator.get_current_account_data),
    repo: NotificationRepository = Depends(),
):
    return repo.get_notifications_by_user(user)


@router.put("/api/notifications/{id}", response_model=bool)
def update_status(
    response: Response,
    id: int,
    user=Depends(authenticator.get_current_account_data),
    repo: NotificationRepository = Depends(),
):
    return repo.update_seen(user["id"], id)


@router.delete("/api/notifications/{id}", response_model=bool)
def delete_notification(
    id: int,
    user=Depends(authenticator.get_current_account_data),
    repo: NotificationRepository = Depends(),
):
    return repo.delete(user["id"], id)
