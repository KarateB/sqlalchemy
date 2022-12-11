import datetime

from infos import url

from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, Table, create_engine, DateTime
from sqlalchemy.orm import relationship, sessionmaker, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy_mixins import UserMixin, BaseMixin

from datetime import datetime as dt

engine = create_engine(url=url, echo=False)
session = sessionmaker(bind=engine)()
Base = declarative_base()


class BaseModule(BaseMixin):
    ...
    # todo class BaseMixin will appear in all parent classes
    """ id_ = Column(Integer, primary_key=True, nullable=False)
    created_at = Column(DateTime, server_default=dt.utcnow(), nullable=False)
    updated_at = Column(DateTime, server_default=dt.utcnow(), onupdate=dt.utcnow(), nullable=False)
    """


class Port(BaseModule):
    __tablename__ = "posts"

    # todo class BaseMixin(Base) will appear in class Port(BaseMixin) even tho it is not indicated.
    # todo id: Integer     /   active: Boolean     /   created_at: TIMESTAMP   /   updated_at: TIMESTAMP

    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean,  server_default=True, nullable=False)

