from fastapi import FastAPI
from pydantic import BaseModel

class myghi(BaseModel):
    name:str
    passwrod:str
    trangthai:str = False

app = FastAPI()

@app.get('/')
async def home():
    data = str(open('data.txt','r',encoding='utf-8').read()).replace('\n',',').split('<tach>')
    return data

@app.post('/dangki')
async def submit(out:myghi):
    name = out.name
    passwrod = out.passwrod
    trangthai = out.trangthai
    data = {"name":name,"passwrod":passwrod,"trangthai":trangthai}
    open('data.txt','a+',encoding='utf-8').write(str(data)+'<tach>')
    return out
