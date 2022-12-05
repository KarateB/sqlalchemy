from infos import url

from sqlalchemy import Column, String, Integer, ForeignKey, Table, create_engine
from sqlalchemy.orm import relationship, sessionmaker, backref
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(url=url, echo=False)
session = sessionmaker(bind=engine)()
Base = declarative_base()



class Root(Base):
    __tablename__ = "Root"

    _id = Column(Integer, primary_key=True, autoincrement=True)   # todo add id Integer -> ****
    var1 = Column(String, nullable=True)     # todo add User String -> ****
    var2 = Column(String, nullable=True)  # todo add User String -> ****
    # todo add relationship -> table_name & backref to assign variable
    subs = relationship('Sub', backref=backref('root'), cascade='all, delete')

    def __repr__(self):     # todo print out as a object like json  sub_id{}, <RootSqlalchemy # 1> instead -> ****
        return f'Item : {self._id}, variable:  {self.var1} , variable: {self.var2}'

    class Config:
        arbitrary_types_allowed = True


class Sub(Base):
    __tablename__ = "Sub"

    sub_id = Column(Integer, primary_key=True, autoincrement=True)     # todo add id Integer -> ****
    var1 = Column(String, nullable=True)     # todo add user_id String -> ****
    var2 = Column(String, nullable=True)     # todo add User String -> ****
    root_id = Column(Integer, ForeignKey('Root._id'))

    def __repr__(self):     # todo print out as a object like json  sub_id{}, <RootSqlalchemy # 1> instead -> ****
        return f'Item : {self.sub_id}, variable:  {self.var1}, variable : {self.var2}, root_id: {self.root_id}'   # todo root_id{} ****

    class Config:
        arbitrary_types_allowed = True


user_1 = Root(var1="user_1var1", var2="user_1var2")
user_2 = Root(var1="user_2var1", var2="user_2var2")
user_3 = Root(var1="user_3var1", var2="user_3var2")

user_sub_1 = Sub(var1="user_sub_1var1", var2="user_sub_1var2", root=user_1)
user_sub_2 = Sub(var1="user_sub_2var1", var2="user_sub_2var2", root=user_2)
user_sub_3 = Sub(var1="user_sub_3var1", var2="user_sub_3var2", root=user_3)

if __name__ == "__main__":

    Base.metadata.create_all(engine)
    array_list = [user_1, user_2, user_3, user_sub_1, user_sub_2, user_sub_3]

    """ # Comment out if not going to create Tables and Users
    session.begin()
    try:
        session.add_all(array_list)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()
    """

    RootSqlalchemy = session.query(Root).all()
    list(print(_) for _ in RootSqlalchemy)
    SubRootSqlalchemy = session.query(Sub).all()
    list(print(_) for _ in SubRootSqlalchemy)

    print()
    user = session.query(Root).filter(Root._id == 2).first()
    print('Call Root from Sub : sub  => ', user.subs[0])

    user = session.query(Sub).filter(Sub.sub_id == 1).first()
    print('Call Sub from Root : root => ', user.root)
