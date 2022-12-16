from infos import url

from sqlalchemy import Column, String, create_engine, DateTime, UnicodeText, func as db_functions
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_mixins import CrudMixin as CRUDMixin

engine = create_engine(url=url, echo=False)
session = sessionmaker(bind=engine)()
Base = declarative_base()

listItems = []


class MainClass(Base, CRUDMixin):
    __class_name__ = "main-class-name"

    populated_start_time = Column(DateTime, nullable=False, server_default=db_functions.now())
    populated_end_time = Column(DateTime, nullable=False, server_default=db_functions.now())


class InspectionMixin(MainClass):
    __abstract__ = True


class RootClass(MainClass):
    __tablename__ = 'root_class'

    field1 = Column(String, nullable=False)
    field2 = Column(UnicodeText, nullable=False)
    field3 = Column(DateTime)
    field4 = Column(DateTime)
    field5 = relationship('Service', backref=backref('alerts', lazy='dynamic'))


class SubClass(MainClass):
    __tablename__ = 'sub_class'
    field1 = Column(String, unique=True)
    field2 = Column(String, unique=True)
    field3 = Column(String, unique=True)
    field4 = Column(DateTime)
    field5 = Column(DateTime)

    def __repr__(self):
        return self.name


