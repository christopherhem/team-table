from typing import List, Union
from models import PayLevelOut, Error
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

                        SELECT
                            id,
                            name,
                            max_members,
                            max_roles

                        FROM pay_levels
                        WHERE id=%s;
                        """,
                        [id]
                    )
                    return self.to_dict(result.fetchall(),result.description)
        except:
            return{"message" : "Error in team_queries PayLevelRepository.get_pay_level"}

    def get_all(self)->Union[Error, List[PayLevelOut]]:
        with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT
                            id,
                            name,
                            max_members,
                            max_roles
                        FROM pay_levels
                        """
                    )
                    return self.to_dict(result.fetchall(),result.description)

    # def delete_pay_level(self, id)->bool:
    #     try:
    #         with pool.connection() as conn:
    #             with conn.cursor() as db:
    #                 result = db.execute(
    #                     """
    #                     DELETE FROM pay_levels
    #                     WHERE id = %s
    #                     """,
    #                     [id]
    #                 )
    #         return True
    #     except:
    #         return False

    # def update_pay_level(self, id, data)->Union[Error, PayLevelOut]:
    #     with pool.connection() as conn:
    #         with conn.cursor() as db:
    #             params = [
    #                 data.name,
    #                 data.max_members,
    #                 data.max_roles,
    #                 id
    #             ]
    #             result = db.execute(
    #                 """
    #                 UPDATE pay_levels
    #                 SET name = %s,
    #                     max_membeers = %s,
    #                     max_roles = %s,
    #                 WHERE id = %s
    #                 RETURNING id, name, max_members, max_roles
    #                 """,
    #                 params,
    #             )
    #             return self.to_dict(result.fetchall(),result.description)

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
