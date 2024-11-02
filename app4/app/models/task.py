from fastapi import APIRouter, Depends, status, HTTPException
from module_17.app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from module_17.app.models.user import User
from sqlalchemy.schema import CreateTable
from sqlalchemy.orm import Session
from module_17.app.backend.db_depends import get_db
from typing import Annotated
from module_17.app.models import *
from module_17.app.routers.schemas import CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete
from slugify import slugify

router = APIRouter(prefix='/task', tags=['task'])


@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks


@router.get('/task_id')
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    tasks = db.scalar(select(Task).where(Task.id == task_id))
    if tasks is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task was not found')
    else:
        return task


@router.post('/create')
async def create_task(db: Annotated[Session, Depends(get_db)], create_tasks: CreateTask, user_id: int):
    users = db.scalar(select(User).where(User.id == user_id))
    if users is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')

    db.execute(insert(Task).values(title=create_tasks.title, content=create_tasks.content,
                                   priority=create_tasks.priority, slug=slugify(create_tasks.title), user_id=user_id))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router.put('/update')
async def update_task(db: Annotated[Session, Depends(get_db)], task_id: int, user_id: int, update_tasks: UpdateTask):
    users = db.scalar(select(User).where(User.id == user_id))
    if users is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')
    db.execute(update(Task).where(Task.id == task_id).values(title=update_tasks.title, content=update_tasks.content,
                                                             priority=update_tasks.priority))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}


@router.delete('/delete')
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    tasks = db.scalar(select(Task).where(Task.id == task_id))
    if tasks is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task was not found')
    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task deletion was successful!'}


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)
    slug = Column(String, unique=True, index=True)
    user = relationship('User', back_populates='tasks')
