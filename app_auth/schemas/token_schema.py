from pydantic import BaseModel

class TokenSchema(BaseModel):
    access_token: str
    token_type: str

class TokenSchemaData(BaseModel):
    username: str | None = None
