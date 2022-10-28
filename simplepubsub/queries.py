import os
from psycopg_pool import ConnectionPool
pool = ConnectionPool(conninfo=os.environ["DATABASE_URL"])
from models import Error, SubUrlOut, SubUrlIn
from typing import  List,  Union

class TeamSubQueries:
    def add_sub(
        self,
        sub:SubUrlIn,
)->Union[Error, SubUrlOut]:
        with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO team_sub_urls(
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
            with pool.connection() as conn:
                    with conn.cursor() as db:
                        result = db.execute(
                            """
                            SELECT id, url
                            FROM team_sub_urls
                            """
                        )
                        return self.to_dict(result.fetchall(),result.description)
        except:
            return{"message":"Error in TeamSubQueries.get_subs"}

    def to_dict(self,rows,description):
        lst = []
        columns = [desc[0] for desc in description]
        for row in rows:
            item = {}
            for i in range(len(row)):
                item[columns[i]]=row[i]
            lst.append(item)
        return lst



class MainSubQueries:
    def add_sub(
        self,
        sub:SubUrlIn,
)->Union[Error, SubUrlOut]:
        with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO mono_sub_urls(
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
            with pool.connection() as conn:
                    with conn.cursor() as db:
                        result = db.execute(
                            """
                            SELECT id, url
                            FROM mono_sub_urls
                            """
                        )
                        return self.to_dict(result.fetchall(),result.description)
        except:
            return{"message":"Error in MainSubQueries.get_subs"}

    def to_dict(self,rows,description):
        lst = []
        columns = [desc[0] for desc in description]
        for row in rows:
            item = {}
            for i in range(len(row)):
                item[columns[i]]=row[i]
            lst.append(item)
        return lst


class MemberSubQueries:
    def add_sub(
        self,
        sub:SubUrlIn,
)->Union[Error, SubUrlOut]:
        with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO member_sub_urls(
                            url
                        )
                        VALUES(
                            %s
                        )
                        RETURNING id, url;
                        """,
                        [sub.url]
                    )
                    id = result.fetchone()[0]
        url = sub.dict()
        return SubUrlOut(id = id,url = url)
    def get_subs(self)->Union[Error, List[SubUrlOut]]:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    SELECT id, url
                    FROM member_sub_urls
                    """
                )
                urls = self.to_dict(result.fetchall(),result.description)
        if type(urls) != list:
            temp = []
            temp.append(urls)
            urls = temp
        return urls

    def to_dict(self,rows,description):
        lst = []
        columns = [desc[0] for desc in description]
        for row in rows:
            item = {}
            for i in range(len(row)):
                item[columns[i]]=row[i]
            lst.append(item)
        return lst
