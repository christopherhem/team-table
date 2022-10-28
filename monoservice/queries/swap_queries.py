from typing import List, Union
from models import Error
from models import ShiftSwapEventOut
from queries.pool import pool
from datetime import datetime

class SwapRepository:
    def perform_swap(self,events):
        for event in events:
            start = event.shift_start
            end = event.shift_end
            user = event.user_id
            team_name = event.team_name
            covering_start = event.availability_start
            covering_end = event.availability_end
            message = f"Your shift from {start} to {end} for {team_name} has been covered. You will need to cover a shift from {covering_start} to {covering_end} in exchange"
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        INSERT INTO notifications (user_id, message)
                        VALUES (%s, %s)
                        """,
                        [user, message]
                    )
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM shift_swap_events WHERE id = %s
                        """,
                        [event.id]
                    )
        return True

    def perform_cover(self,cover,swap):
        covermessage = f"You are now covering a shift from {cover.availability_start} to {cover.availability_end} "
        swapmessage =  f"Your shift from {swap.shift_start} to {swap.shift_end} is now covered. You will be assigned a shift to cover in return soon"
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    INSERT INTO notifications (user_id, message)
                    VALUES (%s,%s)
                    """,
                    [cover.user_id,covermessage]
                )
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    INSERT INTO notifications (user_id, message)
                    VALUES (%s,%s)
                    """,
                    [swap.user_id,swapmessage]
                )
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    DELETE FROM cover_events WHERE id = %s
                    """,
                    [cover.id]
                )
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    DELETE FROM shift_swap_events WHERE id = %s
                    """,
                    [swap.id]
                )
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    INSERT INTO cover_events (availability_start, availability_end, user_id, team_href)
                    VALUES (%s, %s, %s, %s)
                    RETURNING id, availability_start, availability_end, user_id, team_href
                    """,
                    [swap.availability_start,swap.availability_end,swap.user_id,swap.team_href]
                )
                created_cover = self.to_dict(db.fetchall(),db.description)
        return created_cover

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
