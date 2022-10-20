from typing import List, Union
from models import PayLevelOut, Error
from queries.pool import pool

class PayLevelRepository:
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
