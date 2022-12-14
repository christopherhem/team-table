from models import EventVoIn
from queries.pool import pool


class EventVoRepository:
    def create_swap_event(self, event: EventVoIn, uid):

        href = f"http://monoservice:8000/api/table/events/{event.id}"
        team = event.team_href.split("/")[-1]
        with pool.connection() as conn:
            with conn.cursor() as db:

                result = db.execute(
                    """
                    INSERT INTO shift_swap_event_vos(
                        event_href,
                        owner,
                        team,
                        shift_start,
                        shift_end,
                        availability_start,
                        availability_end,
                        mono_id
                    )
                    VALUES(
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
                    )
                    RETURNING id, event_href,owner,team,shift_start,shift_end,availability_start,availability_end;
                    """,
                    [
                        href,
                        uid,
                        team,
                        event.shift_start,
                        event.shift_end,
                        event.availability_start,
                        event.availability_end,
                        event.id,
                    ],
                )
                return self.to_dict(result.fetchall(), result.description)

    def delete_swap_event(self, event):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    DELETE FROM shift_swap_event_vos WHERE mono_id = %s
                    """,
                    [event.id],
                )
        return True

    def get_swap_event(self, id):
        with pool.connection() as conn:
            with conn.cursor() as db:

                result = db.execute(
                    """
                    SELECT
                        id,
                        event_href,
                        owner,
                        team,
                        shift_start,
                        shift_end,
                        availability_start,
                        availability_end
                    FROM shift_swap_event_vos
                    WHERE id = %s;
                    """,
                    [id],
                )
                return self.to_dict(result.fetchall(), result.description)

    def create_cover_event(self, event: EventVoIn, uid):

        href = f"http://monoservice:8000/api/table/events/{event.id}"
        team = event.team_href.split("/")[-1]
        with pool.connection() as conn:
            with conn.cursor() as db:

                result = db.execute(
                    """
                    INSERT INTO cover_event_vos(
                        event_href,
                        owner,
                        team,
                        availability_start,
                        availability_end,
                        mono_id
                    )
                    VALUES(
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
                    )
                    RETURNING id, event_href,owner,team,availability_start,availability_end;
                    """,
                    [
                        href,
                        uid,
                        team,
                        event.availability_start,
                        event.availability_end,
                        event.id,
                    ],
                )
                return self.to_dict(result.fetchall(), result.description)

    def delete_cover_event(self, event):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    DELETE FROM cover_event_vos WHERE mono_id = %s
                    """,
                    [event.id],
                )
        return True

    def get_cover_event(self, id):
        with pool.connection() as conn:
            with conn.cursor() as db:

                result = db.execute(
                    """
                    SELECT
                        id,
                        event_href,
                        owner,
                        team,
                        availability_start,
                        availability_end
                    FROM cover_event_vos
                    WHERE id = %s;
                    """,
                    [id],
                )
            return self.to_dict(result.fetchall(), result.description)

    def get_events(self, tid):
        events = {}
        with pool.connection() as conn:
            with conn.cursor() as db:

                result = db.execute(
                    """
                    SELECT id,owner,shift_start,shift_end,availability_start,availability_end, mono_id
                    FROM shift_swap_event_vos
                    WHERE team = %s
                    """,
                    [tid],
                )
                swap_events = self.to_dict(result.fetchall(), result.description)
                if type(swap_events) != list:
                    temp = []
                    temp.append(swap_events)
                    swap_events = temp
                events["swap_events"] = swap_events

        with pool.connection() as conn:
            with conn.cursor() as db:

                result = db.execute(
                    """
                    SELECT id,owner,availability_start,availability_end, mono_id
                    FROM cover_event_vos
                    WHERE team = %s
                    """,
                    [tid],
                )
                cover_events = self.to_dict(result.fetchall(), result.description)
                if type(cover_events) != list:
                    temp = []
                    temp.append(cover_events)
                    cover_events = temp
                events["cover_events"] = cover_events
        return events

    def to_dict(self, rows, description):
        lst = []
        columns = [desc[0] for desc in description]
        for row in rows:
            item = {}
            for i in range(len(row)):
                item[columns[i]] = row[i]
            lst.append(item)
        if len(lst) == 1:
            lst = lst[0]
        return lst
