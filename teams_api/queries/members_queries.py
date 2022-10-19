from typing import List, Union
from models import MemberIn, MemberOut, Error
from queries.pool import pool

class MemberRepository:
    def get_all(self)->Union[Error, List[MemberOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, member_username, role
                        FROM members
                        """
                    )
                    return self.to_dict(result.fetchall(),result.description)
        except:
            return{"message" : "Error in member_queries get_all"}
    
    def get_members_by_team(self, tid):
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, team
                        FROM roles 
                        WHERE team = %s
                        """,
                        [tid]
                    )
                    role_dics = self.to_dict(result.fetchall(),result.description)
            role_ids = []
            for dic in role_dics:
                role_ids.append(dic['id'])
            members = []
            for rid in role_ids:
                with pool.connection() as conn:
                    with conn.cursor() as db:
                        result = db.execute(
                            """
                            SELECT id, member_username, role
                            FROM members
                            WHERE role = %s
                            """,
                            [rid]
                        )
                        members.append(self.to_dict(result.fetchall(),result.description))
            return members
        except Exception as e:
            return {"message": f"Error in member_queries get_members_by_team: {e}"}
    
    def get_one(self, id)->Union[Error, MemberOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, member_username, role
                        FROM members
                        WHERE id=%s;
                        """,
                        [id]
                    )
                    return self.to_dict(result.fetchall(), result.description)
        except:
            return{"message" : "Error in member_queries get_one"}
    def create(self, member:MemberIn):
        with pool.connection() as conn:
            with conn.cursor() as db:

                result = db.execute(
                    """
                    INSERT INTO members(
                        member_username,
                        role
                    )
                    VALUES(
                        %s,
                        %s
                    )
                    RETURNING id, member_username, role;
                    """,
                    [
                        member.member,
                        member.role
                    ]
                )
                return self.to_dict(result.fetchall(),result.description)

    def delete(self, id):
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    DELETE FROM members
                    WHERE id = %s
                    """,
                    [id]
                )

    def update(self, id:int, data:MemberIn)->Union[Error,MemberOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    params = [
                        data.role.id,
                        id
                    ]
                    result = db.execute(
                        """
                        UPDATE members
                        SET role = %s
                        WHERE id = %s
                        RETURNING id, member_username, role
                        """,
                        params
                    )
                    return self.to_dict(result.fetchall(),result.description)
        except:
            return {"message":"Error in members_queries.update"}

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