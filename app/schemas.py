from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: str
    role: str

    class Config:
        orm_mode = True


class JobCreate(BaseModel):
    title: str
    description: str
    company_name: str


class JobResponse(BaseModel):
    id: int
    title: str
    description: str
    company_name: str

    class Config:
        orm_mode = True


class ApplicationResponse(BaseModel):
    id: int
    status: str
    created_at: datetime

    class Config:
        orm_mode = True
