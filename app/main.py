from fastapi import FastAPI
from module_17.app.routers import task, user

app = FastAPI()


@app.get('/')
async def wellcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task.router)
app.include_router(user.router)
