from sqlalchemy.orm import Session
from uuid import uuid4
import utils as muy_utils
# from utils import get_password_hash

from app_auth.models.user import User
from app_auth.schemas.user_schema import UserSchemaAuth
from app_auth.infrastructures.user_exception import user_exc404, new_user_exc400

class AuthRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user(self, username: str)->User:
        user: User = self.db.query(User).filter(User.username == username.lower()).first()
        if not user:
            raise user_exc404
        return user

    def is_exist_user(self, username: str)->None:
        user: User = self.db.query(User).filter(User.username == username.lower()).first()
        if user is not None:
            raise new_user_exc400

    def add_user_to_db(self, request: UserSchemaAuth)->int:
        new_user = User(
            username=request.username,
            email=request.email,
            is_disabled=request.is_disabled,
            guid=uuid4(),
            hashed_password=muy_utils.get_password_hash(request.password)
        )

        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)

        return new_user.id