from beanie import Document
from fastapi_users_db_beanie import BeanieBaseUser, BeanieUserDatabase


class User(BeanieBaseUser, Document):
    pass


async def get_user_db():
    yield BeanieUserDatabase(User)

