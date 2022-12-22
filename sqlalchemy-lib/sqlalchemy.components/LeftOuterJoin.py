from infos import url

from sqlalchemy import create_engine, Column, String, ForeignKey, Integer, PrimaryKeyConstraint
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_mixins import CrudMixin as CRUDMixin

engine = create_engine(url=url, echo=False)
session = sessionmaker(bind=engine)()
Base = declarative_base()


class CRUDMixins(Base, CRUDMixin):
    __abstract__ = True


class Root(CRUDMixins):
    __tablename__ = 'root'

    id_ = Column(Integer, primary_key=True)
    field1 = Column(String())
    field2 = Column(String())
    field3 = Column(String())
    sub_relationship = relationship('Sub', backref='sub')


class Sub(CRUDMixins):
    __tablename__ = 'sub_table'
    __table_args__ = (PrimaryKeyConstraint('id_', 'id_'), )

    id_ = Column(Integer, primary_key=True)
    root_id_ = Column(Integer, ForeignKey('root.id_'))
    field1 = Column(Integer())
    field2 = Column(String())
    field3 = Column(String())


root = Root()
try:
    results_left_join = root.query(Root, Sub).outerjoin(Root, Root.id_ == Sub.id_).all()
    for o_ in results_left_join:
        print(o_)
except Exception as exception:
    print(exception, type(exception))
