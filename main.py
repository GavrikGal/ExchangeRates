from fastapi import FastAPI, Depends

from app.api.schemas.user import UserFromDB, UserCreate
from app.services.user_service import UserService
from app.utils.unitofwork import UnitOfWork, IUnitOfWork

app = FastAPI()


async def get_user_service(uow: IUnitOfWork = Depends(UnitOfWork)) -> UserService:
    return UserService(uow)


@app.post("/auth/register/", response_model=UserFromDB)
async def register(user_data: UserCreate,
                   user_service: UserService = Depends(get_user_service)):
    # fake_user = UserFromDB(username=user_data.username, id=1)

    # Кодер понимает, что дальше уже сложно обманывать
    # и надо реализовать через TDD сервис сохранения пользователей
    # Поэтому кодер ожидает получить сервис, который, при передаче ему
    # входных данных нового пользователя, вернет ему пользователя с автоматически
    # сгенерированным id.
    # Id умеют генерировать базы данных. Осталось получить сервис.
    # user_service = await get_user_service()

    # Сервис получен, теперь его надо тестировать
    user_from_db = await user_service.add_user(user_data)

    return user_from_db
