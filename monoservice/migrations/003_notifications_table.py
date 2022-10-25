steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE notifications(
            id SERIAL PRIMARY KEY NOT NULL,
            user_id INT REFERENCES users(id),
            message VARCHAR(250),
            seen BOOLEAN DEFAULT FALSE
        );

        """,
        # "Down" SQL statement
        """
        DROP TABLE notifications;
        """
    ],
]