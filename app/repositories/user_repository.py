from app.repositories.base_repository import BaseRepository
from app.db.models import User


class UserRepository(BaseRepository):
    model = User
