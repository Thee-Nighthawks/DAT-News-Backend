from pydantic import BaseModel
from typing import Optional, TypeVar
from datetime import datetime

T = TypeVar('T')

class Register(BaseModel):
    mail: str
    password: str
    name: str
    age: int
    gender: int
    admin: Optional[int] = 0

class Login(BaseModel):
    mail: str
    password: str

class News(BaseModel):
    nele: int
    title: str
    author: Optional[dict] = None
    date: datetime
    body: str
    audio: Optional[str] = None
    link: str
    comment: Optional[dict] = None
    sentiment: int

class NewspaperAlign(BaseModel):
    neutral: int
    right: int
    left: int 

class Response(BaseModel):
    code: str
    status: str
    message: str
    result: Optional[T] = None


# Type definers
NewsType = {
    'nele': int,
    'title': str,
    'author': dict,
    'date': datetime,
    'body': str,
    'audio': str,
    'link': str,
    'comment': dict,
    'sentiment': int
}

SentimentType = {
    1: 'positive',
    2: 'Neutral',
    3: 'Negetive'
}

GenderType = {
    1: 'male',
    2: 'female',
    3: 'Prefer not to respond'
}