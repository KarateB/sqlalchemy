from infos import url

from sqlalchemy import Column, String, Integer, Boolean, create_engine, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_mixins import UserMixin, BaseMixin

from datetime import datetime as dt
import uuid as ud

engine = create_engine(url=url, echo=False)
session = sessionmaker(bind=engine)()
Base = declarative_base()

listItems = []


class UserModule(UserMixin):
    ...
    # todo class BaseMixin will appear in all parent classes
    """ id_ = Column(Integer, primary_key=True, nullable=False)
    created_at = Column(DateTime, server_default=dt.utcnow(), nullable=False)
    updated_at = Column(DateTime, server_default=dt.utcnow(), onupdate=dt.utcnow(), nullable=False)
    """
    xid = Column(Integer, nullable=False)
    id = Column(Integer, primary_key=True, nullable=False)
    created_at = Column(DateTime, server_default=str(dt.utcnow()), nullable=False)
    updated_at = Column(DateTime, server_default=str(dt.utcnow()), onupdate=str(dt.utcnow()), nullable=False)

    @property
    def fid(self):
        return self.id

    @property
    def fxid(self):
        return self.xid

    @property
    def fc_at(self):
        return self.created_at

    @property
    def fup_at(self):
        return self.updated_at

    @fid.setter
    def fid_set(self, new_value):
        self.id = str(ud.uuid4())
        if not new_value:
            raise ValueError('Exception is raised')


    @fc_at.setter
    def fc_at_set(self, new_value):
        self.created_at = dt.utcnow()
        if not new_value:
            raise ValueError('Exception is raised')

    @fup_at.setter
    def fup_at_set(self, new_value):
        self.updated_at = dt.utcnow()
        if new_value:
            raise ValueError('Exception is raised')


class Port(BaseMixin, UserModule):
    __tablename__ = "posts"

    # todo class BaseMixin(Base) will appear in class Port(BaseMixin) even tho it is not indicated.
    # todo id: Integer     /   active: Boolean     /   created_at: TIMESTAMP   /   updated_at: TIMESTAMP

    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    deleted = Column(Boolean,  server_default="TRUE", nullable=False)

    def __repr__(self):
        _dict = dict()
        _dict_names = [a for a, b in Port.__dict__.items() if '_' not in str(a[::2])]

        for i in range(len(_dict_names)):
            _dict[str(_dict_names[i])] = str(getattr(self, _dict_names[i]))

        return str(_dict)


def add_items(n) -> None:
    for i in range(1, n):
        port = Port()
        port.title = "title " + str(i)
        port.content = "content " + str(i)
        port.id = str(ud.uuid4())[:8]
        port.created_at = dt.utcnow()
        port.updated_at = dt.utcnow()
        port.deleted = False
        port.active = True
        port.xid = i
        listItems.append(port)


add_items(5001)
list(print(_) for _ in listItems)


