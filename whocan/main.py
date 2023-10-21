from typing import Annotated

from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, Session
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from .orm.connect import prepare_db
from .deps import db_session

app = FastAPI()

app.mount("/static", StaticFiles(directory="whocan/static"), name="static")


@app.on_event("startup")
def on_startup():
    prepare_db()


templates = Jinja2Templates(directory="whocan/templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("home.html.jinja", {"request": request})
