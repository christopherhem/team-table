import os
from psycopg_pool import ConnectionPool
pool = ConnectionPool(conninfo=os.environ["DATABASE_URL"])
from pydantic import BaseModel
from .models import Error, SubUrlOut, SubUrlIn
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
        return SubUrlOut(id,url)
    def get_subs(self)->Union[Error, List[SubUrlOut]]:
        try:
            with pool.connection() as conn:
                    with conn.cursor() as db:
                        result = db.execute(
                            """
                            SELECT sub_urls(
                                su.url
                            )
                            FROM sub_urls AS su
                            """
                        )
                        subs = []
                        rows= result.fetchall()
                        for row in rows:
                            sub = self.record_to_dict(row, result.description)
                            subs.append(sub)
                        return subs
        except:
            return{"message":"Error in SubQueries.get_subs"}
    def record_to_dict(self,row, desc):
        sub = None
        if row is not None:
            sub = {}
            sub_fields = [
                'id', 
                'url'
            ]
            for i, column in enumerate(desc):
                if column.name in sub_fields:
                    sub[column.name] = row[i]
            sub["id"] = sub["id"]
        return sub
