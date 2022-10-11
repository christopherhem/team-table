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
     ]
]
