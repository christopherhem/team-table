from fastapi import FastAPI
from routers import teams_router

app = FastApi()
app.include_router(teams_router.router)

