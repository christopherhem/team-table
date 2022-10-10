from typing import List, Union
from models import TeamOut, TeamIn, Error
from queries.pool import pool

class TeamRepository:
    def create(team:TeamIn):
        with pool.connection() as conn:
            with conn.cursor() as db:

                result = db.execute(
                    """
                    INSERT INTO teams(
                        name,
                        type,
                        description
                    )
                    VALUES(
                        %s,
                        %s,
                        %s
                    )
                    RETURNING id;
                    """,
                    [
                        team.name,
                        team.type,
                        team.description
                        #need to set pay_level to a default value
                    ]
                )
        id = result.fetchone()[0]
        paid = result.fetchone()[4]
        data = team.dict()
        return TeamOut(id=id, pay_level = paid, **data)

    def get_all(self)->Union[Error, List[TeamOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT teams(
                            t.id,
                            t.name,
                            t.type,
                            t.descripton,
                            t.pay_level
                        )
                        FROM teams AS t
                        LEFT JOIN team_types as tt
                            ON (type=tt.id)
                        LEFT JOIN pay_levels AS p
                            ON (paylevel=p.id)
                        GROUP BY
                            t.id, t.name,
                            t.description
                        ORDER BY t.id;
                        """
                    )
                    teams = []
                    rows= result.fetchall()
                    for row in rows:
                        team = self.team_record_to_dict(row, result.description)
                        teams.append(team)
                    return teams
        except:
            return{"message" : "Error in team_queries TeamRepository.get_all"}

    def get_team(self, id)->Union[Error, TeamOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT teams(
                            t.id,
                            t.name,
                            t.type,
                            t.descripton,
                            t.pay_level
                        )
                        FROM teams AS t
                        LEFT JOIN team_types as tt
                            ON (type=tt.id)
                        LEFT JOIN pay_levels AS p
                            ON (paylevel=p.id)
                        GROUP BY
                            t.id, t.name,
                            t.description
                        WHERE id=%s;
                        """,
                        [id]
                    )
                    row = result.fetchone()
                    return self.team_record_to_dict(row, result.description)
        except:
            return{"message" : "Error in team_queries TeamRepository.get_team"}

    def delete_team(self, id):
        with pool.connection as conn:
            with conn.cursor as db:
                result = db.execute(
                    """
                    DELETE FROM teams
                    WHERE id = %s
                    """,
                    [id]
                )

    def update_team(self, id, data):
        with pool.connection as conn:
            with conn.cursor as db:
                params = [
                    data.name,
                    data.type,
                    data.description,
                    data.pay_level,
                    id
                ]
                result = db.execute(
                    """
                    UPDATE teams
                    SET name = %s,
                        type = %s,
                        description = %s,
                        pay_level = %s
                    WHERE id = %s
                    RETURNING id, name, type, description, pay_level
                    """,
                    params,
                )
                team = None
                row = result.fetchone()
                if row is not None:
                    team = {}
                    for i, column in enumerate(result.description):
                        team[column.name] = row[i]
                return team


    def team_record_to_dict(self, row, description):
        team = None
        if row is not None:
            team = {}
            team_fields = [
                "id",
                "name",
                "type",
                "description",
                "pay_level"
            ]
            for i, column in enumerate(description):
                if column.name in team_fields:
                    team[column.name] = row[i]
            team["id"] = team["id"]
        type = {}
        type_fields = [
            "id",
            "name"
        ]
        for i, column in enumerate(description):
            if column.name in type_fields:
                type[column.name] = row[i]
        type["id"] = type["id"]

        team["type"] = type
        pay_level = {}
        pay_level_fields = [
            "id",
            "name",
            "max_members",
            "max_roles"
        ]
        for i, column in enumerate(description):
            if column.name in pay_level_fields:
                pay_level[column.name] = row[i]
        pay_level["id"] = pay_level["id"]

        team["pay_level"] = pay_level
        return team





# class TeamTypeRepository:
#     def get_team_types(self):
#         with pool.connection as conn:
#             with conn.cursor as db:
#                 result = db.execute(
#                     """
#                     SELECT id
#                     """
#                 )
