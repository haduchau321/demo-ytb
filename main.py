from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path

class myghi(BaseModel):
    name:str
    passwrod:str
    trangthai:str = False

app = FastAPI()

@app.get('/')
async def home():
    data = str(open('data.json','r', newline='', encoding="cp437", errors='ignore').read()).replace('\n',',').split('<tach>')
    return data

@app.post('/dangki')
async def submit(out:myghi):
    name = out.name
    if name != '':
        passwrod = out.passwrod
        if passwrod != '':
            trangthai = out.trangthai
            if trangthai != '':
                data = {"name":name,"passwrod":passwrod,"trangthai":trangthai}
                open('data.json','a+', newline='', encoding="cp437", errors='ignore').write(str(data)+'<tach>')
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    
