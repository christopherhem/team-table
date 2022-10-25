from typing import List, Union
from models import TeamOut, TeamIn, Error
from queries.pool import pool
from datetime import datetime as datetime
from datetime import *


class SwapRepository:
    def get_valid_swaps(self, user):
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                """
                SELECT id, event_href, owner, team, shift_start, shift_end, availability_start, availability_end
                FROM shift_swap_event_vos
                WHERE owner = %s
                """,
                [user['account']['username']]
                )
                user_swaps = self.to_dict(result.fetchall(),result.description)
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
                        SELECT id, event_href, owner, team, shift_start, shift_end, availability_start, availability_end
                        FROM shift_swap_event_vos
                        WHERE team = %s AND owner != %s                   
                        """,
                        [
                            swap['team'],
                            user['account']['username']
                        ]
                    )
                    team_events = self.to_dict(result.fetchall(),result.description)
            if type(team_events) != list:
                temp = []
                temp.append(team_events)
                team_events = temp
            valid_swap_list = []
            for event in team_events:
                if event['availability_start'] <= swap['shift_start'] and event['availability_end']>=swap['shift_end']:
                    if swap['availability_start'] <= event['shift_start'] and swap['availability_end']>=event['shift_end']:
                        valid_swap_list.append(event)
            partial_out = {'user_event' : swap, 'valid_swaps': valid_swap_list}
            final.append(partial_out)
        if type(final)!=list:
            temp = []
            temp.append(final)
            final = temp
        finaldict = {}
        finaldict['swaps'] = final
        return finaldict


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