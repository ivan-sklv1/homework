from typing import List
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel


app = FastAPI()

users = []

class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/users')
async def get_all_users() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
async def create_user(username: str, age: int):
    user_id = int(max((u.id for u in users), default=0) + 1)
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int):
    for u in users:
        if u.id == user_id:
            u.username = username
            u.age = age
            return u
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User was not found.')


@app.delete('/user/{user_id}')
async def delete_user(user_id: int):
    for i, u in enumerate(users):
        if u.id == user_id:
            del users[i]
            return u
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User was not found.')
