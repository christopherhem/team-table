from fastapi import FastAPI
<<<<<<< HEAD
from routers import teams_router, pay_level_router, roles_router, permissions_router, team_type_router, event_types_router

=======
from fastapi.middleware.cors import CORSMiddleware
import os
from routers import teams_router, pay_level_router, members_router
>>>>>>> Josh

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

app.include_router(teams_router.router)
app.include_router(pay_level_router.router)
<<<<<<< HEAD
app.include_router(roles_router.router)
app.include_router(permissions_router.router)
app.include_router(team_type_router.router)
app.include_router(event_types_router.router)
=======
app.include_router(members_router.router)
>>>>>>> Josh
