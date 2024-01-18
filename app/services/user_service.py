from app.api.schemas.user import UserCreate, UserFromDB, UserLogin, UserRegistered
from app.utils.unitofwork import IUnitOfWork


class UserService:
    """ Сервис добавления, получения и изменения данных пользователей """

    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    async def add_user(self, user: UserCreate) -> UserFromDB:
        """ Добавление данные пользователя """

        user_dict: dict = user.model_dump()

        async with self.uow:
            user_from_db = await self.uow.user.add_one(user_dict)
            user_to_return = UserFromDB.model_validate(user_from_db)
            await self.uow.commit()
            return user_to_return

    async def get_user(self, user: UserLogin) -> UserRegistered | None:
        """ Получить данные пользователя """

        user_dict: dict = user.model_dump()

        async with self.uow:
            user_registered = await self.uow.user.get_one(user_dict)
            user_to_return = UserRegistered.model_validate(user_registered)
            return user_to_return
