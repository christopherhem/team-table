from routers.models import TeamVoOut, TeamVoIn
from queries.pool import pool

class TeamVORepository:
    def get_all(self):
        with pool.connection as conn:
            with conn.cursor as db:
                result = db.execute(
                    """
                    SELECT u.id, u.first_name, t.name
                    FROM users as u
                    LEFT JOIN team_vo as t
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
        with pool.connection as conn:
            with conn.cursor as db:
                result = db.execute(
                    """
                    INSERT INTO team_vo ()
                    """
                )
            

    def get_team(self, id):
        with pool.connection as conn:
            with conn.cursor as db:
                result = db.execute(
                    """
                    SELECT u.id, u.first_name, t.name
                    FROM users as u
                    LEFT JOIN team_vo as t
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
