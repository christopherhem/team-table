import requests, json
from models import *
from routers.users_router import create_user

create_user(
    UserIn(
        username="Test1",
        password="test",
        first_name="testy1",
        last_name="mctestface",
        email="test1@test.com",
    )
)
create_user(
    UserIn(
        username="Test2",
        password="test",
        first_name="testy2",
        last_name="mctestface",
        email="test2@test.com",
    )
)
