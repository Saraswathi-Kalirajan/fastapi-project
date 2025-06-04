from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

from pydantic.types import conint


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True


class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)





























# from pydantic import BaseModel, EmailStr, Field
# from datetime import datetime 
# from typing import Optional, Annotated
# from pydantic.types import conint
# class PostBase(BaseModel):
#     title: str
#     content:str
#     published: bool = True
#     #rating: Optional[int] = None 
# class PostCreate(PostBase):
#     pass

# class UserOut(BaseModel):
#     email: EmailStr 
#     id: int 
#     created_at: datetime
#     class Config:
#         orm_mode = True  

# class Post(PostBase):
#     id: int
#     created_at: datetime
#     owner_id: int
#     owner: UserOut
#     class Config:
#         orm_mode = True 

# class PostOut(BaseModel):
#     Post: Post 
#     votes: int
#     class Config:
#         orm_mode = True 

# class UserCreate(BaseModel):
#     email: EmailStr 
#     password: str 

# # class UserOut(BaseModel):
# #     email: EmailStr 
# #     id: int 
# #     created_at: datetime
# #     class Config:
# #         orm_mode = True 
# class UserLogin(BaseModel):
#     email: EmailStr
#     password: str

# class Token(BaseModel):
#     access_token: str 
#     token_type: str 

# class TokenData(BaseModel):
#     id: Optional[int] = None


# class Vote(BaseModel):
#     post_id: int
#     dir: Annotated[int, Field(le=1)]   


# from pydantic import BaseModel, EmailStr
# from datetime import datetime
# from typing import Optional

# from pydantic.types import conint

# from app.models import User


# class PostBase(BaseModel):
#     title: str
#     content: str
#     published: bool = True


# class PostCreate(PostBase):
#     pass


# class UserOut(BaseModel):
#     id: int
#     email: EmailStr
#     created_at: datetime

#     class Config:
#         orm_mode = True


# class Post(PostBase):
#     id: int
#     created_at: datetime
#     owner_id: int
#     owner: UserOut

#     class Config:
#         orm_mode = True


# # class PostOut(BaseModel):
# #     Post: Post
# #     votes: int

# #     class Config:
# #         orm_mode = True  


# class PostOut(BaseModel):
#     id: int
#     title: str
#     content: str
#     created_at: str
#     owner: Optional[User] = None
#     votes: int

#     class Config:
#         orm_mode = True


# # class PostOut(BaseModel):
# #     id: int
# #     title: str
# #     content: str
# #     created_at: str
# #     owner: Optional[UserOut] = None
# #     votes: int

# #     class Config:
# #         orm_mode = True


# class UserCreate(BaseModel):
#     email: EmailStr
#     password: str


# class UserLogin(BaseModel):
#     email: EmailStr
#     password: str


# class Token(BaseModel):
#     access_token: str
#     token_type: str


# class TokenData(BaseModel):
#     id: Optional[int] = None


# class Vote(BaseModel):
#     post_id: int
#     dir: conint(le=1)