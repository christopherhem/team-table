from queries.pool import pool

class EventQueries:
    def get_table(self):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT u.id AS user_id, u.first_name AS name,
                        e.id AS event_id, e.shift_start,
                        e.shift_end, e.event_type,
                        tm.name AS team_name
                    FROM users as u
                    LEFT JOIN events AS e
                        ON (u.id=e.user_id)
                    LEFT JOIN team_vo AS tm
                        ON (tm.href=e.team_href)
                    GROUP BY
                        u.id, e.id, e.shift_start, e.shift_end,
                        e.event_type, u.first_name, tm.name
                    ORDER BY e.shift_start
                    """,
                )
                table = []
                rows= db.fetchall()
                for row in rows:
                    event = self.event_record_to_dict(row, db.description)
                    table.append(event)
                return table

    def get_event(self, event_id):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.excecute(
                    """
                    SELECT u.id AS user_id, u.first_name AS name,
                        e.id AS event_id, e.shift_start,
                        e.shift_end, e.event_type, tm.href AS team_href,
                        tm.name AS team_name
                    FROM users as u
                    LEFT JOIN events AS e
                        ON (u.id=t.user_href)
                    LEFT JOIN team_vo AS tm
                        ON (tm.href=t.team_href)
                    WHERE e.id=%s
                    """,
                    [event_id]
                )
                row = db.fetchone()
                return self.event_record_to_dict(row, db.description)

    def create_event(self, event):
        id = None
        with pool.connection() as conn:
            with conn.cursor as db:
                db.execute(
                    """
                    INSERT INTO events (
                        shift_start, shift_end, event_type, user_id, team_href
                    )
                    VALUES(%s, %s, %s, %s, %s)
                    RETURNING id
                    """,
                    [
                        event.shift_start,
                        event.shift_end,
                        event.event_type,
                        event.user_id,
                        event.team_href
                    ],
                )

                row = db.fetchone()
                id = row[0]
                if id is not None:
                    return self.get_event(id)

    def event_record_to_dict(self, row, description):
        event = None
        if row is not None:
            event = {}
            event_fields = [
                "event_id",
                "shift_start",
                "shift_end",
                "type"
            ]
            for i, column in enumerate(description):
                if column.name in event_fields:
                    event[column.name] = row[i]
            event["id"] = event["event_id"]

            user = {}
            user_fields = [
                "user_id",
                "first_name"
            ]
            for i, column in enumerate(description):
                if column.name in user_fields:
                    user[column.name] = row[i]
            user["id"] = user["user_id"]

            event["user"] = user
        return event
