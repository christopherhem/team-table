from typing import List, Union
from models import PayLevelOut, PayLevelsOut, Error
from queries.pool import pool

class PayLevelRepository:
    # def create_pay_level(self, pay_level):
    #     id = None
    #     with pool.connection() as conn:
    #         with conn.cursor() as db:

    #             result = db.execute(
    #                 """
    #                 INSERT INTO pay_levels(
    #                     p.name,
    #                     p.max_members,
    #                     p.max_roles,
    #                 )
    #                 VALUES(
    #                     %s,
    #                     %s,
    #                     %s,
    #                 )
    #                 RETURNING id;
    #                 """,
    #                 [
    #                     pay_level.name,
    #                     pay_level.type,
    #                     pay_level.description
    #                     #need to set pay_level to a default value
    #                 ]
    #             )
    #             row = result.fetchone()
    #             id = row[0]
    #     if id is not None:
    #         return self.get_pay_level(id)


    def get_pay_level(self, id)->Union[Error, PayLevelOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT pay_levels(
                            p.id,
                            p.name,
                            p.max_members,
                            p.max_roles,
                        )
                        WHERE id=%s;
                        """,
                        [id]
                    )
                    row = result.fetchone()
                    return self.team_record_to_dict(row, result.description)
        except:
            return{"message" : "Error in team_queries PayLevelRepository.get_pay_level"}

    def get_all(self)->Union[Error, PayLevelsOut]:
        with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT pay_levels(
                            p.id,
                            p.name,
                            p.max_members,
                            p.max_roles,
                        )
                        """
                    )
                    pay_levels = []
                    rows = result.fetchall()
                    for row in rows:
                        pay_level = self.pay_level_record_to_dict(row, result.description)
                        pay_levels.append(pay_level)
                    return pay_level

    def delete_pay_level(self, id):
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    DELETE FROM trucks
                    WHERE id = %s
                    """,
                    [id],
                )

    def update_pay_level(self, id, data)->Union[Error, PayLevelOut]:
        with pool.connection() as conn:
            with conn.cursor() as db:
                params = [
                    data.name,
                    data.max_members,
                    data.max_roles,
                    id
                ]
                result = db.execute(
                    """
                    UPDATE pay_levels
                    SET name = %s,
                        max_membeers = %s,
                        max_roles = %s,
                    WHERE id = %s
                    RETURNING id, name, max_members, max_roles
                    """,
                    params,
                )
                pay_level = None
                row = result.fetchone()
                if row is not None:
                    pay_level = {}
                    for i, column in enumerate(result.description):
                        pay_level[column.nam] = row[i]
                return pay_level

    def pay_level_record_to_dict(self, row, description):
        pay_level = None
        if row is not None:
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
        return pay_level
