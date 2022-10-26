from models import TeamIn
from queries.teams_queries import TeamRepository

team = TeamIn(name = 'test', type = 1)

def test_create_team():
    team = TeamIn(name = 'test', type = 1)
    created_team = TeamRepository.create(team)
    assert created_team == {'id':1, "name":"test", "type":1,"description":None, "pay_level":1} 


