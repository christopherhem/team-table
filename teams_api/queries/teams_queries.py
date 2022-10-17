from typing import List, Union
from models import TeamOut, TeamIn, Error
from queries.pool import pool
#import requests

class TeamRepository:
    def create(self, team:TeamIn):
        with pool.connection() as conn:
            with conn.cursor() as db:

                result = db.execute(
                    """
                    INSERT INTO teams(
                        name,
                        type,
                        description,
                        pay_level
                    )
                    VALUES(
                        %s,
                        %s,
                        %s,
                        1
                    )
                    RETURNING id, name, type, description, pay_level ;
                    """,
                    [
                        team.name,
                        team.type.id,
                        team.description
                        #need to set pay_level to a default value
                    ]
                )
                id = result.fetchone()[0]
        #uncomment once pubsub up and running for teamvos in monoservice
        #requests.post("localhost:8085/api/stps", data = self.get_team(id))
        return self.get_team(id)

    def get_all(self)->Union[Error, List[TeamOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT
                            id,
                            name,
                            type,
                            descripton,
                            pay_level
                        FROM teams
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
                        SELECT
                            id,
                            name,
                            type,
                            description,
                            pay_level
                        
                        WHERE id=%s
                        """,
                        [id]
                    )
                    row = result.fetchone()
                    return self.team_record_to_dict(row, result.description)
        except Exception as e:
            return{"message" : str(e)}

    def delete_team(self, id):
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    DELETE FROM teams
                    WHERE id = %s
                    """,
                    [id]
                )

    def update_team(self, id, data):
        with pool.connection() as conn:
            with conn.cursor() as db:
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
        return self.to_dict(result.fetchall(),result.description)
