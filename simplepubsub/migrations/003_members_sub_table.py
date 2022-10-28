steps = [
    [
        """
        CREATE TABLE member_sub_urls(
            id SERIAL PRIMARY KEY NOT NULL,
            url TEXT NOT NULL UNIQUE
        );
        """,
        """
        DROP TABLE member_sub_urls;
        """,
    ],
    [
        """
        INSERT INTO member_sub_urls (url)
        VALUES ('http://monoservice:8000/api/main/teams/members/')
        """,
        """
        """,
    ],
]
