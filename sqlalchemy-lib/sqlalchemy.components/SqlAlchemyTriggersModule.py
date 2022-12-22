from infos import url

from sqlalchemy import Column, Integer, update,  create_engine, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy_mixins import CrudMixin as CRUDMixin
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.functions import func

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
