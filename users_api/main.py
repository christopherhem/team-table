from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

from routers import users

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

app.include_router(users.router)


@app.get("/api/users")
def get_users():
    return {
        "users": {
            "id": int,
            "username": str,
            "password": str,
            "first_name": str,
            "last_name": str,
            "email": str,
            "phone_number": str,
            "profile_picture_href": str,
    }
}
    
