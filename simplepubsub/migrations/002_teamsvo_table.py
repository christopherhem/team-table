steps = [
     [
        """
        CREATE TABLE mono_sub_urls(
            id SERIAL PRIMARY KEY NOT NULL,
            url TEXT NOT NULL UNIQUE
        );
        """,
        """
        DROP TABLE mono_sub_urls;
        """
     ],
     [
        """
        INSERT INTO mono_sub_urls (url)
        VALUES ('http://monoservice:8000/api/main/teams/')
        """,
        """
        """
     ]
]
