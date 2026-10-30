from pydantic import BaseModel
class User(BaseModel):
    id: int
    name: str
def validate_user_data(user_id, name):
    return User(id=user_id, name=name).model_dump()
