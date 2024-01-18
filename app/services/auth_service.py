from app.api.schemas.user import UserLogin
from app.services.user_service import UserService
from app.utils.unitofwork import UnitOfWork


class AuthService:
    """ Сервис аутентификации """

    @staticmethod
    async def authenticate(user: UserLogin):
        user_service = UserService(UnitOfWork())
        user_from_db = await user_service.get_user(user)

        pass