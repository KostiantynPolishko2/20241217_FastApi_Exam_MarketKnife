# Custom path parameter that converts input to lowercase
class LowerCasePath(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value: str) -> str:
        if not isinstance(value, str):
            raise TypeError("Value must be a string")
        return value.lower()