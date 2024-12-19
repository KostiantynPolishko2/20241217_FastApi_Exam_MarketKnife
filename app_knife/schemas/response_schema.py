from pydantic import BaseModel, Field

class ResponseSchema(BaseModel):
    code: int
    property: str

    def __str__(self):
        return f'HTTP {self.code}, {self.property}'