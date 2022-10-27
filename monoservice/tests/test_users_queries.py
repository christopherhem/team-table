# Christopher's Test
from fastapi.testclient import TestClient
from main import app 
from queries.users_queries import UserQueries


client = TestClient(app)

class FakeUserQueries:
    def get_all(self):
        return []

class CreateUserQueries:
    def create_user(self, user):
        result = {
            "id": 1,
            "username": "fakeuser1",
            "first_name": "fakefirst",
            "last_name": "fakelast",
            "email": "fake@mail.com",
            "phone_number": None,
            "profile_picture_href": None
        }
        result.update(user)
        return result

def test_get_all_users():
    app.dependency_overrides[
        UserQueries
    ] = FakeUserQueries
    response = client.get("api/users")
    app.dependency_overrides = {}
    assert response.status_code == 200
    assert response.json() == []