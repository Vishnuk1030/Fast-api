from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app=FastAPI()

templates=Jinja2Templates(directory="template")

@app.get("/book/{id}",response_class=HTMLResponse)
async def read_book(request:Request,id:int):
    return templates.TemplateResponse("index.html",{"request":request,"id":id})

