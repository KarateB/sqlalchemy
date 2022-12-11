from infos import url

from sqlalchemy import Column, String, Boolean, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_mixins import UserMixin, BaseMixin

from datetime import datetime as dt

engine = create_engine(url=url, echo=False)
session = sessionmaker(bind=engine)()
Base = declarative_base()


class UserModule(UserMixin):
    ...
    # todo class BaseMixin will appear in all parent classes
    """ id_ = Column(Integer, primary_key=True, nullable=False)
    created_at = Column(DateTime, server_default=dt.utcnow(), nullable=False)
    updated_at = Column(DateTime, server_default=dt.utcnow(), onupdate=dt.utcnow(), nullable=False)
    """


class Port(BaseMixin, UserModule):
    __tablename__ = "posts"

    # todo class BaseMixin(Base) will appear in class Port(BaseMixin) even tho it is not indicated.
    # todo id: Integer     /   active: Boolean     /   created_at: TIMESTAMP   /   updated_at: TIMESTAMP

    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean,  server_default="TRUE", nullable=False)

    @property
    def port_title(self):
        return self.title

    @property
    def port_content(self):
        return self.content

    def __repr__(self):
        _dict = dict()
        _dict_names = [a for a, b in Port.__dict__.items() if '_' not in str(a[::2])]

        for i in range(len(_dict_names)):
            _dict[str(_dict_names[i])] = str(getattr(self, _dict_names[i]))

        return str(_dict)


port = Port()
port.id = 1
port.created_at = dt.utcnow()
port.updated_at = dt.utcnow()
port.published = True
port.title = "New Title 1"
port.content = "A new content 1"

port_2 = Port()
port_2.id = 2
port_2.created_at = dt.utcnow()
port_2.updated_at = dt.utcnow()
port_2.published = True
port_2.title = "A New Title 2"
port_2.content = "A new content 2"

list(print(_) for _ in [port, port_2])


