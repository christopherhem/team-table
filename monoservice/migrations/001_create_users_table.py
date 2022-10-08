steps = [
     [
        # "Up" SQL statement
        """
        CREATE TABLE users (
            id SERIAL PRIMARY KEY NOT NULL,
            email VARCHAR(200) NOT NULL,
            username VARCHAR(250) NOT NULL,
            hashed_password  VARCHAR(300) NOT NULL,
            first_name VARCHAR(300) NOT NULL,
            last_name VARCHAR(300) NOT NULL,
            phone_number VARCHAR(30),
            profile_picture_href VARCHAR(700)
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE users;
        """
    ],
]
