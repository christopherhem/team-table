steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE user_vo (
            id SERIAL PRIMARY KEY NOT NULL,
            username VARCHAR(30) NOT NULL,
            password  VARCHAR(30) NOT NULL,
            first_name VARCHAR(30) NOT NULL,
            last_name VARCHAR(30) NOT NULL,
            email VARCHAR(30) NOT NULL,
            phone_number VARCHAR(30) NOT NULL,
            profile_picture VARCHAR(30) NOT NULL
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE user_vo;
        """
    ],
    [
        # "Up" SQL statement
        """
        CREATE TABLE event (
            id SERIAL PRIMARY KEY NOT NULL,
            shift_start TIMESTAMP NOT NULL,
            shift_end TIMESTAMP NOT NULL,
            user_id INTEGER REFERENCES user_vo("id") ON DELETE CASCADE
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE event;
        """
    ]
]
