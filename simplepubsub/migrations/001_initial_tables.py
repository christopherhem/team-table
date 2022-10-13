steps = [
     [
        """
        CREATE TABLE sub_urls(
            id SERIAL PRIMARY KEY NOT NULL
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
        VALUES (localhost:8100/api/teams/events)
        """,
        """
        """
     ]
]
