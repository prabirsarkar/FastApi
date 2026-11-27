
from pydantic import BaseModel, ConfigDict, EmailStr

class EmployeeCreate(BaseModel):
    name: str
    email: EmailStr
    designation: str
    department: str | None = None

class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    designation: str
    department: str | None

    model_config = ConfigDict(from_attributes=True)
