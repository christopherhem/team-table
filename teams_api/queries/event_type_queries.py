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
                    result = db.execute(
                        """
                        SELECT(id, name, table_name)
                        FROM event_types;
                        """
                    )
                    event_types = []
                    columns = []
                    print(result)
                    for i in result.description:
                        columns.append(i[0])
                    print(columns)
                    rows= result.fetchall()
                    return event_types
        except Exception as e:
            return{"message" : str(e)}

    def get_event_type(self, id)->Union[Error, EventTypeOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT event_types(
                            e.id,
                            e.name,
                            e.table_name
                        )
                        FROM event_types AS e
                        WHERE id=%s;
                        """,
                        [id]
                    )
                    row = result.fetchone()
                    return self.event_type_record_to_dict(row, result.description)
        except:
            return{"message" : "Error in team_type_queries TeamRepository.get_team_type"}
