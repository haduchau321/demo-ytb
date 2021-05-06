from fastapi import FastAPI
from pydantic import BaseModel

class myghi(BaseModel):
    name:str
    passwrod:str
    trangthai:str = False

app = FastAPI()

@app.get('/')
async def home():
    data = {'name':'haduchau','password':'yeutaodi123','data':'xin chào bạn đã bị tấn công'}
    return data

@app.post('/dangki')
async def submit(out:myghi):
    name = out.name
    passwrod = out.passwrod
    trangthai = out.trangthai
    return out
