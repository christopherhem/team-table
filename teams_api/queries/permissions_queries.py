from typing import List, Optional, Union
from queries.pool import pool
from models import *

class PermissionsQueries:
    def create(self, perm: PermissionsIn) -> Union[PermissionsOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO permissions (
                            role, 
                            approve_swaps,
                            invite_members,
                            add_roles
                        )
                        VALUES
                            (%s, %b, %b, %b)
                        RETURNING id;
                        """,
                        [
                            perm.role,
                            perm.approve_swaps,
                            perm.invite_members,
                            perm.add_roles
                        ]
                    )
                    id = result.fetchone()[0]
                    return self.perm_in_to_out(id, perm)
        except Exception:
            return {"message": "Unable to create permission"}

    def get_all(self) -> Union[Error, List[PermissionsOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT permissions(
                            p.id,
                            p.role,
                            p.approve_swaps,
                            p.invite_members,
                            p.add_roles
                        )
                        FROM permissions as p
                        LEFT JOIN roles as r
                            ON (role=r.id)
                        ORDER BY p.id;
                        """
                    )
                    permissions = []
                    rows = result.fetchall()
                    for row in rows:
                        permission = self.perm_record_to_dict(row, result.description)
                        permissions.append(permission)
                    return permissions
        except Exception:
            return {"message": "Could not get all permissions"}

    def get_one(self, id)-> Union[Error, PermissionsOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT permissions (
                            p.id,
                            p.role,
                            p.approve_swaps,
                            p.invite_members,
                            p.add_roles
                        )
                        FROM permissions as p
                        LEFT JOIN roles as r
                            ON (role=r.id)
                        ORDER BY p.id
                        WHERE id=%s;
                        """
                        [id]
                    )
                    row = result.fetchone()
                    return self.perm_record_to_dict(row, result.description)
        except:
            return{"message" : "Error in permissions PermissionsQueries.get_one"}
    
    def update(self, id, data):
        with pool.connection as conn:
            with conn.cursor as db:
                params = [
                    data.name,
                    id
                ]
                result = db.execute(
                    """
                    UPDATE permissions
                    SET role = %s, approve_swaps = %b, invite_members = %b, add_roles = %b
                    WHERE id = %s
                    RETURNING 
                        id, 
                        role,
                        approve_swaps,
                        invite_members,
                        add_roles
                    """,
                    params,
                )
                row = result.fetchone()
                return self.perm_record_to_dict(row, result.description)

    def delete(self, id):
        with pool.connection as conn:
            with conn.cursor as db:
                result = db.execute(
                    """
                    DELETE FROM permissions
                    WHERE id = %s
                    """,
                    [id]
                )

    def perm_in_to_out(self, id: int, perm: PermissionsIn):
        old_data = perm.dict()
        return PermissionsOut(id=id, **old_data)
    
    def perm_record_to_dict(self, row, description):
        perm = None
        if row is not None:
            perm = {}
            perm_fields = ["id", "role", "approve_swaps", "invite_members", "add_roles"]
            for i, column in enumerate(description):
                if column.role in perm_fields:
                    perm[column.role] = row[i]
            perm["id"] = perm["id"]
        return perm