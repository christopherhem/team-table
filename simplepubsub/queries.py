import os
from psycopg_pool import ConnectionPool
pool = ConnectionPool(conninfo=os.environ["DATABASE_URL"])
from pydantic import BaseModel
from models import Error, SubUrlOut, SubUrlIn
from typing import  List, Optional, Union

class SubQueries:
    def add_sub(
        self,
        sub:SubUrlIn,
)->Union[Error, SubUrlOut]:
        with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO sub_urls(
                            url
                        )
                        VALUES(
                            %s
                        )
                        RETURNING id;
                        """,
                        [sub.url]
                    )
                    id = result.fetchone()[0]
        url = sub.dict()
        return SubUrlOut(id = id,url = url)
    def get_subs(self)->Union[Error, List[SubUrlOut]]:
        try:
            print("sub call initiated")
            with pool.connection() as conn:
                    with conn.cursor() as db:
                        result = db.execute(
                            """
                            SELECT id, url
                            FROM sub_urls
                            """
                        )
                        return self.to_dict(result.fetchall(),result.description)
        except:
            return{"message":"Error in SubQueries.get_subs"}

    def to_dict(self,rows,description):
        lst = []
        columns = [desc[0] for desc in description]
        for row in rows:
            item = {}
            for i in range(len(row)):
                item[columns[i]]=row[i] 
            lst.append(item)
        return lst
