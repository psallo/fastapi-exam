from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from starlette.responses import HTMLResponse, RedirectResponse
import bbs_db as db


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def root(request: Request):
  return templates.TemplateResponse("index.html", {"request": request})

@app.get("/bbs")
def bbs(request: Request):
  rows = db.get_list()
  print(rows)
  data = {"request" : request, "rows" : rows}
  return templates.TemplateResponse("bbs_list.html", data)

@app.get("/write")
def write(request: Request):
  return templates.TemplateResponse("bbs_write.html", {"request": request})

@app.post("/post")
def post(request: Request,
         title: str = Form(...),
         content: str = Form(...),
         writer: str = Form(...)):
  data = (title, content, writer)
  print(data)
  db.post(data)
  return RedirectResponse(url="/bbs", status_code=303)

@app.get("/bbs/{title}")
def get_id(request: Request, title):
  row = db.get_id(title)
  data = {"request" : request, "row" : row}
  print(data)
  return templates.TemplateResponse("bbs.html", data)