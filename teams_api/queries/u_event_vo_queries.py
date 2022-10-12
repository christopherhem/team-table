from typing import List, Union
from models import SwapEventVoIn, Error, SwapEventVoOut, CoverEventVoIn, CoverEventVoOut
from queries.pool import pool
import requests

class SwapEventVoRepository:
    def create(self, event:SwapEventVoIn):

        href = f"localhost:8000/api/table/events/{event.id}"
        team = requests.get(event.team_href)
        with pool.connection() as conn:
            with conn.cursor() as db:

                result = db.execute(
                    """
                    INSERT INTO swap_event_vos(
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
                    );
                    """,
                    [
                        href,
                        #jwt user id somehow,
                        team.id,
                        event.shift_start,
                        event.shift_end,
                        event.availability_start,
                        event.availability_end
                    ]
                )
        id = result.fetchone()[0]
        return self.get_event(id)

    def get_event(self, id):
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
        event = {}
        row = result.fetchone()
        count=0
        for i in result.description:
            event[i[0]]=row[count]
            count+=1
        return event


class CoverEventVoRepository:
    def create(self, event:CoverEventVoIn):

        href = f"localhost:8000/api/table/events/{event.id}"
        team = requests.get(event.team_href)
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
                    );
                    """,
                    [
                        href,
                        #jwt user id somehow,
                        team.id,
                        event.availability_start,
                        event.availability_end
                    ]
                )
        id = result.fetchone()[0]
        return self.get_event(id)

    def get_event(self, id):
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
        event = {}
        row = result.fetchone()
        count=0
        for i in result.description:
            event[i[0]]=row[count]
            count+=1
        return event

