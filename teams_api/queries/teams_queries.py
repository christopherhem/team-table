from models import *
import os
from psycopg_pool import ConnectionPool

pool = ConnectionPool(conninfo=os.environ["DATABASE_URL"])

class TeamRepository:
    def create(team:TeamIn):
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    INSERT INTO teams(
                        name,
                        type,
                        description
                    )
                    VALUES(
                        %S,
                        %S,
                        %S
                    )
                    RETURNING id;
                    """,
                    [
                        team.name,
                        team.type,
                        team.description
                        #need to set pay_level to a default value
                    ]
                )
        id = result.fetchone()[0]
        paid = result.fetchone()[4]
        data = team.dict()
        return TeamOut(id=id, pay_level = paid, **data)