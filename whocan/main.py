from typing import Annotated

from fastapi import FastAPI, Depends, Form
from sqlmodel import SQLModel, Session, select
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from .orm.connect import prepare_db, engine
from .deps import db_session
from .orm.model import *
from .vertex_query import query_ai

app = FastAPI()

app.mount("/static", StaticFiles(directory="whocan/static"), name="static")


@app.on_event("startup")
def on_startup():
    prepare_db()


templates = Jinja2Templates(directory="whocan/templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("home.html.jinja", {"request": request})


@app.post("/search", response_class=HTMLResponse)
async def search(request: Request, issue: Annotated[str, Form()], district: Annotated[int, Form()]):
    with Session(engine) as sess:
        res = sess.exec(
            select(Candidate, Site).where(Candidate.district == district).join(Site,
                                                                               Site.cand_id == Candidate.id)).fetchall()

    # Candidate to prompt summary
    results: dict[str, str] = {}

    # Exec query on all sites
    for cand, site in res:
        prompt_res = query_ai(issue, cand.name, site.site)
        results[
            cand.name] = prompt_res if len(
            prompt_res.strip()) > 2 else "The candidate does not have any statements on this subject."

    return templates.TemplateResponse("search.html.jinja",
                                      {"request": request, "results": results, "district": district, "issue": issue})
