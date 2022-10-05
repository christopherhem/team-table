from psycopg_pool import ConnectionPool


class UsersQueries:
    def create_user(
        self,
        username: str,
        password: str,
        first_name: str,
        last_name: str,
        email: str,
    );
        with pool.connection() as conn:
            with conn.cursor() as db:
                try:
                    db.execute(
                        """
                        INSERT INTO users (username, password, email, first_name, last_name)
                        """
                    )