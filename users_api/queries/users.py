from pydantic import BaseModel
from typing import  List, Optional, Union
from queries.pool import pool 

class Error(BaseModel):
    message: str

class User(BaseModel):
    id: int
    email: str
    hashed_password: str
    first_name: str
    last_name: str

class UserIn(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    email: str
    phone_number: str
    profile_picture_href: str

class UserOut(BaseModel):
    id: int
    username: str
    password: str
    first_name: str
    last_name: str
    email: str
    phone_number: str
    profile_picture_href: str

class UserPatch(BaseModel):
    password: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    phone_number: Optional[str]
    profile_picture_href: Optional[str]

class UserQueries:
    def get_all(self) -> Union[Error, List[UserOut]]:
        try:
            # connect the database
            with pool.connection() as conn:
                # get a cursor (something to run SQL with)
                with conn.cursor() as db:
                    # Run our SELECT statement
                    result = db.execute(
                        """
                        SELECT id
                            , username
                            , password
                            , first_name
                            , last_name
                            , email
                            , phone_number
                            , profile_picture_href
                        FROM users
                        ORDER BY username;
                        """
                    )
                    return [
                        self.record_to_user_out(record)
                        for record in result
                    ]
        except Exception as e:
            print(e)
            return {"message": "Could not get all users"}

    def get_one(self, user_id: int) -> Optional[UserOut]: 
        # connect the database
        with pool.connection() as conn:
            # get a cursor (something to run SQL with)
            with conn.cursor() as db:
                # Run our SELECT statement
                result = db.execute(
                    """
                    SELECT id
                            , username
                            , password
                            , first_name
                            , last_name
                            , email
                            , phone_number
                            , profile_picture_href
                    FROM users
                    WHERE id = %s
                    """,
                    [user_id]
                )
                # We're only trying to get one 
                record = result.fetchone()
                if record is None:
                    return None
                return self.record_to_user_out(record)

    def create(self, user: UserIn) -> Union[UserOut, Error]:
        # connect the database
        with pool.connection() as conn:
            # get a cursor (something to run SQL with)
            with conn.cursor() as db:
                # Run our INSERT statement
                result = db.execute(
                    """
                    INSERT INTO users (
                        username, 
                        password, 
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
                        user.password,
                        user.first_name,
                        user.last_name,
                        user.email,
                        user.phone_number,
                        user.profile_picture_href

                    ]
                )
                id = result.fetchone()[0]
                return self.user_in_to_out(id, user)

    def update(self, user_id: int, user: UserIn) -> Union[UserPatch, Error]:
        try:
            # connect the database
            with pool.connection() as conn:
                # get a cursor (something to run SQL with)
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE users
                        SET password = %s
                          ,  first_name = %s
                          , last_name = %s
                          , email = %s
                          , phone_number = %s
                          , profile_picture_href = %s
                        WHERE id = %s
                        RETURNING id
                            , password
                            , first_name
                            , last_name
                            , email
                            , phone_number
                            , profile_picture_href
                        """,
                        [
                            user.password,
                            user.first_name,
                            user.last_name,
                            user.email,
                            user.phone_number,
                            user.profile_picture_href,
                            user.user_id
                        ]
                    )
                    return self.patch_user_in_to_out(user_id, user)
        except Exception as e:
            print(e)
            return {"message": "Could not update user"}

    def delete(self, user_id: int) -> bool:
        try:
            # connect the database
            with pool.connection() as conn:
                # get a cursor (something to run SQL with)
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM users
                        WHERE id = %s
                        """,
                        [user_id]
                    )
                    return True
        except Exception as e:
            print(e)
            return False

    def user_in_to_out(self, id: int, user: UserIn):
        old_data = user.dict()
        return UserOut(id=id, **old_data)

    def patch_user_in_to_out(self, id: int, user: UserIn):
        old_data = user.dict(exclude_unset=True)
        return UserPatch(id=id, **old_data)

    def record_to_user_out(self, record):
        return UserOut(
            id=record[0],
            username=record[1],
            password=record[2],
            first_name=record[3],
            last_name=record[4],
            email=record[5],
            phone_number=record[6],
            profile_picture_href=record[7],
        )
