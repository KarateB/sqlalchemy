import uuid

from infos import url

from sqlalchemy import create_engine, Column, String, ForeignKey, Integer, DateTime, select, func
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime as dt

engine = create_engine(url=url, echo=False)
session = sessionmaker(bind=engine)()
Base = declarative_base()


class Root(Base):
    __tablename__ = 'root'

    id_ = Column(String(), primary_key=True, server_default=str(uuid.uuid4().__str__()))
    field1 = Column(String())
    field2 = Column(String())
    field3 = Column(String())
    created_at = Column(DateTime, server_default=str(dt.utcnow()), nullable=False)
    updated_at = Column(DateTime, server_default=str(dt.utcnow()), onupdate=str(dt.utcnow()), nullable=False)

    def __init__(self, id_, field1, field2, field3):
        self.id_ = id_
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

    def __repr__(self):
        return f'id: {self.id_}, field1: {self.field1}, field2:{self.field2}, field3: {self.field3}'


if __name__ == "__main__":

    root1 = Root(id_=str(uuid.uuid4().__str__()), field1='field1', field2='field2', field3='field3')
    print(root1)

