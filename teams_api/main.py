from fastapi import FastAPI
from routers import teams_router, pay_level_router, team_type_router, event_types_router

app = FastAPI()
app.include_router(teams_router.router)
app.include_router(pay_level_router.router)
app.include_router(team_type_router.router)
app.include_router(event_types_router.router)
