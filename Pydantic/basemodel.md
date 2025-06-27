# [Models](https://docs.pydantic.dev/latest/concepts/models/)

Primary way of defining schema is via models. Models are classes which inherit from BaseModel and defines fields as annotated attributes

Think of Models like a group of required data types.

Models share many similar data types as in Python.

## Example

```
from pydantic import BaseModel, EmailStr, validator

class User(BaseModel):
    name: str
    email: EmailStr
    account_id: int

    @validator("account_id")
    def validate_account_id(cls, value):
        if value <= 0:
            raise ValueError(f"account_id must be positive: {value}")
        return value

user = User(name="jack", email="jack@pixegami.io", account_id=-1234)
print(user)
```