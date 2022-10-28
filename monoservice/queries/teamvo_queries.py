from models import TeamVoOut, TeamVoIn, MemberIn
from queries.pool import pool


class TeamVORepository:
    def get_user_teams(self, user):
        with pool.connection() as conn:
            with conn.cursor() as db:
                resultlst = db.execute(
                    """
                    SELECT 
                        team_id
                    FROM teams_users_relations
                    WHERE user_id = %s
                    """,
                    [user["id"]],
                )
                teams_dict = self.to_dict(resultlst.fetchall(), resultlst.description)
        team_ids = []
        if type(teams_dict) != list:
            temp = []
            temp.append(teams_dict)
            teams_dict = temp
        for dic in teams_dict:
            team_ids.append(dic["team_id"])

        teams_lst = []
        for id in team_ids:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT 
                            id, team_href, name, description
                        FROM teams_vo
                        WHERE id = %s
                        """,
                        [id],
                    )
                    teams_lst.append(
                        self.to_dict(result.fetchall(), result.description)
                    )
        return teams_lst

    def get_all(self):
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    SELECT 
                        id, team_href, name, description
                    FROM teams_vo
                    """
                )
                return self.to_dict(result.fetchall(), result.description)

    def create(self, team: TeamVoIn, user) -> TeamVoOut:
        user_id = user["id"]
        team_href = f"http://teams:8000/api/teams/{team.id}"
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    INSERT INTO teams_vo (team_href, name, description)
                    VALUES (%s, %s, %s)
                    RETURNING id, team_href, name, description
                    """,
                    [team_href, team.name, team.description],
                )
                created_team = self.to_dict(result.fetchall(), result.description)

        team_id = created_team["id"]
        member_u_str = "".join([str(team_id), user["username"]])
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    INSERT INTO teams_users_relations (team_id, user_id, unique_string)
                    VALUES (%s, %s, %s)    
                    """,
                    [team_id, user_id, member_u_str],
                )
        return created_team

    def get_team(self, id):
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    SELECT id, team_href, name, description
                    FROM teams_vo
                    WHERE id = %s;
                    """,
                    [id],
                )
                teamres = self.to_dict(result.fetchall(), result.description)
                return teamres

    def create_user_relation(self, member: MemberIn):
        print(member.team_href)
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    SELECT id, username
                    FROM users
                    WHERE username = %s
                    """,
                    [member.member_username],
                )
                user_id = result.fetchone()[0]
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    SELECT id, team_href
                    FROM teams_vo
                    WHERE team_href = %s
                    """,
                    [member.team_href],
                )
                team_id = result.fetchone()[0]
        unique_string = str(team_id) + member.member_username
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    INSERT INTO teams_users_relations (team_id, user_id, unique_string)
                    VALUES (%s, %s, %s)
                    RETURNING team_id, user_id, unique_string
                    """,
                    [team_id, user_id, unique_string],
                )
        return True

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
