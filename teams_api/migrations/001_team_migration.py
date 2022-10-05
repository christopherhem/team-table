steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE team_types(
            id SERIAL PRIMARY KEY NOT NULL,
            name STR NOT NULL
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
            name STR NOT NULL UNIQUE,
            event_type_href STR UNIQUE,
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
            name STR NOT NULL,
            max_members INT NOT NULL
            max_roles INT NOT NULL
        );
        """,
        """
        DROP TABLE pay_levels;
        """
    ]
    [
        # "Up" SQL statement
        """
        CREATE TABLE teams (
            id SERIAL PRIMARY KEY NOT NULL,
            type INT NOT NULL REFERENCES team_types(id),
            pay_level INT NOT NULL REFERENCES pay_levels(id) 
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
            name STR NOT NULL,
            user_href STR NOT NULL UNIQUE
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
            name STR NOT NULL,
            team INT NOT NULL REFERENCES teams(id),
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
            user INT NOT NULL REFERENCES user_vos(id),
            team INT NOT NULL REFERENCES teams(id),
            role INT NOT NULL REFERENCES roles(id)
        );
        """,
        """
        DROP TABLE members;
        """
    ],
    [
        """
        CREATE TABLE user_event_vos(
            id SERIAL PRIMARY KEY NOT NULL,
            event_href STR NOT NULL,
            user INT NOT NULL REFERENCES user_vos(id),
            team INT NOT NULL REFERENCES teams(id),
            event_start TIMESTAMP NOT NULL,
            event_end TIMESTAMP NOT NULL
        );
        """,
        """
        DROP TABLE user_event_vos;
        """
    ],
]
