import os
from psycopg_pool import ConnectionPool

pool = ConnectionPool(conninfo=os.environ["DATABASE_URL"])

class UserQueries:
    def get_all_users(self):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT id, username, password, first_name, last_name, email, phone_number, profile_picture_href
                    FROM users;
                    """
                )

                users = []
                for row in cur.fetchall():
                    record = {}
                    for i, column in enumerate(cur.description):
                        record[column.username] = row[i]
                    users.append(record)
            
                return users