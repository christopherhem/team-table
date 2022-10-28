from typing import List, Union
from queries.pool import pool
from models import (
    Error,
    TeamTypeIn,
    TeamTypeOut,
)


class TeamTypeRepository:
    def create(self, team_type: TeamTypeIn, event_types: List[int]):
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    INSERT INTO team_types(
                        name
                    )
                    VALUES(
                        %s
                    )
                    RETURNING id, name;
                    """,
                    [team_type.name],
                )
                team_type = self.to_dict(result.fetchall(), result.description)
                print(team_type)
                team_type_id = team_type["id"]
        with pool.connection() as conn:
            with conn.cursor() as db:
                for event_type in event_types:
                    many_to_many = db.execute(
                        """
                                INSERT INTO event_types_team_types(
                                    team_type,
                                    event_type
                                )
                                VALUES(
                                    %s,
                                    %s
                                )
                                RETURNING id, team_type, event_type
                                """,
                        [team_type_id, event_type],
                    )
        return team_type

    def get_all(self) -> Union[Error, List[TeamTypeOut]]:
        print("function called")
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, name
                        FROM team_types;
                        """
                    )
                    out = self.to_dict(result.fetchall(), result.description)
            if type(out) != list:
                temp = []
                temp.append(out)
                out = temp
            return out
        except:
            return {"message": "Error in team_type queries TeamTypeRepository.get_all"}

    def get_team_type(self, id) -> Union[Error, TeamTypeOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, name
                        FROM team_types
                        WHERE id=%s;
                        """,
                        [id],
                    )
                    return self.to_dict(result.fetchall(), result.description)
        except:
            return {
                "message": "Error in team_type_queries TeamRepository.get_team_type"
            }

    def delete_team_type(self, id):
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    DELETE FROM teams
                    WHERE id = %s
                    """,
                    [id],
                )

    def update_team_type(self, id, data):
        with pool.connection() as conn:
            with conn.cursor() as db:
                params = [data.name, id]
                result = db.execute(
                    """
                    UPDATE team_types
                    SET name = %s,
                    WHERE id = %s
                    RETURNING id, name
                    """,
                    params,
                )
                return self.to_dict(result.fetchall(), result.description)

    def to_dict(self, rows, description):
        lst = []
        columns = [desc[0] for desc in description]
        for row in rows:
            item = {}
            for i in range(len(row)):
                item[columns[i]] = row[i]
            lst.append(item)
        if len(lst) == 1:
            lst = lst[0]
        return lst
