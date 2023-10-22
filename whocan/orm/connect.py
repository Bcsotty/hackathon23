from sqlmodel import create_engine, SQLModel, Session, select
# Required to create tables
from .model import *
import csv
from .extract_website import extract_website_text

sqlite_file_name = "db.sqlite"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def prepare_db():
    # Create tables if not exists
    SQLModel.metadata.create_all(engine)

    cand_csv = csv.reader(open('candidates.csv'))

    # Add candidates from csv into DB
    with Session(engine) as sess:
        # Only do once
        if not sess.get(Candidate, 1):
            for district, name, url in cand_csv:
                cand = Candidate(district=int(district), name=name)

                sess.add(cand)
                sess.commit()

                # Download and cache websites
                site_txt = " ".join(extract_website_text(url))

                sess.add(Site(cand_id=cand.id, site=site_txt))
                sess.commit()
