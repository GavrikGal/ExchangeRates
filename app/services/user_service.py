from app.api.schemas.user import UserCreate, UserFromDB
from app.utils.unitofwork import IUnitOfWork


class UserService:

    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    async def add_user(self, user: UserCreate) -> UserFromDB:
        user_dict: dict = user.model_dump()

        async with self.uow:
            user_from_db = await self.uow.user.add_one(user_dict)
            user_to_return = UserFromDB.model_validate(user_from_db)
            await self.uow.commit()
            return user_to_return

        # session = get_async_session()
        # user_rep = UserRepository(session)
        # user_from_db = await user_rep.add_one(user.model_dump())
        # user_to_return = UserFromDB.model_validate(user_from_db)
        # await session.commit()
        # await session.close()
        #
        # return user_to_return
