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
                        SELECT members(
                            m.id,
                            m.member,
                            m.role
                        )
                        FROM members AS m
                        LEFT JOIN roles AS r
                            ON (role=r.id)
                        LEFT JOIN user_vos AS u
                            ON (member=u.id)
                        GROUP BY
                            m.id
                        WHERE id=%s;
                        """,
                        [id]
                    )
                    members = []
                    rows= result.fetchall()
                    for row in rows:
                        member = self.record_to_dict(row, result.description)
                        members.append(member)
                    return members
        except:
            return{"message" : "Error in member_queries get_one"}

    def get_one(self, id)->Union[Error, MemberOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT members(
                            m.id,
                            m.member,
                            m.role
                        )
                        FROM members AS m
                        LEFT JOIN roles AS r
                            ON (role = r.id)
                        LEFT JOIN user_vos AS u
                            ON (member = u.id)
                        GROUP BY
                            m.id
                        WHERE id=%s;
                        """,
                        [id]
                    )
                    row = result.fetchone()
                    return self.record_to_dict(row, result.description)
        except:
            return{"message" : "Error in member_queries get_one"}
    def create(self, member:MemberIn):
        with pool.connection() as conn:
            with conn.cursor() as db:

                result = db.execute(
                    """
                    INSERT INTO members(
                        member,
                        role
                    )
                    VALUES(
                        %s,
                        %s
                    )
                    RETURNING id;
                    """,
                    [
                        member.member.id,
                        member.role.id
                    ]
                )
        id = result.fetchone()[0]
        data = member.dict()
        return MemberOut(id=id, **data)
    
    def delete(self, id):
        with pool.connection as conn:
            with conn.cursor as db:
                result = db.execute(
                    """
                    DELETE FROM members
                    WHERE id = %s
                    """,
                    [id]
                )

    def update(self, id:int, data:MemberIn)->Union[Error,MemberOut]:
        try:
            with pool.connection as conn:
                with conn.cursor as db:
                    params = [
                        data.role.id,
                        id
                    ]
                    result = db.execute(
                        """
                        UPDATE teams
                        SET role = %s
                        WHERE id = %s
                        RETURNING id, member, team, role
                        """,
                        params
                    )
                    member = None
                    row = result.fetchone()
                    if row is not None:
                        member = {}
                        for i, column in enumerate(result.description):
                            member[column.nam] = row[i]
                    return member
        except:
            return {"message":"Error in members_queries.update"}

    def record_to_dict(self, row, description):
        member = None
        if row is not None:
            member = {}
            member_fields = [
                "id",
                "member",
                "role"
            ]
            for i, column in enumerate(description):
                if column.name in member_fields:
                    member[column.name] = row[i]
            member["id"] = member["id"]
        member_var = {}
        member_var_fields = [
            "id",
            "name",
            "user_href"
        ]
        for i, column in enumerate(description):
            if column.name in member_var_fields:
                member_var[column.name] = row[i]
        member_var["id"] = member_var["id"]

        member["member"] = member_var
        
        # team = {}
        # team_fields = [
        #     "id",
        #     "name",
        #     "type",
        #     "description",
        #     "pay_level"
        # ]
        # for i, column in enumerate(description):
        #     if column.name in team_fields:
        #         team[column.name] = row[i]
        # team["id"] = team["id"]

        # type = {}
        # type_fields = [
        #     "id",
        #     "name"
        # ]
        # for i, column in enumerate(description):
        #     if column.name in type_fields:
        #         type[column.name] = row[i]
        # type["id"] = type["id"]

        # team["type"] = type
        # pay_level = {}
        # pay_level_fields = [
        #     "id",
        #     "name",
        #     "max_members",
        #     "max_roles"
        # ]
        # for i, column in enumerate(description):
        #     if column.name in pay_level_fields:
        #         pay_level[column.name] = row[i]
        # pay_level["id"] = pay_level["id"]

        # team["pay_level"] = pay_level

        role = {}
        role_fields = [
            "id",
            "name",
            "team"
        ]
        for i, column in enumerate(description):
            if column.name in role_fields:
                role[column.name] = row[i]
        role["id"] = role["id"]

        member["role"] = role

        return member