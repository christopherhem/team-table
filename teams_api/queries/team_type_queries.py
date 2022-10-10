from typing import List, Union
from queries.pool import pool
from models import (
    Error,
    TeamTypeIn,
    TeamTypeOut,
    )

class TeamTypeRepository:
    def create(self, team_type:TeamTypeIn):
        with pool.connection() as conn:
            with conn.cursor() as db:

                result = db.execute(
                    """
                    INSERT INTO team_types(
                        name,
                    )
                    VALUES(
                        %s
                    )
                    RETURNING id;
                    """,
                    [
                        team_type.name,
                    ]
                )
        id = result.fetchone()[0]
        row = result.fetchone()
        return self.team_type_record_to_dict(row, result.description)

    def get_all(self)->Union[Error, List[TeamTypeOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT team_types(
                            t.id,
                            t.name,
                        )
                        FROM team_types AS t
                        """
                    )
                    team_types = []
                    rows= result.fetchall()
                    for row in rows:
                        team_type = self.team_type_record_to_dict(row, result.description)
                        team_types.append(team_type)
                    return team_types
        except:
            return{"message" : "Error in team_type queries TeamTypeRepository.get_all"}

    def get_team_type(self, id)-> Union[Error, TeamTypeOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT team_types(
                            t.id,
                            t.name,
                        )
                        FROM team_types AS t
                        WHERE id=%s;
                        """,
                        [id]
                    )
                    row = result.fetchone()
                    return self.team_type_record_to_dict(row, result.description)
        except:
            return{"message" : "Error in team_type_queries TeamRepository.get_team_type"}

    def delete_team_type(self, id):
        with pool.connection as conn:
            with conn.cursor as db:
                result = db.execute(
                    """
                    DELETE FROM teams
                    WHERE id = %s
                    """,
                    [id]
                )

    def update_team_type(self, id, data):
        with pool.connection as conn:
            with conn.cursor as db:
                params = [
                    data.name,
                    id
                ]
                result = db.execute(
                    """
                    UPDATE team_types
                    SET name = %s,
                    WHERE id = %s
                    RETURNING id, name
                    """,
                    params,
                )
                row = result.fetchone()
                return self.team_type_record_to_dict(row, result.description)

    def team_type_record_to_dict(self, row, description):
        team_type = None
        if row is not None:
            team_type = {}
            team_type_fields = ["id", "name"]
            for i, column in enumerate(description):
                if column.name in team_type_fields:
                    team_type[column.name] = row[i]
            team_type["id"] = team_type["id"]
        return team_type
