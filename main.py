from fastapi import FastAPI

from app.api.schemas.user import UserFromDB, UserCreate

app = FastAPI()


@app.post("/auth/register/", response_model=UserFromDB)
async def register(user_data: UserCreate):
    fake_user = UserFromDB(username=user_data.username, id=1)
    return fake_user
