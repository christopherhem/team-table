<<<<<<< HEAD
from models import TeamIn
from queries.teams_queries import TeamRepository

=======
from fastapi.testclient import TestClient
from main import app
from models import TeamIn
from queries.teams_queries import TeamRepository

client = TestClient(app)
>>>>>>> main
team = TeamIn(name = 'test', type = 1)

def test_create_team():
    team = TeamIn(name = 'test', type = 1)
    created_team = TeamRepository.create(team)
    assert created_team == {'id':1, "name":"test", "type":1,"description":None, "pay_level":1} 

# comment to update and force pipeline test
