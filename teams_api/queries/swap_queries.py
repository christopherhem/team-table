from queries.pool import pool
from datetime import datetime as datetime


class SwapRepository:
    def get_valid_swaps(self, user):
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                SELECT id, event_href, owner, team, shift_start, shift_end, availability_start, availability_end, mono_id
                FROM shift_swap_event_vos
                WHERE owner = %s
                """,
                    [user["account"]["username"]],
                )
                user_swaps = self.to_dict(result.fetchall(), result.description)
        if type(user_swaps) != list:
            temp = []
            temp.append(user_swaps)
            user_swaps = temp
        final = []
        for swap in user_swaps:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, event_href, owner, team, shift_start, shift_end, availability_start, availability_end, mono_id
                        FROM shift_swap_event_vos
                        WHERE team = %s AND owner != %s
                        """,
                        [swap["team"], user["account"]["username"]],
                    )
                    team_events = self.to_dict(result.fetchall(), result.description)
            if type(team_events) != list:
                temp = []
                temp.append(team_events)
                team_events = temp
            valid_swap_list = []
            for event in team_events:

                # the less than/= values here may need to be swapped
                if (
                    event["availability_start"] <= swap["shift_start"]
                    and event["availability_end"] >= swap["shift_end"]
                ):
                    if (
                        swap["availability_start"] <= event["shift_start"]
                        and swap["availability_end"] >= event["shift_end"]
                    ):
                        valid_swap_list.append(event)
            partial_out = {"user_event": swap, "valid_swaps": valid_swap_list}
            final.append(partial_out)
        if type(final) != list:
            temp = []
            temp.append(final)
            final = temp
        finaldict = {}
        finaldict["swaps"] = final
        return finaldict

    def get_user_covers(self, user):
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                SELECT id, event_href, owner, team, availability_start, availability_end, mono_id
                FROM cover_event_vos
                WHERE owner = %s
                """,
                    [user["account"]["username"]],
                )
                user_covers = self.to_dict(result.fetchall(), result.description)
        if type(user_covers) != list:
            temp = []
            temp.append(user_covers)
            user_covers = temp
        final = []
        for cover in user_covers:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, event_href, owner, team, shift_start, shift_end, availability_start, availability_end, mono_id
                        FROM shift_swap_event_vos
                        WHERE team = %s AND owner != %s
                        """,
                        [cover["team"], user["account"]["username"]],
                    )
                    team_events = self.to_dict(result.fetchall(), result.description)
            if type(team_events) != list:
                temp = []
                temp.append(team_events)
                team_events = temp
            valid_swap_list = []
            for event in team_events:

                # the less than/= values here may need to be swapped
                if (
                    cover["availability_start"] <= event["shift_start"]
                    and cover["availability_end"] >= event["shift_end"]
                ):
                    valid_swap_list.append(event)
            partial_out = {"user_event": cover, "valid_swaps": valid_swap_list}
            final.append(partial_out)
        if type(final) != list:
            temp = []
            temp.append(final)
            final = temp
        finaldict = {}
        finaldict["user_covers"] = final
        return finaldict

    def get_valid_covers(self, user):
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                SELECT id, event_href, owner, team, shift_start, shift_end, availability_start, availability_end, mono_id
                FROM shift_swap_event_vos
                WHERE owner = %s
                """,
                    [user["account"]["username"]],
                )
                user_swaps = self.to_dict(result.fetchall(), result.description)
        if type(user_swaps) != list:
            temp = []
            temp.append(user_swaps)
            user_swaps = temp
        final = []
        for swap in user_swaps:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, event_href, owner, team, availability_start, availability_end, mono_id
                        FROM cover_event_vos
                        WHERE team = %s AND owner != %s
                        """,
                        [swap["team"], user["account"]["username"]],
                    )
                    team_events = self.to_dict(result.fetchall(), result.description)
            if type(team_events) != list:
                temp = []
                temp.append(team_events)
                team_events = temp
            valid_swap_list = []
            for event in team_events:
                # the less than/= values here may need to be swapped
                if (
                    event["availability_start"] <= swap["shift_start"]
                    and event["availability_end"] >= swap["shift_end"]
                ):
                    valid_swap_list.append(event)
            partial_out = {"user_event": swap, "valid_swaps": valid_swap_list}
            final.append(partial_out)
        if type(final) != list:
            temp = []
            temp.append(final)
            final = temp
        finaldict = {}
        finaldict["covers_for_user"] = final
        return finaldict

    def get_swaps_for_single_swap(self, user, event_id):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT id, event_href, owner, team, shift_start, shift_end, availability_start, availability_end, mono_id
                    FROM shift_swap_event_vos
                    WHERE mono_id = %s
                    """,
                    [event_id],
                )
                u_event = self.to_dict(db.fetchall(), db.description)
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                        SELECT id, event_href, owner, team, shift_start, shift_end, availability_start, availability_end, mono_id
                        FROM shift_swap_event_vos
                        WHERE team = %s AND owner != %s
                        """,
                    [u_event["team"], user["account"]["username"]],
                )
                team_events = self.to_dict(db.fetchall(), db.description)
            if type(team_events) != list:
                temp = []
                temp.append(team_events)
                team_events = temp
            valid_swap_list = []
            for event in team_events:
                # the less than/= values here may need to be swapped
                if (
                    event["availability_start"] <= u_event["shift_start"]
                    and event["availability_end"] >= u_event["shift_end"]
                ):
                    if (
                        u_event["availability_start"] <= event["shift_start"]
                        and u_event["availability_end"] >= event["shift_end"]
                    ):
                        valid_swap_list.append(event)
        return valid_swap_list

    def get_swaps_for_single_cover(self, user, event_id):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT id, event_href, owner, team, availability_start, availability_end, mono_id
                    FROM cover_event_vos
                    WHERE mono_id = %s
                    """,
                    [event_id],
                )
                u_event = self.to_dict(db.fetchall(), db.description)
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                        SELECT id, event_href, owner, team, shift_start, shift_end, availability_start, availability_end, mono_id
                        FROM shift_swap_event_vos
                        WHERE team = %s AND owner != %s
                        """,
                    [u_event["team"], user["account"]["username"]],
                )
                team_events = self.to_dict(db.fetchall(), db.description)
            if type(team_events) != list:
                temp = []
                temp.append(team_events)
                team_events = temp
            valid_swap_list = []
            for event in team_events:
                # the less than/= values here may need to be swapped
                if (
                    u_event["availability_start"] <= event["shift_start"]
                    and u_event["availability_end"] >= event["shift_end"]
                ):
                    valid_swap_list.append(event)
        return valid_swap_list

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
