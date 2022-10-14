steps = [
     [
        """
        CREATE TABLE sub_urls(
            id SERIAL PRIMARY KEY NOT NULL,
            url TEXT NOT NULL UNIQUE
        );
        """,
        """
        DROP TABLE sub_urls;
        """
     ],
     [
        """
        INSERT INTO sub_urls (url)
        VALUES ('http://teams:8000/api/teams/events')
        """,
        """
        """
     ]
]
