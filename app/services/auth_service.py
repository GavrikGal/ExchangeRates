

from app.api.schemas.user import UserLogin
from app.repositories.user_repository import UserRepository
from app.db.database import async_session_maker


class AuthService:
    """ Сервис аутентификации """

    @staticmethod
    async def authenticate(user: UserLogin):
        # todo: Уже есть сервис пользователя,
        # там должен быть метод получения пользователя

        user_dict: dict = user.model_dump()

        pass