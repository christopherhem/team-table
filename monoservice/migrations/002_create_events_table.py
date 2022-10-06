steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE team_vo (
            href VARCHAR(50) NOT NULL UNIQUE,
            name VARCHAR(50) NOT NULL UNIQUE
        );

        """,
        # "Down" SQL statement
        """
        DROP TABLE teams_vo;
        """
    ],
    [
        # "Up" SQL statement
        """
        CREATE TABLE events (
            id SERIAL PRIMARY KEY NOT NULL,
            event_type TEXT NOT NULL check(event_type = 'shift'),
            shift_start TIMESTAMP NOT NULL,
            shift_end TIMESTAMP NOT NULL,
            user_id INTEGER REFERENCES users("id") ON DELETE CASCADE,
            team_href VARCHAR(50) REFERENCES team_vo("href") ON DELETE CASCADE
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE event;
        """
    ]
]
