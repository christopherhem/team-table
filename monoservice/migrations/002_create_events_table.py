steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE teams_vo (
            id SERIAL PRIMARY KEY NOT NULL,
            team_href VARCHAR(50) NOT NULL UNIQUE,
            name VARCHAR(50) NOT NULL UNIQUE,
            description TEXT
        );

        """,
        # "Down" SQL statement
        """
        DROP TABLE teams_vo;
        """
    ],
    [
        """
        CREATE TABLE teams_users_relations(
            id SERIAL PRIMARY KEY NOT NULL,
            team_id INT NOT NULL REFERENCES teams_vo(id),
            user_id INT NOT NULL REFERENCES users(id),
            unique_string VARCHAR(100) NOT NULL UNIQUE
        );
        """,
        """
        DROP TABLE teams_user_relations;
        """
    ],
    [
        """
        CREATE TABLE event_types (
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(50) NOT NULL
        )
        """,
        """
        DROP TABLE event_types
        """
    ],
    [
        """
        INSERT INTO event_types (name) VALUES
        ('cover_events'),
        ('shift_swap_events');
        """,
        """
        """
    ],
    [
        # "Up" SQL statement
        """
        CREATE TABLE cover_events(
            id SERIAL PRIMARY KEY NOT NULL,
            availability_start TIMESTAMP NOT NULL,
            availability_end TIMESTAMP NOT NULL,
            user_id INTEGER REFERENCES users("id") ON DELETE CASCADE,
            team_href VARCHAR(50) REFERENCES teams_vo("team_href") ON DELETE CASCADE
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE cover_events;
        """
    ],
    [
        # "Up" SQL statement
        """
        CREATE TABLE shift_swap_events(
            id SERIAL PRIMARY KEY NOT NULL,
            shift_start TIMESTAMP NOT NULL,
            shift_end TIMESTAMP NOT NULL,
            availability_start TIMESTAMP NOT NULL,
            availability_end TIMESTAMP NOT NULL,
            user_id INTEGER REFERENCES users("id") ON DELETE CASCADE,
            team_href VARCHAR(50) REFERENCES teams_vo("team_href") ON DELETE CASCADE
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE shift_swap_events;
        """
    ]

]
