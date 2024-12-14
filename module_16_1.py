from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return "Главная страница"

@app.get("/user/admin")
async def admin_page():
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def user_id_page(user_id: int):
    return f"Вы вошли как пользователь № {user_id}"

@app.get("/user")
async def user_inform_page(username: str, age: int):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"


# запуск: uvicorn module_16_1:app --reload
