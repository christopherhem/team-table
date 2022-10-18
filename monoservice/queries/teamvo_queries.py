from models import TeamVoOut, TeamVoIn
from queries.pool import pool

class TeamVORepository:
    def get_all(self):
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    SELECT u.id, u.first_name, t.name
                    FROM users as u
                    LEFT JOIN teams_vo as t
                        ON (u.id = t.user_id)
                    GROUP BY
                        u.id, u.first_name, t.name
                    ORDER BY t.name
                    """
                )
                teams = []
                rows = result.fetchall()
                for row in rows:
                    team = self.team_record_to_dict(row, result.description)
                    teams.append(team)
                return teams

    #unfinished, need create function for pub/sub to work
    def create(self, team:TeamVoIn)->TeamVoOut:
        user_id = None
        team_href = f"https://teams:8000/api/teams/{team.team_id}"
        with pool.connection() as conn:
            with conn.cursor() as db:
                user = db.execute(

                """
                SELECT id
                FROM users
                WHERE username=%s;

                """,
                [team.username]
                )
                user_id = self.to_dict(user.fetchall(), user.description)
                user_id = user_id["id"]

        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    INSERT INTO teams_vo (team_href, name, user_id)
                    VALUES (%s, %s, %s)
                    RETURNING id, team_href, name, user_id
                    """,
                    [
                        team_href,
                        team.name,
                        user_id
                    ]
                )
                return self.to_dict(result.fetchall(), result.description)


    def get_team(self, id):
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    SELECT u.id, u.first_name, t.name
                    FROM users as u
                    LEFT JOIN teams_vo as t
                        ON (u.id = t.user_id)
                    WHERE t.id = %s
                    """,
                    [id]
                )
                row = result.fetchone()
                return self.team_record_to_dict(row, result.description)

    def team_record_to_dict(self, row, description):
        team = None
        if row is not None:
            team = {}
            team_fields = [
                "id",
                "href",
                "name",
                "user_id"
            ]
            for i, column in enumerate(description):
                if column.name in team_fields:
                    team[column.name] = row[i]
            team["id"] = team["id"]

            user = {}
            user_fields = [
                "user_id",
                "first_name"
            ]
            for i, column in enumerate(description):
                if column.name in user_fields:
                    user[column.name] = row[i]
            user["id"] = user["user_id"]

            team["user_id"] = user
        return team


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
