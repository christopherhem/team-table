from queries.pool import pool

import requests

class EventQueries:
    def get_table(self):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT u.id AS user_id, u.first_name AS name,
                        e.availability_start,
                        e.availability_end, s.shift_start, s.shift_end,
                        s.availability_start, s.availability_end
                        tm.name AS team_name
                    FROM users as u
                    LEFT JOIN cover_events AS e
                        ON (u.id=e.user_id)
                    LEFT JOIN shift_swap_events as s
                        ON (u.id=s.user_id)
                    LEFT JOIN team_vo AS tm
                        ON (tm.href=e.team_href)
                    GROUP BY
                        u.id,
                        u.first_name, tm.name,
                    ORDER BY tm.name
                    """,
                )
                table = []
                rows= db.fetchall()
                for row in rows:
                    event = self.shift_swap_event_record_to_dict(row, db.description)
                    table.append(event)
                return table

    def get_cover_event(self, id):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.excecute(
                    """
                    SELECT u.id AS user_id, u.first_name AS name,
                        e.availability_start,
                        e.availability_end,
                        tm.name AS team_name
                    FROM users as u
                    LEFT JOIN cover_events AS e
                        ON (u.id=e.user_id)
                    LEFT JOIN team_vo AS tm
                        ON (tm.href=t.team_href)
                    WHERE e.id=%s
                    """,
                    [id]
                )
                row = db.fetchone()
                return self.cover_event_record_to_dict(row, db.description)

    def get_shift_swap_event(self, id):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.excecute(
                    """
                    SELECT u.id AS user_id, u.first_name AS name,
                        s.availability_start,
                        s.availability_end, s.shift_start,
                        s.shift_end, tm.name AS team_name
                    FROM users as u
                    LEFT JOIN shift_swap_events AS s
                        ON (u.id=s.user_id)
                    LEFT JOIN team_vo AS tm
                        ON (tm.href=t.team_href)
                    WHERE e.id=%s
                    """,
                    [id]
                )
                row = db.fetchone()
                return self.shift_swap_event_record_to_dict(row, db.description)

    def create_cover_event(self, cover_event):
        id = None
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    INSERT INTO cover_events (
                        availability_start, availability_end, user_id, team_href
                    )
                    VALUES(%s, %s, %s, %s)
                    RETURNING id
                    """,
                    [
                        cover_event.availability_start,
                        cover_event.availability_end,
                        cover_event.user_id,
                        cover_event.team_href
                    ],
                )

                row = db.fetchone()
                id = row[0]
                if id is not None:
                    return self.get_cover_event(id)

    def create_shift_swap_event(self, shift_swap_event):
        id = None
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    INSERT INTO shift_swap_events (
                        shift_start, shift_end
                        availability_start, availability_end,
                        user_id, team_href,
                    )
                    VALUES(%s, %s, %s, %s)
                    RETURNING id
                    """,
                    [
                        shift_swap_event.shift_start,
                        shift_swap_event.shift_end,
                        shift_swap_event.availability_start,
                        shift_swap_event.availability_end,
                        shift_swap_event.user_id,
                        shift_swap_event.team_href
                    ],
                )

                row = db.fetchone()
                id = row[0]
                if id is not None:
                    return self.get_shift_swap_event(id)

    def delete_cover_event(self, id):
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    DELETE FROM cover_events
                    WHERE id = %s
                    """,
                    [id]
                )

    def delete_shift_swap_event(self, id):
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    DELETE FROM shift_swap_events
                    WHERE id = %s
                    """,
                    [id]
                )

    def update_cover_event(self, id, data):
        with pool.connection() as conn:
            with conn.cursor() as db:
                params = [
                    data.availability_start,
                    data.availability_end,
                    id
                ]
                result = db.excute(
                    """
                    UPDATE cover_events
                    SET availability_start = %s,
                        availability_end = %s
                    WHERE id = %s
                    RETURNING id, availability_start, availability_end, user_id, team_href
                    """,
                    params
                )

                row = result.fetchone()
                return self.cover_event_record_to_dict(row, result.description)

    def update_shift_swap_event(self, id, data):
        with pool.connection() as conn:
            with conn.cursor() as db:
                params = [
                    data.shift_start,
                    data.shift_end,
                    data.availability_start,
                    data.availability_end,
                    id
                ]
                result = db.excute(
                    """
                    UPDATE cover_events
                    SET shift_start = %s
                        shift_end = %s
                        availability_start = %s,
                        availability_end = %s
                    WHERE id = %s
                    RETURNING id, availability_start, availability_end, user_id, team_href
                    """,
                    params
                )

                row = result.fetchone()
                return self.shift_swap_event_record_to_dict(row, result.description)

    def get_event_types(self):
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        SELECT id, name
                        FROM event_types;
                        """
                    )
                    event_types = []
                    rows = db.fetchall()
                    for row in rows:
                        event_type = self.event_type_record_to_dict(row, db.description)
                        event_types.append(event_type)
                    return event_types
        except Exception as e:
            return {"message": str(e)}

    def get_event_type(self, id):
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        SELECT id, name
                        FROM event_types
                        WHERE id=%s
                        """,
                        [id],
                    )

                    row = db.fetchone()
                    return self.event_type_record_to_dict(row, db.description)

        except Exception as e:
            return {"message": str(e)}

    def event_type_record_to_dict(self, row, description):
        event_type = None
        if row is not None:
            event_type = {}
            event_type_fields = ["id", "name"]
            for i, column in enumerate(description):
                if column.name in event_type_fields:
                    event_type[column.name] = row[i]
            event_type["id"] = event_type["id"]
        return event_type

    def cover_event_record_to_dict(self, row, description):
        event = None
        if row is not None:
            event = {}
            event_fields = [
                "id",
                "availability_start",
                "availability_end",
                "user_id",
                "team_href"
            ]
            for i, column in enumerate(description):
                if column.name in event_fields:
                    event[column.name] = row[i]
            event["id"] = event["id"]

            user = {}
            user_fields = [
                "id",
                "first_name"
            ]
            for i, column in enumerate(description):
                if column.name in user_fields:
                    user[column.name] = row[i]
            user["id"] = user["id"]

            event["user_id"] = user

            team = {}
            team_fields = [
                "id",
                "href",
                "name"
            ]
            for i, column in enumerate(description):
                if column.name in team_fields:
                    team[column.name] = row[i]
            team["id"] = team["id"]

            event["team_href"] = team
        return event

    def shift_swap_event_record_to_dict(self, row, description):
        event = None
        if row is not None:
            event = {}
            event_fields = [
                "id",
                "shift_start",
                "shift_end"
                "availability_start",
                "availability_end",
                "user_id",
                "team_href"
            ]
            for i, column in enumerate(description):
                if column.name in event_fields:
                    event[column.name] = row[i]
            event["id"] = event["id"]

            user = {}
            user_fields = [
                "id",
                "first_name"
            ]
            for i, column in enumerate(description):
                if column.name in user_fields:
                    user[column.name] = row[i]
            user["id"] = user["id"]

            event["user_id"] = user

            team = {}
            team_fields = [
                "id",
                "href",
                "name"
            ]
            for i, column in enumerate(description):
                if column.name in team_fields:
                    team[column.name] = row[i]
            team["id"] = team["id"]

            event["team_href"] = team
        return event
