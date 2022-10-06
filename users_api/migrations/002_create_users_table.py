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
    [
        # "Up" SQL statement
        """
        CREATE TABLE event_vo (
            id SERIAL PRIMARY KEY NOT NULL,
            shift_start TIMESTAMP NOT NULL,
            shift_end TIMESTAMP NOT NULL,
            user_id INTEGER REFERENCES users("id") ON DELETE CASCADE
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE event_vo;
        """
    ],
    [
        # "Up" SQL statement
        """
        CREATE TABLE team_vo (
            id SERIAL PRIMARY KEY NOT NULL,
            description VARCHAR(200) NOT NULL,
            max_users INTEGER NOT NULL,
            is_role_required BOOLEAN NOT NULL,
            is_approved_required BOOLEAN NOT NULL,
            picture_href VARCHAR(500),
            user_id INTEGER REFERENCES users("id") ON DELETE CASCADE
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE team_vo;
        """
    ]
]
