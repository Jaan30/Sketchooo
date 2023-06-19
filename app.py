from fastapi import FastAPI 
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()
app.mount("/static",StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    with open('templates/index.html','r') as file:
        content = file.read()
    return HTMLResponse(content=content)
    