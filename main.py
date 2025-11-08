from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory=templates)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root(request: Request):
  return templates.TemplateRespomse("index.html", {"request": request})