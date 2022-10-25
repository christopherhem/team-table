from fastapi import FastAPI
from routers import (
    event_types_router,
    members_router,
    pay_level_router,
    permissions_router,
    roles_router,
    teams_router,
    team_type_router,
    u_event_vo_router,
    swap_router
)

from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        os.environ.get("CORS_HOST", "http://localhost:3000")
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(event_types_router.router)
app.include_router(members_router.router)
app.include_router(pay_level_router.router)
app.include_router(permissions_router.router)
app.include_router(roles_router.router)
app.include_router(teams_router.router)
app.include_router(team_type_router.router)
app.include_router(u_event_vo_router.router)
app.include_router(swap_router.router)
