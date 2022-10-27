# Josh's Test
from fastapi.testclient import TestClient
from main import app
from models import TeamIn, TeamOut
from queries.teams_queries import TeamRepository
from routers.users_dependencies import get_current_user
import json

client = TestClient(app)

class TestTeamRepository:
    def create(name, type, description):
        result = {'id' : 1, 'name' : name, 'type' : type, 'description' : description, 'pay_level' : 1}
        return result

def get_test_user():
    return {'id': 1, 'email':'test@test.com','username':'test','hashed_password':'9asdf91234sadf','first_name':'testy','last_name':'mctestface','phone_number':'1234567890','profile_picture-href':'https://www.google.com'}

app.dependency_overrides[get_current_user] = get_test_user

def test_create_team_route():
    app.dependency_overrides[
        TeamRepository
    ] = TestTeamRepository
    team = json.dumps({'name' : 'test', 'type' : 1, 'description' : "test description"})
    response = client.post('api/teams/', data = team)
    assert response.status_code == 200
    assert response.json() == {'id':1, "name":"test", "type":1,"description": "test description", "pay_level":1} 
