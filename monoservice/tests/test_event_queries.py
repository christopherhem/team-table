# from fastapi.testclient import TestClient
# from main import app
# from queries.events_queries import EventQueries


# client = TestClient(app)

# class FakeEventQueries:
#     def get_cover_event_(self, id):
#         result = {
#             "id": id,
#             "availability_start": "2022-10-28T04:00:00",
#             "availability_end": '2022-10-28T02:00:00',
#             "user_id": 1,
#             "team_href": "http://teams:8000/api/teams/1",
#             "team_name": "team 1"
#         }
#         return result


# def get_test_user():
#     return {'id': 1, 'email':'test@test.com','username':'test','hashed_password':'9asdf91234sadf','first_name':'testy','last_name':'mctestface','phone_number':'1234567890','profile_picture-href':'https://www.google.com'}


# class CreateEventQueries:
#     def create_cover_event(self, cover_event):
#         result = {
#             "id": 1,
#             "availability_start": "2022-10-28T04:00:00",
#             "availability_end": '2022-10-28T02:00:00',
#             "user_id": 1,
#             "team_href": "http://teams:8000/api/teams/1",
#             "team_name": "team 1"
#         }
#         result.update(cover_event)
#         return result

# def test_get_cover_event():
#     app.dependency_overrides[
#         EventQueries
#     ] = FakeEventQueries
#     response = client.get("/api/table/cover_events/{id}", id = 1)
#     assert response.status_code == 200
#     assert response.json() == {
#             "id": 1,
#             "availability_start": "2022-10-28T04:00:00",
#             "availability_end": '2022-10-28T02:00:00',
#             "user_id": 1,
#             "team_href": "http://teams:8000/api/teams/1",
#             "team_name": "team 1"
#         }
