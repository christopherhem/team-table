from pool import pool

class EventQueries:
    def get_table(self):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT u.href AS user_href, u.first_name AS name,
                        e.id AS event_id, e.shift_start,
                        e.shift_end, e.event_type, tm.href AS team_href,
                        tm.name AS team_name
                    FROM user_vo as u
                    LEFT JOIN events AS e
                        ON (u.href=t.user_href)
                    LEFT JOIN team_vo AS tm
                        ON (tm.href=t.team_href)
                    GROUP BY
                        t.id, t.shift_start, t.shift_end,
                        e.type, u.first_name, tm.name
                    ORDER BY t.shift_start
                    """,
                )
                table = []
                rows= db.fetchall()
                for row in rows:
                    event = self.event_record_to_dict(row, db.description)
                    table.append(event)
                return table

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
                "user_href",
                "first_name"
            ]
            for i, column in enumerate(description):
                if column.name in user_fields:
                    user[column.name] = row[i]
            user["href"] = user["user_href"]

            event["user"] = user
        return event
