from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    phone_number: str

class User(BaseModel):
    id: int
    name: str
    phone_number: str

class GroupCreate(BaseModel):
    name: str

class UserGroupCreate(BaseModel):
    user_id: int
    group_id: int

class Group(BaseModel):
    id: int
    name: str
