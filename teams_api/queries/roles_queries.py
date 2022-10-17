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
                            (name, team)
                        VALUES
                            (%s, %s)
                        RETURNING id, name, team;
                        """,
                        [
                            role.name,
                            role.team
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
                    return self.to_dict(result.fetchall(),result.description)
                    
        except Exception:
            return {"message": "Could not get all roles"}

    def get_one(self, id)-> Union[Error, RolesOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT roles(
                            r.id,
                            r.name,
                        )
                        FROM roles as r
                        LEFT JOIN teams as t
                            ON (team=t.id)
                        ORDER BY r.id
                        WHERE id=%s;
                        """
                        [id]
                    )
                    row = result.fetchone()
                    return self.role_record_to_dict(row, result.description)
        except:
            return{"message" : "Error in roles RolesQueries.get_one"}

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
                    RETURNING id, name
                    """,
                    params,
                )
                row = result.fetchone()
                return self.role_record_to_dict(row, result.description)

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