from queries.pool import pool
from models import (
    CoverEventIn,
    CoverEventUpdateIn,
    ShiftSwapEventIn,
)


class EventQueries:
    def get_cover_event_table(self):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT e.id, e.availability_start,
                        e.availability_end, e.team_href,
                        e.user_id
                    FROM cover_events as e
                    LEFT JOIN users AS u
                        ON (u.id=e.user_id)
                    LEFT JOIN teams_vo AS tm
                        ON (tm.team_href=e.team_href)
                    GROUP BY e.id, e.availability_start,
                        e.availability_end, e.team_href,
                        e.user_id
                    ORDER BY e.availability_start
                    """,
                )
                events =  self.to_dict(db.fetchall(), db.description)
        if type(events) != list:
            temp = []
            temp.append(events)
            events = temp
        for dic in events:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT name
                        FROM teams_vo
                        WHERE team_href = %s

                        """,
                        [dic['team_href']]
                    )
                    dic['team_name'] = str(result.fetchone()).strip("(',)")
        return events

    def get_shift_swap_event_table(self):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT e.id, e.shift_start, e.shift_end,
                        e.availability_start, e.availability_end,
                        e.team_href, e.user_id
                    FROM shift_swap_events as e
                    LEFT JOIN users AS u
                        ON (u.id=e.user_id)
                    LEFT JOIN teams_vo AS tm
                        ON (tm.team_href=e.team_href)
                    GROUP BY e.id, e.shift_start, e.shift_end,
                        e.availability_start, e.availability_end,
                        e.team_href, e.user_id
                    ORDER BY e.shift_start
                    """,
                )
                events =  self.to_dict(db.fetchall(), db.description)
        if type(events) != list:
            temp = []
            temp.append(events)
            events = temp
        for dic in events:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT name
                        FROM teams_vo
                        WHERE team_href = %s

                        """,
                        [dic['team_href']]
                    )
                    dic['team_name'] = str(result.fetchone()).strip("(',)")
        return events

    def get_user_cover_events(self, user):
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    SELECT id, availability_start,
                        availability_end, user_id,
                        team_href
                    FROM cover_events
                    WHERE user_id = %s;
                    """,
                    [user["id"]]
                )
                cover_events =  self.to_dict(result.fetchall(), result.description)
        if type(cover_events) != list:
            temp = []
            temp.append(cover_events)
            cover_events = temp
        for dic in cover_events:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT name
                        FROM teams_vo
                        WHERE team_href = %s

                        """,
                        [dic['team_href']]
                    )
                    dic['team_name'] = str(result.fetchone()).strip("(',)")

        return cover_events


    def get_user_shift_swap_events(self, user):
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    SELECT e.id, e.shift_start, e.shift_end,
                        e.availability_start, e.availability_end,
                        e.user_id, e.team_href
                    FROM shift_swap_events as e
                    WHERE e.user_id = %s;
                    """,
                    [user["id"]]
                )
                events =  self.to_dict(result.fetchall(), result.description)
        if type(events) != list:
            temp = []
            temp.append(events)
            events = temp
        for dic in events:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT name
                        FROM teams_vo
                        WHERE team_href = %s

                        """,
                        [dic['team_href']]
                    )
                    dic['team_name'] = str(result.fetchone()).strip("(',)")
        return events

    def get_cover_event(self, id):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT e.id, e.availability_start,
                        e.availability_end, e.team_href,
                        e.user_id
                    FROM cover_events as e
                    LEFT JOIN users AS u
                        ON (u.id=e.user_id)
                    LEFT JOIN teams_vo AS tm
                        ON (tm.href=e.team_href)
                    WHERE e.id=%s
                    """,
                    [id]
                )
                return self.to_dict(db.fetchall(), db.description)

    def get_shift_swap_event(self, id):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT e.id, e.shift_start,
                        e.shift_end, e.availability_start,
                        e.availability_end, e.team_href,
                        e.user_id
                    FROM shift_swap_events as e
                    LEFT JOIN users AS u
                        ON (u.id=e.user_id)
                    LEFT JOIN teams_vo AS tm
                        ON (tm.href=e.team_href)
                    WHERE e.id=%s
                    """,
                    [id]
                )
                return self.to_dict(db.fetchall(), db.description)

    def create_cover_event(self, cover_event: CoverEventIn, user):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    INSERT INTO cover_events (
                        availability_start, availability_end, user_id, team_href
                    )
                    VALUES(%s, %s, %s, %s)
                    RETURNING id, availability_start, availability_end, user_id, team_href
                    """,
                    [
                        cover_event.availability_start,
                        cover_event.availability_end,
                        user["id"],
                        cover_event.team_href
                    ],
                )
                event =  self.to_dict(db.fetchall(), db.description)

        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT name
                    FROM teams_vo
                    WHERE team_href = %s
                    """,
                    [event['team_href']]
                )
                event['team_name'] = str(db.fetchone()).strip("(',)")
        return event

    def create_shift_swap_event(self, shift_swap_event: ShiftSwapEventIn, user):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    INSERT INTO shift_swap_events (
                        shift_start, shift_end,
                        availability_start, availability_end,
                        user_id, team_href
                    )
                    VALUES(%s, %s, %s, %s, %s, %s)
                    RETURNING id, shift_start, shift_end, availability_start, availability_end, user_id, team_href
                    """,
                    [
                        shift_swap_event.shift_start,
                        shift_swap_event.shift_end,
                        shift_swap_event.availability_start,
                        shift_swap_event.availability_end,
                        user["id"],
                        shift_swap_event.team_href
                    ],
                )
                event = self.to_dict(db.fetchall(), db.description)
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT name
                    FROM teams_vo
                    WHERE team_href = %s
                    """,
                    [event['team_href']]
                )
                event['team_name'] = str(db.fetchone()).strip("(',)")
        return event

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

    def update_cover_event(self, id, data: CoverEventUpdateIn):
        with pool.connection() as conn:
            with conn.cursor() as db:
                params = [
                    data.availability_start,
                    data.availability_end,
                    id
                ]
                result = db.execute(
                    """
                    UPDATE cover_events
                    SET availability_start = %s,
                        availability_end = %s
                    WHERE id = %s
                    RETURNING id, availability_start, availability_end, user_id, team_href
                    """,
                    params
                )

                event =  self.to_dict(db.fetchall(), db.description)

        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT name
                    FROM teams_vo
                    WHERE team_href = %s
                    """,
                    [event['team_href']]
                )
                event['team_name'] = str(db.fetchone()).strip("(',)")
        return event

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
                result = db.execute(
                    """
                    UPDATE shift_swap_events
                    SET shift_start = %s,
                        shift_end = %s,
                        availability_start = %s,
                        availability_end = %s
                    WHERE id = %s
                    RETURNING id, shift_start, shift_end, availability_start, availability_end, user_id, team_href
                    """,
                    params
                )

                event =  self.to_dict(db.fetchall(), db.description)

        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT name
                    FROM teams_vo
                    WHERE team_href = %s
                    """,
                    [event['team_href']]
                )
                event['team_name'] = str(db.fetchone()).strip("(',)")
        return event

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
                    return self.to_dict(db.fetchall(), db.description)
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

                    return self.to_dict(db.fetchall(), db.description)

        except Exception as e:
            return {"message": str(e)}



    def to_dict(self,rows,description):
            lst = []
            columns = [desc[0] for desc in description]
            for row in rows:
                item = {}
                for i in range(len(row)):
                    item[columns[i]]=row[i]
                lst.append(item)
            if len(lst) == 1:
                lst = lst[0]
            return lst
