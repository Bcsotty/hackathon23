from sqlmodel import create_engine, SQLModel, Session, select
# Required to create tables
from .model import *

sqlite_file_name = "db.sqlite"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def prepare_db():
    # Create tables if not exists
    SQLModel.metadata.create_all(engine)

    with Session(engine) as sess:
        # TODO add hardcoded things
        pass
