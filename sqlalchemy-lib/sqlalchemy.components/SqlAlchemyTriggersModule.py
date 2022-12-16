from infos import url

from sqlalchemy import create_engine, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy.sql.functions as func
from sqlalchemy import Column, Integer, update
from sqlalchemy_mixins import CrudMixin as CRUDMixin

engine = create_engine(url=url, echo=False)
session = sessionmaker(bind=engine)()
Base = declarative_base()

listItems = []
Table = None


class Root(Base):
    id: int


class Object(CRUDMixin, Base):
    __tablename__ = "objects"

    id = Column(Integer, primary_key=True, nullable=False)
    last_update = Column(DateTime, server_default=func.now(), onupdate=func.current_timestamp())

    def touch(self):
        stmt = update(Root).where(Root.id == self.id)
        session.engine.execute(stmt)
