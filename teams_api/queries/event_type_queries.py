from typing import List, Union
from queries.pool import pool
from models import (
    Error,
    EventTypeOut,
    )

class EventTypeRepository:
    error = None
    def get_all(self)->Union[List[EventTypeOut], Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        SELECT id, name, table_name
                        FROM event_types;
                        """
                    )
                    event_types = []
                    rows= db.fetchall()
                    for row in rows:
                        event_type = self.event_type_record_to_dict(row, db.description)
                        event_types.append(event_type)
                    return event_types
        except Exception as e:
            return{"message" : str(e)}

    def get_event_type(self, id)->Union[Error, EventTypeOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, name, table_name

                        FROM event_types
                        WHERE id=%s;
                        """,
                        [id]
                    )
                    row = result.fetchone()
                    return self.event_type_record_to_dict(row, result.description)
        except:
            return{"message" : "Error in event_type_queries TeamRepository.get_team_type"}

    def event_type_record_to_dict(self, row, description):
        event_type = None
        if row is not None:
            event_type = {}
            event_type_fields = ["id", "name", "table_name"]
            for i, column in enumerate(description):
                print(column.name)
                if column.name in event_type_fields:
                    event_type[column.name] = row[i]
            event_type["id"] = event_type["id"]
        return event_type
