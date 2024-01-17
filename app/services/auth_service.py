

from app.api.schemas.user import UserLogin
from app.repositories.user_repository import UserRepository
from app.db.database import async_session_maker


class AuthService:
    """ Сервис аутентификации """

    @staticmethod
    async def authenticate(user: UserLogin):
        user_dict: dict = user.model_dump()
        # todo: Из репозитория получить пользователя
        pass