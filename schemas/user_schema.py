
from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    phone_no: str
    password: str
    salt:str
    role:int
    status:int
    

class UserUpdate(BaseModel):
    name: str
    email: EmailStr
    phone_no: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone_no:str
    role:int
    status:int
    created_at:datetime
    updated_at:datetime

    model_config = ConfigDict(from_attributes=True)
