from fastapi import APIRouter, Depends, status, HTTPException
from module_17.app.backend.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CreateTable
from sqlalchemy.orm import Session
from module_17.app.backend.db_depends import get_db
from typing import Annotated
from module_17.app.models import *
from module_17.app.routers.schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify


router = APIRouter(prefix='/user', tags=['user'])


@router.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users


@router.get('/user_id')
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')
    else:
        return user


@router.post('/create')
async def create_user(db: Annotated[Session, Depends(get_db)], create_users: CreateUser):
    db.execute(insert(User).values(username=create_users.username, firstname=create_users.firstname,
                                   lastname=create_users.lastname, age=create_users.age,
                                   slug=slugify(create_users.username)))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router.put('/update')
async def update_user(db: Annotated[Session, Depends(get_db)], user_id: int, update_users: UpdateUser):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')
    db.execute(update(User).where(User.id == user_id).values(firstname=update_users.firstname,
                                                             lastname=update_users.lastname, age=update_users.age))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}


@router.delete('/delete')
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')
    db.execute(delete(User).where(User.id == user_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User deletion was successful!'}


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    tasks = relationship('Task', back_populates='user')
