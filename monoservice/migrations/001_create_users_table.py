steps = [
     [
        # "Up" SQL statement
        """
        CREATE TABLE users (
            id SERIAL PRIMARY KEY NOT NULL,
            username VARCHAR(30) NOT NULL,
            password  VARCHAR(30) NOT NULL,
            first_name VARCHAR(30) NOT NULL,
            last_name VARCHAR(30) NOT NULL,
            email VARCHAR(30) NOT NULL,
            phone_number VARCHAR(30),
            profile_picture_href VARCHAR(500)
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE users;
        """
    ],
]
