steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE team_types(
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(50) NOT NULL UNIQUE
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE team_types;
        """
    ],
    [
        """
        INSERT INTO team_types (name)
        VALUES ('shift_swapping_team')
        """,
        """
        """
    ],
    [
        """
        CREATE TABLE event_types(
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(50) NOT NULL UNIQUE,
            table_name VARCHAR(50) NOT NULL UNIQUE
        );
        """,
        """
        DROP TABLE event_types;
        """
    ],
    [
        """
        INSERT INTO event_types(name,table_name)
        VALUES('shift_swap_events','shift_swap_event_vos')
        """,
        """
        """
    ],
    [
        """
        INSERT INTO event_types(name,table_name)
        VALUES('cover_events','cover_event_vos')
        """,
        """
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
        INSERT INTO event_types_team_types (team_type, event_type)
        VALUES (1,1)
        """,
        """
        """
    ],
    [
       """
        INSERT INTO event_types_team_types (team_type, event_type)
        VALUES (1,2)
        """,
        """
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
        """
        INSERT INTO pay_levels(name,max_members,max_roles)
        VALUES('Free',10,3)
        """,
        """
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
    # [
    #     """
    #     CREATE TABLE user_vos(
    #         id SERIAL PRIMARY KEY NOT NULL,
    #         name VARCHAR(50) NOT NULL,
    #         user_href VARCHAR(200) NOT NULL UNIQUE
    #     );
    #     """,
    #     """
    #     DROP TABLE user_vos;
    #     """
    # ],
    [
        """
        CREATE TABLE roles(
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(50) NOT NULL,
            team INT NOT NULL REFERENCES teams(id),
            can_invite BOOL,
            can_approve BOOL
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
            member_username VARCHAR(50) NOT NULL,
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
            event_href VARCHAR(100) NOT NULL,
            owner VARCHAR(50),
            team INT REFERENCES teams(id) ON DELETE CASCADE,
            availability_start TIMESTAMP NOT NULL,
            availability_end TIMESTAMP NOT NULL,
            mono_id INT NOT NULL UNIQUE
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE cover_event_vos;
        """
    ],
    [
        # "Up" SQL statement
        """
        CREATE TABLE shift_swap_event_vos(
            id SERIAL PRIMARY KEY NOT NULL,
            event_href VARCHAR(100) NOT NULL,
            owner VARCHAR(50),
            team INT REFERENCES teams(id) ON DELETE CASCADE,
            shift_start TIMESTAMP NOT NULL,
            shift_end TIMESTAMP NOT NULL,
            availability_start TIMESTAMP NOT NULL,
            availability_end TIMESTAMP NOT NULL,
            mono_id INT NOT NULL UNIQUE
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE shift_swap_event_vos;
        """
    ]
]
