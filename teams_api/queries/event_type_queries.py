from typing import List, Union
from queries.pool import pool
from models import (
    Error,
    EventTypeOut,
    )

class EventTypeRepository:
    def get_all(self)->Union[Error, List[EventTypeOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT event_types(
                            e.id,
                            e.name,
                            e.event_type_href AS href
                        )
                        FROM event_types AS e
                        """
                    )
                    event_types = []
                    rows= result.fetchall()
                    for row in rows:
                        event_type = self.event_type_record_to_dict(row, result.description)
                        event_types.append(event_type)
                    return event_types
        except:
            return{"message" : "Error in event_type queries EventTypeRepository.get_all"}

    def get_event_type(self, id)->Union[Error, EventTypeOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT event_types(
                            e.id,
                            e.name,
                            e.event_type_href AS href
                        )
                        FROM team_types AS t
                        WHERE id=%s;
                        """,
                        [id]
                    )
                    row = result.fetchone()
                    return self.event_type_record_to_dict(row, result.description)
        except:
            return{"message" : "Error in team_type_queries TeamRepository.get_team_type"}

    def event_type_record_to_dict(self, row, description):
        event_type = None
        if row is not None:
            event_type = {}
            event_type_fields = ["id", "name", "href"]
            for i, column in enumerate(description):
                if column.name in event_type_fields:
                    event_type[column.name] = row[i]
            event_type["id"] = event_type["id"]
