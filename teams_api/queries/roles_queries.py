from typing import List, Union
from queries.pool import pool
from models import *

class RolesQueries:
    def create(self, role: RolesIn) -> Union[RolesOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO roles
                            (name, teams)
                        VALUES
                            (%s, %s)
                        RETURNING id;
                        """,
                        [
                            role.name,
                            role.team
                        ]
                    )
                    id = result.fetchone()[0]
                    return self.role_in_to_out(id,role)
        except Exception:
            return {"message": "Unable to create"}

    def get_all(self) -> Union[Error, List[RolesOut]]:
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
                        ORDER BY r.id;
                        """
                    )
                    roles = []
                    rows = result.fetchall()
                    for row in rows:
                        role = self.role_record_to_dict(row, result.description)
                        roles.append(role)
                    return roles
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

    def role_in_to_out(self, id: int, role: RolesIn):
        old_data = role.dict()
        return RolesOut(id=id, **old_data)

    def role_record_to_dict(self, row, description):
        role = None
        if row is not None:
            role = {}
            role_fields = ["id", "name"]
            for i, column in enumerate(description):
                if column.name in role_fields:
                    role[column.name] = row[i]
            role["id"] = role["id"]
        return role
