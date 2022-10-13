from typing import List, Union
from queries.pool import pool
from models import (
    Error,
    EventTypeOut,
    )

class EventTypeRepository:
    def get_all(self)->Union[List[EventTypeOut], Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, name, table_name
                        FROM event_types;
                        """
                    )
            return self.to_dict(result.fetchall(), result.description)
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
                    return self.to_dict(result.fetchall(), result.description)
        except:
            return{"message" : "Error in team_type_queries TeamRepository.get_team_type"}

    def to_dict(self,rows,description):
        new_dict = []
        columns = [desc[0] for desc in description]
        for row in rows:
            item = {}
            for i in range(len(row)):
                item[columns[i]]=row[i] 
            new_dict.append(item)
        return new_dict
