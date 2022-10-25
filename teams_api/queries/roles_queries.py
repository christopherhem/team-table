from re import L
from typing import List, Union
from queries.pool import pool
from models import RolesIn, RolesOut, Error

class RolesQueries:
    def create(self, role: RolesIn) -> Union[RolesOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO roles
                            (name, team, can_invite, can_approve)
                        VALUES
                            (%s, %s, %s, %s)
                        RETURNING id, name, team, can_invite, can_approve;
                        """,
                        [
                            role.name,
                            role.team,
                            role.can_invite,
                            role.can_approve
                        ]
                    )
                    return self.to_dict(result.fetchall(),result.description)
        except Exception:
            return {"message": "Unable to create"}

    def get_all(self, tid) -> Union[Error, List[RolesOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id,name,team
                        FROM roles
                        WHERE team = %s
                        """,
                        [tid]
                    )
                    roles = self.to_dict(result.fetchall(),result.description)
            if type(roles) != list:
                l = []
                l.append(roles)
                roles = l
            return roles
                    
        except Exception as e:
            return {"message": f"Error in roles_queries get_all: {e}"}

    def get_one(self, id)-> Union[Error, RolesOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, name, team
                        FROM roles
                        WHERE id = %s
                        """,
                        [id]
                    )
                    return self.to_dict(result.fetchall(),result.description)
        except Exception as e:
            return{"message" : f"Error in roles_queries get_one: {e}"}

    def update(self, id, data):
        with pool.connection() as conn:
            with conn.cursor() as db:
                params = [
                    data.name,
                    id
                ]
                result = db.execute(
                    """
                    UPDATE roles
                    SET name = %s,
                    WHERE id = %s
                    RETURNING id, name, team
                    """,
                    params,
                )
                return self.to_dict(result.fetchall(),result.description)

    def delete(self, id):
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    DELETE FROM roles
                    WHERE id = %s
                    """,
                    [id]
                )

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