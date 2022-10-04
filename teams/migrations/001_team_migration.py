steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE teams (
            id SERIAL PRIMARY KEY NOT NULL,
            type INT NOT NULL REFERENCES team_types(id),
            level INT NOT NULL REFERENCES paylevels(id) 
        );

        CREATE TABLE team_types(
            id SERIAL PRIMARY KEY NOT NULL,
            name NOT NULL
        );
        
        CREATE TABLE event_types_team_types(
            id SERIAL PRIMARY KEY NOT NULL,
            team_type INT NOT NULL REFERENCES team_types(id),
            event_type INT NOT NULL REFERENCES event_types(id)
        );

        CREATE TABLE event_types(
            id SERIAL PRIMARY KEY NOT NULL,
            name,
            event_type_href STR UNIQUE,
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE dummy;
        """
    ],
    [
        # "Up" SQL statement
        """
        CREATE TABLE big_dummy (
            id SERIAL PRIMARY KEY NOT NULL,
            required_limited_text VARCHAR(1000) NOT NULL,
            required_unlimited_text TEXT NOT NULL,
            required_date_time TIMESTAMP NOT NULL,
            automatically_set_date_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            required_integer INTEGER NOT NULL,
            required_money MONEY NOT NULL
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE big_dummy;
        """
    ]
]
