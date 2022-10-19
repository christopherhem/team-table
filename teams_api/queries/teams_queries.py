from typing import List, Union
from models import TeamOut, TeamIn, Error
from queries.pool import pool

from .roles_queries import *
from .members_queries import *

class TeamRepository:
    def create(self, team:TeamIn, user):
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
                        team.type,
                        team.description
                    ]
                )
                created_team = self.to_dict(result.fetchall(),result.description)
        owner_role = RolesQueries.create(self, RolesIn(name = "Owner", team = created_team['id']))
        print(user)
        print(owner_role)
        MemberRepository.create(self, MemberIn(member = user['account']['username'], role = owner_role['id']))
        return created_team


    def get_all(self)->Union[Error, List[TeamOut], TeamOut]:
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
                        FROM teams;
                        """
                    )
                    return self.to_dict(result.fetchall(),result.description)
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
                        FROM teams
                        WHERE id=%s
                        """,
                        [id]
                    )
                    return self.to_dict(result.fetchall(),result.description)
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
