from fastapi import FastAPI
from typing import Optional

from pydantic import BaseModel

class Package(BaseModel):
    name: str
    number: int
    description: Optional[str]=None
    
app = FastAPI()

# pydantic BaseModel
@app.post('/package/{priority}')
async def create_package(priority:int,package:Package,value:bool):
    return {"priority":priority,**package.dict(),"value":value}
    
@app.get('/')
async def myFunc():
    return {"Hello ":"world"}

@app.get("/component/{component_id}") #path params
async def getComponet(component_id:int):
    return {"component_id": component_id}

@app.get("/component/") #query params
async def read_components(number:int,text:str):
    return {"number":number,"text":text}

