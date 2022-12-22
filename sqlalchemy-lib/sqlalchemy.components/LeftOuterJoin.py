from infos import url

from sqlalchemy import create_engine, Column, String, ForeignKey, Integer, PrimaryKeyConstraint
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_mixins import CrudMixin as CRUDMixin, BaseMixin

engine = create_engine(url=url, echo=False)
session = sessionmaker(bind=engine)()
Base = declarative_base()


class CRUDMixins(CRUDMixin):
    __abstract__ = True


class Root(CRUDMixins, BaseMixin):
    __tablename__ = 'root'

    id_ = Column(Integer, primary_key=True)
    field1 = Column(String())
    field2 = Column(String())
    field3 = Column(String())


class Sub(CRUDMixins, BaseMixin):
    __tablename__ = 'sub_table'

    id_ = Column(Integer, primary_key=True)
    root_id_ = Column(Integer)
    field1 = Column(Integer())
    field2 = Column(String())
    field3 = Column(String())


if __name__ == "__main__":
    root = Root()
    root.__tablename__ = 'root'
    sub = Sub()
    sub.__tablename__ = 'sub_table'
    try:
        results_left_join = root.query(root, sub).outerjoin(Root, Root.id_ == Sub.id_).all()
        for o_ in results_left_join:
            print(o_)
    except Exception as exception:
        print(exception, type(exception))
