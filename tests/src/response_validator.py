
mock_response = [
    {
        "job": "Radiographer, diagnostic",
        "company": "Klein, Dillon and Neal",
        "residence": "2232 Jackson Forks\nLake Teresa, CO 46959",
        "website": [
            "http://bishop-torres.net/",
            "http://bishop-torres.net/"
        ],
        "username": "aabbott",
        "name": "Madison Mitchell",
        "address": "1782 Moore Hill Apt. 717\nWest Stephaniestad, NM 75293",
        "mail": "amberrodriguez@hotmail.com",
        "phone": {
            "home": "677-197-4239x889",
            "mobile": "001-594-038-9255x99138"
        }
    },
    {
        "job": "Radiographer, diagnostic",
        "company": "Klein, Dillon and Neal",
        "residence": "2232 Jackson Forks\nLake Teresa, CO 46959",
        "website": [
            "http://bishop-torres.net/",
            "http://bishop-torres.net/"
        ],
        "username": "aabbott",
        "name": "Madison Mitchell",
        "address": "1782 Moore Hill Apt. 717\nWest Stephaniestad, NM 75293",
        "mail": "amberrodriguez@hotmail.com",
        "phone": {
            "home": "677-197-4239x889",
            "mobile": "001-594-038-9255x99138"
        }
    },
    {
        "job": "Radiographer, diagnostic",
        "company": "Klein, Dillon and Neal",
        "residence": "2232 Jackson Forks\nLake Teresa, CO 46959",
        "username": "aabbott",
        "name": "Madison Mitchell",
        "address": "1782 Moore Hill Apt. 717\nWest Stephaniestad, NM 75293",
        "mail": "amberrodriguez@hotmail.com",
        "phone": {
            "home": "677-197-4239x889",
            "mobile": "001-594-038-9255x99138"
        }
    }

]

from typing import List, Optional
from pydantic import BaseModel, EmailStr, AnyHttpUrl, Field, ValidationError, validator
from .enums import *

class MockResponsePhoneField(BaseModel):
    home: str
    mobile: str


class MockResponse(BaseModel):
    job: str
    company: str
    residence: str
    website: Optional[List[AnyHttpUrl]] = Field(min_items=2, max_items=3)
    username: str
    name: str
    address: str
    mail: EmailStr
    phone: MockResponsePhoneField


class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    gender: Gender
    status: Status

    @validator('id', pre=True)
    def check_id_value_type(cls, _id):
        if type(_id) == int:
            return _id
        raise ValidationError(f"Excepted that id`s value type is int; But got: {type(_id)}")

class UserNotExists(BaseModel):
    message: str
    
    @validator('message')
    def check_message_val(cls, message):
        print(message)
        if message != 'Resource not found':
            raise ValidationError(f"Excepted that message will be 'Resource not found'; But got: {message}")

class Post(BaseModel):
    id: int
    user_id:int
    title:str
    body:str
    @validator('id', pre=True)
    def check_id_value_type(cls, _id):
        if type(_id) == int:
            return _id
        raise ValidationError(f"Excepted that id`s value type is int; But got: {type(_id)}")
    @validator('user_id', pre=True)
    def check_user_id_value_type(cls, user_id):
        if type(user_id) == int:
            return user_id
        raise ValidationError(f"Excepted that user_id`s value type is int; But got: {type(user_id)}")

if __name__ == "__main__":
    t_d = {
        'id': "3230", 
        'name': 'Mr. Himadri Bhattacharya', 
        'email': 'himadri_mr_bhattacharya@heller-effertz.co', 
        'gender': 'male', 
        'status': 'inactive'
    }
    User.parse_obj(t_d)
    print('done')