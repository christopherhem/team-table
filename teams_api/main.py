from fastapi import FastAPI
from routers import teams_router, pay_level_router, roles_router, permissions_router

app = FastAPI()
app.include_router(teams_router.router)
app.include_router(pay_level_router.router)
app.include_router(roles_router.router)
app.include_router(permissions_router.router)
