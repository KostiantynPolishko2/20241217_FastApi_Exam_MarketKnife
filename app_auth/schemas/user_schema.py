from pydantic import BaseModel, EmailStr, Field
from uuid import UUID

class UserSchema(BaseModel):
    username: str = Field(min_length=5, max_length=12, description='login')
    email: EmailStr
    is_disabled: bool=Field(default=False, description="users' status")

class UserSchemaAuth(UserSchema):
    password: str = Field(min_length=5, max_length=12, description='login')

class UserSchemaInDB(UserSchema):
    guid: UUID
    hashed_password: str

class UserSchemaOut(BaseModel):
    guid: UUID
    email: str | None = None




