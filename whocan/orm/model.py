import datetime
from typing import Optional

import pydantic.main
from sqlmodel import SQLModel, Field
from sqlalchemy import PrimaryKeyConstraint


class Candidate(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    district: str
    name: str


class Site(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    cand_id: int = Field(foreign_key="candidate.id")
    site: str
