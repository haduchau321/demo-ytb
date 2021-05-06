from fastapi import FastAPI
# import uvicorn
from pydantic import BaseModel
from pathlib import Path

class myghi(BaseModel):
    name:str
    passwrod:str
    trangthai:str = False

app = FastAPI()

@app.get('/')
async def home():
    data = str(open(str(Path().absolute())+'\\data.json','r', newline='', encoding="cp437", errors='ignore').read()).replace('\n',',').split('<tach>')
    return data

@app.post('/dangki')
async def submit(out:myghi):
    name = out.name
    if len(name) > 0:
        passwrod = out.passwrod
        if len(passwrod) > 0:
            trangthai = out.trangthai
            if len(trangthai) > 0:
                data = {"name":name,"passwrod":passwrod,"trangthai":trangthai}
                open(str(Path().absolute())+'\\data.json','r', newline='', encoding="cp437", errors='ignore').write(str(data)+'<tach>')
                return True
            else:
                return False
        else:
            return False
    else:
        return False
