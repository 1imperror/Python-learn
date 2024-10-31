from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from typing import Annotated

app = FastAPI()
templates = Jinja2Templates(directory='templates')


class User(BaseModel):
    id: int
    username: str
    age: int


users: list[User] = []


@app.get('/', response_class=HTMLResponse)
async def new_get(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@app.get("/user/{user_id}", response_class=HTMLResponse)
async def get_users(request: Request, user_id: int) -> HTMLResponse:
    user = next((user for user in users if user.id == user_id), None)
    return templates.TemplateResponse('users.html', {'request': request, 'user': user})


@app.post("/user/{username}/{age}", response_model=User)
async def add_user(
    username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='Ivano')],
        age: Annotated[int, Path(ge=18, le=70, description='Enter age', example=24)]) -> User:
    user_id = users[-1].id + 1 if users else 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/{username}/{age}", response_model=User)
async def update_user(
    user_id: int,
    username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='Ivano')],
        age: Annotated[int, Path(ge=18, le=70, description='Enter age', example=24)]) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}", response_model=User)
async def delete_user(user_id: int) -> User:
    for i, user in enumerate(users):
        if user.id == user_id:
            return users.pop(i)
    raise HTTPException(status_code=404, detail="User was not found")
