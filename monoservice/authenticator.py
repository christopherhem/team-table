import os
from fastapi import Depends
from jwtdown_fastapi.authentication import Authenticator
from queries.users_queries import UserQueries, User, UserOut


class MyAuthenticator(Authenticator):
    async def get_account_data(
        self,
        email: str,
        accounts: UserQueries,
    ):
        return accounts.get_user(email)

    def get_account_getter(
        self,
        accounts: UserQueries = Depends(),
    ):
        return accounts

    def get_hashed_password(self, account: User):
        return account.hashed_password

    def get_account_data_for_cookie(self, account: User):
        return account.email, UserOut(**account.dict())


authenticator = MyAuthenticator(os.environ["SIGNING_KEY"])
