from typing import List, Union
from models import Error, SwapEventVoOut, EventVoIn, CoverEventVoOut
from queries.pool import pool
import requests

class EventVoRepository:
    def create_swap_event(self, event:EventVoIn, user):

        href = f"localhost:8080/api/table/events/{event.id}"
        team = list(event.team_href)[-1]
        print(user)
        with pool.connection() as conn:
            with conn.cursor() as db:

                result = db.execute(
                    """
                    INSERT INTO shift_swap_event_vos(
                        event_href,
                        owner,
                        team,
                        shift_start,
                        shift_end,
                        availability_start,
                        availability_end
                    )
                    VALUES(
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
                    )
                    RETURNING id, event_href,owner,team,shift_start,shift_end,availability_start,availability_end;
                    """,
                    [
                        href,
                        user['account']['username'],
                        team,
                        event.shift_start,
                        event.shift_end,
                        event.availability_start,
                        event.availability_end
                    ]
                )
                id = result.fetchone()[0]
                return self.get_swap_event(id)

    def get_swap_event(self, id):
        with pool.connection() as conn:
            with conn.cursor() as db:

                result = db.execute(
                    """
                    SELECT swap_event_vos(
                        id,
                        event_href,
                        owner,
                        team,
                        shift_start,
                        shift_end,
                        availability_start,
                        availability_end,
                    )
                    WHERE id = %s;
                    """,
                    [id]
                )
                return self.to_dict(result.fetchall(),result.description)

    def create_cover_event(self, event:EventVoIn, user):

        href = f"localhost:8000/api/table/events/{event.id}"
        team = list(event.team_href)[-1]
        with pool.connection() as conn:
            with conn.cursor() as db:

                result = db.execute(
                    """
                    INSERT INTO cover_event_vos(
                        event_href,
                        owner,
                        team,
                        availability_start,
                        availability_end
                    )
                    VALUES(
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
                    )
                    RETURNING id, event_href,owner,team,availability_start,availability_end;
                    """,
                    [
                        href,
                        user['account']['username'],
                        team,
                        event.availability_start,
                        event.availability_end
                    ]
                )
        id = result.fetchone()[0]
        return self.get_cover_event(id)

    def get_cover_event(self, id):
        with pool.connection() as conn:
            with conn.cursor() as db:

                result = db.execute(
                    """
                    SELECT cover_event_vos(
                        id,
                        event_href,
                        owner,
                        team,
                        availability_start,
                        availability_end,
                    )
                    WHERE id = %s;
                    """,
                    [id]
                )
            return self.to_dict(result.fetchall(),result.description)

    def to_dict(self,rows,description):
        lst = []
        columns = [desc[0] for desc in description]
        for row in rows:
            item = {}
            for i in range(len(row)):
                item[columns[i]]=row[i]
            lst.append(item)
        if len(lst) == 1:
            lst = lst[0]
        return lst
