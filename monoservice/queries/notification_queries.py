from typing import List, Union
from models import Error
from models import ShiftSwapEventOut
from queries.pool import pool
from datetime import datetime


class NotificationRepository:
    def get_notifications_by_user(self,user):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT id, message, seen
                    FROM notifications
                    WHERE user_id = %s
                    """,
                    [user['id']]
                )
                notifications = self.to_dict(db.fetchall(),db.description)
        if type(notifications) != list:
            temp = []
            temp.append(notifications)
            notifications = temp
        return notifications

    def update_seen(self, uid, id):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT user_id
                    FROM notifications
                    WHERE id = %s
                    """,
                    [id]
                )
                validation = self.to_dict(db.fetchall(),db.description)
        if validation['user_id'] == uid:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE notifications
                        SET seen = true
                        WHERE id = %s
                        """,
                        [id]
                    )
            return True
        else:
            return False

    def delete(self, uid, id):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT user_id
                    FROM notifications
                    WHERE id = %s
                    """,
                    [id]
                )
                validation = self.to_dict(db.fetchall(),db.description)
        if validation['user_id'] == uid:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM notifications
                        WHERE id = %s
                        """,
                        [id]
                    )
            return True
        else: 
            return False


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