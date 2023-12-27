from pydantic import BaseModel, ConfigDict


class UserCreate(BaseModel):
    username: str
    password: str


class UserFromDB(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
