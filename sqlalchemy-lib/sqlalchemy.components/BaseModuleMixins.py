import datetime

from infos import url

from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, Table, create_engine, DateTime
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

    def __repr__(self):
        _return = f' < \n' \
                  f' id : {self.id}\n ' \
                  f'created_at: {self.created_at}\n ' \
                  f'updated_at: {self.updated_at}\n ' \
                  f'title: {self.title}\n ' \
                  f'content: {self.content}\n ' \
                  f'published: {self.published}\n ' \
                  f'>'
        return _return


port = Port()
port.id = 1
port.created_at = dt.utcnow()
port.updated_at = dt.utcnow()
port.published = True
port.title = "New Title with a lot of content and fun."
port.content = "A new content with a lot of content and fun."
print(port)


