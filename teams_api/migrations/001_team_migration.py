steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE team_types(
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(50) NOT NULL
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE team_types;
        """
    ],
    [
        """
        CREATE TABLE event_types(
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(50) NOT NULL UNIQUE,
            event_type_href VARCHAR(200) UNIQUE
        );
        """,
        """
        DROP TABLE event_types;
        """
    ],
    [
        """
        CREATE TABLE event_types_team_types(
            id SERIAL PRIMARY KEY NOT NULL,
            team_type INT NOT NULL REFERENCES team_types(id),
            event_type INT NOT NULL REFERENCES event_types(id)
        );
        """,
        """
        DROP TABLE event_types_team_types;
        """
    ],
    [
        """
        CREATE TABLE pay_levels(
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(50) NOT NULL,
            max_members INT NOT NULL,
            max_roles INT NOT NULL
        );
        """,
        """
        DROP TABLE pay_levels;
        """
    ],
    [
        # "Up" SQL statement
        """
        CREATE TABLE teams (
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(50) NOT NULL,
            type INT NOT NULL REFERENCES team_types(id),
            description TEXT,
            pay_level INT REFERENCES pay_levels(id)
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE teams;
        """
    ],
    [
        """
        CREATE TABLE user_vos(
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(50) NOT NULL,
            user_href VARCHAR(200) NOT NULL UNIQUE
        );
        """,
        """
        DROP TABLE user_vos;
        """
    ],
    [
        """
        CREATE TABLE roles(
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(50) NOT NULL,
            team INT NOT NULL REFERENCES teams(id)
        );
        """,
        """
        DROP TABLE roles;
        """
    ],
    [
        """
        CREATE TABLE permissions(
            id SERIAL PRIMARY KEY NOT NULL,
            role INT NOT NULL REFERENCES roles(id),
            approve_swaps BOOL NOT NULL,
            invite_members BOOL NOT NULL,
            add_roles BOOL NOT NULL

        );
        """,
        """
        DROP TABLE permissions;
        """
    ],
    [
        """
        CREATE TABLE members(
            id SERIAL PRIMARY KEY NOT NULL,
            user INT NOT NULL,
            role INT NOT NULL REFERENCES roles(id)
        );
        """,
        """
        DROP TABLE members;
        """
    ],
    [
        # "Up" SQL statement
        """
        CREATE TABLE cover_event_vos(
            id SERIAL PRIMARY KEY NOT NULL,
            event_href VARCHAR(100) NOT NULL
            owner INTEGER REFERENCES users("id") ON DELETE CASCADE,
            team VARCHAR(50) REFERENCES team_vo("href") ON DELETE CASCADE
            availability_start TIMESTAMP NOT NULL,
            availability_end TIMESTAMP NOT NULL,
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
        CREATE TABLE shift_swap_event_vos(
            id SERIAL PRIMARY KEY NOT NULL,
            event_href VARCHAR(100) NOT NULL
            owner INTEGER REFERENCES users("id") ON DELETE CASCADE,
            team VARCHAR(50) REFERENCES team_vo("href") ON DELETE CASCADE,
            shift_start TIMESTAMP NOT NULL,
            shift_end TIMESTAMP NOT NULL,
            availability_start TIMESTAMP NOT NULL,
            availability_end TIMESTAMP NOT NULL
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE shift_swap_events;
        """
    ]
]
