steps = [
     [
        """
        CREATE TABLE team_sub_urls(
            id SERIAL PRIMARY KEY NOT NULL,
            url TEXT NOT NULL UNIQUE
        );
        """,
        """
        DROP TABLE team_sub_urls;
        """
     ],
     [
        """
        INSERT INTO team_sub_urls (url)
        VALUES ('http://teams:8000/api/teams/events/')
        """,
        """
        """
     ]
]
