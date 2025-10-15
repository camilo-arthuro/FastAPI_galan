from fastapi import FastAPI
from pydantic import BaseModel

class NewUser(BaseModel):
    name: str
    last_name: str
    age: int
    country: str

class UpdateUser(BaseModel):
    new_name: str
    new_last_name: str
    new_age: int
    new_country: str
class PartialUpdate(BaseModel):
    new_age: int
    new_country: str

app = FastAPI()

users_list = []
users_dic = {}
counter_id = 1
@app.post("/api/users")
async def create_user(new_user: NewUser):
    global counter_id
    users_list.append(new_user)
    users_dic[counter_id] = new_user
    counter_id += 1
    return users_dic
@app.get("/api/users/{id}")
async def get_user_id(id: int):
    return users_dic[id]
@app.get("/api/users")
async def get_all_users():
    return users_dic
@app.put("/api/users/{id}")
async def update_user(id: int, updated_user: UpdateUser):
    #this function does not update the user from the list
    users_dic[id] = updated_user
    return users_dic[id]
@app.patch("/api/users/{id}")
async def partial_update(id: int, partial_user: PartialUpdate):
    #this function does not update the user from the list
    current_user = users_dic[id]
    new_user = NewUser(
        name = current_user.name,
        last_name = current_user.last_name,
        age = partial_user.new_age,
        country = partial_user.new_country
    )
    users_dic[id] = new_user
    return users_dic[id]
@app.delete("/api/usuaris/{id}")
async def delete_user(id: int):
    #this function does not delete the user from the list
    users_dic.pop(id)
    return users_dic