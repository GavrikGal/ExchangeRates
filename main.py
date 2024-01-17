from fastapi import FastAPI, Depends

from app.api.schemas.user import UserFromDB, UserCreate, UserLogin
from app.services.user_service import UserService
from app.services.auth_service import AuthService
from app.utils.unitofwork import UnitOfWork, IUnitOfWork

app = FastAPI()


async def get_user_service(uow: IUnitOfWork = Depends(UnitOfWork)) -> UserService:
    return UserService(uow)


@app.post("/auth/register/", response_model=UserFromDB)
async def register(user_data: UserCreate,
                   user_service: UserService = Depends(get_user_service)):
    """ Конечная точка регистрации пользователя """
    # fake_user = UserFromDB(username=user_data.username, id=1)

    # Кодер понимает, что с фейковой БД уже сложно обманывать пользователя
    # и надо реализовать через TDD сервис сохранения пользователей
    # Поэтому кодер ожидает получить сервис, который, при передаче ему
    # входных данных нового пользователя, вернет ему пользователя с автоматически
    # сгенерированным id.
    # Id умеют генерировать базы данных. Осталось получить сервис.
    # Сервис будем получать через Depends - это проще

    # Сервис получен, теперь его надо тестировать
    user_from_db = await user_service.add_user(user_data)

    return user_from_db


@app.post('/auth/login/')
async def login(user: UserLogin):
    """ Конечная точка логина """
    # 1. Пользователь хочет конечную точку? Вот, пожалуйста
    # pass

    # 2. Пользователь хочет получить json? Ща дам
    # return {'message': 'Держи json'}

    # 3. Тип токена должен быть 'bearer'? Ща организуем
    # return {'token_type': 'bearer'}

    # 4. Хочет иметь 'access_token' в json-ответе? Ща засуну
    # return {'token_type': 'bearer',
    #         'access_token': 'access_token'}

    # 5. Походу пора реализовывать выдачу настоящих токенов этому пользователю
    # Для этого есть библиотека JWT.

    # todo: переделать. Уже есть сервис пользователя, там должен быть метод получения пользователя
    # Надо сначала сделать сервис, который будет аутентифицировать пользователя
    auth_user = AuthService.authenticate(user)

    # Затем надо будет выдать этому пользователю токен

    return {'token_type': 'bearer',
            'access_token': 'норм токен для Гала'}

