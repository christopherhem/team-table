from fastapi.testclient import TestClient
from main import app
from queries.events_queries import EventQueries


client = TestClient(app)

class FakeEventQueries:
    def get_cover_event(self, id):
        result = {
            "id": id,
            "availability_start": "2022-10-28T04:00:00",
            "availability_end": '2022-10-28T02:00:00',
            "user_id": 1,
            "team_href": "http://teams:8000/api/teams/1"
        }
        return result


def test_get_cover_event():
    app.dependency_overrides[
        EventQueries
    ] = FakeEventQueries
    response = client.get("/api/table/cover_events/1")
    assert response.status_code == 200
    assert response.json() == {
            "id": 1,
            "availability_start": "2022-10-28T04:00:00",
            "availability_end": '2022-10-28T02:00:00',
            "user_id": 1,
            "team_href": "http://teams:8000/api/teams/1"
        }
