from fastapi import FastAPI


app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/user')
async def get_all_users() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def create_user(username: str, age: int) -> str:
    users[str(len(users) + 1)] = f'Имя: {username}, возраст: {age}'
    return f'User {len(users)} is registered'

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int) ->str:
    if str(user_id) in users:
        users[str(user_id)] = f'Имя: {username}, возраст: {age}'
        return f'User {user_id} is updated'
    else:
        return f'User {user_id} not found'

@app.delete('/user/{user_id}')
async def delete_user(user_id: str) -> str:
    if str(user_id) in users:
        users.pop(user_id)
        return f'User {user_id} has been deleted'
    else:
        return f'User {user_id} not found'
