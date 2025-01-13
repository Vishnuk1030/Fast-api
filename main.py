from fastapi import FastAPI,HTTPException
from typing import Optional,List

from pydantic import BaseModel


class Package(BaseModel):
    name: str
    number: int
    description: Optional[str]=None
    
class PackageIn(BaseModel):
    secret_id:int
    name: str
    number: int
    description: Optional[str]=None
    
class Todo(BaseModel):
    name:str
    due_date:str
    description:str
    
app = FastAPI()


# pydantic BaseModel
# @app.post('/package/{priority}')
# async def create_package(priority:int,package:Package,value:bool):
#     return {"priority":priority,**package.dict(),"value":value}
    
# @app.post('/package/',response_model=Package)
# async def make_package(package:PackageIn):
#     return package

# @app.post('/package/',response_model=Package,respose_model_exclude_unset=True)
# async def make_package(package:PackageIn):
#     return package

# @app.post('/package/',response_model=Package,response_model_exclude={"description"})
# async def make_package(package:PackageIn):
#     return package

@app.post('/package/',response_model=Package,response_model_include={"description"})
async def make_package(package:PackageIn):
    return package

@app.get('/')
async def myFunc():
    return {"Hello ":"world"}

@app.get("/component/{component_id}") #path params
async def getComponet(component_id:int):
    return {"component_id": component_id}

@app.get("/component/") #query params
async def read_components(number:int,text:str):
    return {"number":number,"text":text}

#create,Read,Update and Delete, Todo API

store_todo=[]

@app.get('/getTodo')
async def todo_get():
    return {"Hello":"world"}

@app.post('/PostTodo')
async def todo_post(todo:Todo):
    store_todo.append(todo)
    return todo

@app.get('/todo/',response_model=List[Todo])
async def todo_getall():
    return store_todo

@app.get('/todo/{id}')
async def get_one_todo(id:int):
    try:
        return store_todo[id]
    except:
        raise HTTPException(status_code=404,detail="Todo not found")
    
@app.put('/todo/{id}')
async def update_todo(id:int,todo:Todo):
    try:
        store_todo[id]=todo
        return store_todo[id]
    except:
        raise HTTPException(status_code=404,detail="Todo not found")

@app.delete('/todo/{id}')
async def delete_todo(id:int):
    try:
        obj=store_todo[id]
        store_todo.pop(id)
        return obj
    except:
        raise HTTPException(status_code=404,detail="Todo not found")


