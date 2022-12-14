from pydantic import BaseModel
from typing import List, Optional, Union
from queries.pool import pool
from models import User, UserIn, UserOut,  Error


class UserQueries:
    def get_all(self) -> Union[Error, List[User]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id
                            , username
                            , hashed_password
                            , first_name
                            , last_name
                            , email
                            , phone_number
                            , profile_picture_href
                        FROM users
                        ORDER BY username;
                        """
                    )
                    return [self.record_to_user_out(record) for record in result]
        except Exception as e:
            print(e)
            return {"message": "Could not get all users"}

    def get_one(self, user_id: int) -> Optional[UserOut]:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    SELECT id
                        , username
                        , hashed_password
                        , first_name
                        , last_name
                        , email
                        , phone_number
                        , profile_picture_href
                    FROM users
                    WHERE id = %s
                    """,
                    [user_id],
                )
                record = result.fetchone()
                if record is None:
                    return None
                return self.record_to_user_out(record)

    def get_user(self, email: str) -> Optional[User]:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    SELECT id
                        , username
                        , hashed_password
                        , first_name
                        , last_name
                        , email
                        , phone_number
                        , profile_picture_href
                    FROM users
                    WHERE email = %s
                    """,
                    [email],
                )
                # We're only trying to get one
                record = result.fetchone()
                if record is None:
                    return None
                return self.record_to_user_out(record)

    def create(self, user: UserIn, hashed_password: str) -> Union[User, Error]:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    INSERT INTO users (
                        username,
                        hashed_password,
                        first_name,
                        last_name,
                        email,
                        phone_number,
                        profile_picture_href
                    )
                    VALUES
                        (%s, %s, %s, %s, %s, %s, %s)
                    RETURNING id;
                    """,
                    [
                        user.username,
                        hashed_password,
                        user.first_name,
                        user.last_name,
                        user.email,
                        user.phone_number,
                        user.profile_picture_href,
                    ],
                )
                id = result.fetchone()[0]
                return User(
                    id=id,
                    email=user.email,
                    hashed_password=hashed_password,
                    username=user.username,
                    first_name=user.first_name,
                    last_name=user.last_name,
                    phone_number=user.phone_number,
                    profile_picture_href=user.profile_picture_href,
                )

    def update(self, user_id: int, user: UserIn, hp) -> Union[UserOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE users
                        SET
                            hashed_password = %s,
                            first_name = %s,
                            last_name = %s,
                            email = %s,
                            phone_number = %s,
                            profile_picture_href = %s
                        WHERE id = %s
                        RETURNING
                            id,
                            username,
                            first_name,
                            last_name,
                            email,
                            phone_number,
                            profile_picture_href
                        """,
                        [
                            hp,
                            user.first_name,
                            user.last_name,
                            user.email,
                            user.phone_number,
                            user.profile_picture_href,
                            user_id,
                        ],
                    )
                    return self.record_to_user_out_safe(db.fetchone())
        except Exception as e:
            print(e)
            return {"message": "Could not update user"}

    def delete(self, user_id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM users
                        WHERE id = %s
                        """,
                        [user_id],
                    )
                    return True
        except Exception as e:
            print(e)
            return False

    def user_in_to_out(self, id: int, user: UserIn):
        old_data = user.dict(exclude_unset=True)
        return UserOut(id=id, **old_data)

    def put_user_in_to_out(self, id: int, user: UserIn):
        old_data = user.dict(exclude_unset=True)
        return UserOut(id=id, **old_data)

    def record_to_user_out(self, record):
        return User(
            id=record[0],
            username=record[1],
            hashed_password=record[2],
            first_name=record[3],
            last_name=record[4],
            email=record[5],
            phone_number=record[6],
            profile_picture_href=record[7],
        )

    def record_to_user_out_safe(self, record):
        return User(
            id=record[0],
            username=record[1],
            first_name=record[3],
            last_name=record[4],
            email=record[5],
            phone_number=record[6],
            profile_picture_href=record[7],
        )
