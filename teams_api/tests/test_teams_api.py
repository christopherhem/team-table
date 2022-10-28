# Josh's Test
from fastapi.testclient import TestClient
from main import app
from queries.teams_queries import TeamRepository
from routers.users_dependencies import get_current_user

client = TestClient(app)


class TestTeamRepository:
    def create(self, team, user):
        result = {
            "id": 1,
            "name": team.name,
            "type": team.type,
            "description": team.description,
            "pay_level": 1,
        }
        return result

    def get_all(self):
        return [
            {
                "id": 1,
                "name": "test1",
                "type": 1,
                "description": "test description",
                "pay_level": 1,
            },
            {
                "id": 2,
                "name": "test2",
                "type": 1,
                "description": "test description",
                "pay_level": 1,
            },
        ]


def get_test_user():
    return {
        "id": 1,
        "email": "test@test.com",
        "username": "test",
        "hashed_password": "9asdf91234sadf",
        "first_name": "testy",
        "last_name": "mctestface",
        "phone_number": "1234567890",
        "profile_picture-href": "https://www.google.com",
    }


app.dependency_overrides[get_current_user] = get_test_user

# def test_create_team_route(): #does not currently work on pipeline due to pub sub request but does work in docker container
#     app.dependency_overrides[
#         TeamRepository
#     ] = TestTeamRepository
#     team = ({'name' : 'test', 'type' : 1, 'description' : "test description"})
#     response = client.post('api/teams/', json = team)
#     assert response.status_code == 200
#     assert response.json() == {'id':1, "name":"test", "type":1,"description": "test description", "pay_level":1}


def test_get_teams_route():
    app.dependency_overrides[TeamRepository] = TestTeamRepository
    response = client.get("/api/teams/")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "name": "test1",
            "type": 1,
            "description": "test description",
            "pay_level": 1,
        },
        {
            "id": 2,
            "name": "test2",
            "type": 1,
            "description": "test description",
            "pay_level": 1,
        },
    ]
