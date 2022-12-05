from infos import url

from sqlalchemy import Column, String, Integer, ForeignKey, Table, create_engine
from sqlalchemy.orm import relationship, sessionmaker, backref
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(url=url, echo=False)
session = sessionmaker(bind=engine)()
Base = declarative_base()

root_relationship = Table(
                         'RelationRoot',
                         Base.metadata,
                         Column('root_id', Integer, ForeignKey('root._id', ondelete='cascade')),
                         Column('sub_id', Integer, ForeignKey('sub.sub_id', ondelete='cascade'))
                         )


class Root(Base):
    __tablename__ = "root"

    _id = Column(Integer, primary_key=True, autoincrement=True)   # todo add id Integer -> ****
    var1 = Column(String, nullable=True)     # todo add User String -> ****
    var2 = Column(String, nullable=True)  # todo add User String -> ****
    # todo add relationship -> back populate both table to each other
    subs = relationship('Sub', back_populates='roots', secondary=root_relationship)

    def __repr__(self):     # todo print out as a object like json  sub_id{}, <RootSqlalchemy # 1> instead -> ****
        return f'Item : {self._id}, variable:  {self.var1} , variable: {self.var2}'

    class Config:
        arbitrary_types_allowed = True


class Sub(Base):
    __tablename__ = "sub"

    sub_id = Column(Integer, primary_key=True, autoincrement=True)     # todo add id Integer -> ****
    var1 = Column(String, nullable=True)     # todo add user_id String -> ****
    var2 = Column(String, nullable=True)     # todo add User String -> ****
    # todo add relationship -> back populate both table to each other
    roots = relationship('Root', back_populates='subs', secondary=root_relationship)

    def __repr__(self):     # todo print out as a object like json  sub_id{}, <RootSqlalchemy # 1> instead -> ****
        return f'Item : {self.sub_id}, variable:  {self.var1}, variable : {self.var2}'   # todo root_id{} ****

    class Config:
        arbitrary_types_allowed = True


user_1 = Root(var1="user_1var1", var2="user_1var2")
user_2 = Root(var1="user_2var1", var2="user_2var2")
user_3 = Root(var1="user_3var1", var2="user_3var2")

user_sub_1 = Sub(var1="user_sub_1var1", var2="user_sub_1var2")
user_sub_2 = Sub(var1="user_sub_2var1", var2="user_sub_2var2")
user_sub_3 = Sub(var1="user_sub_3var1", var2="user_sub_3var2")


if __name__ == "__main__":

    Base.metadata.create_all(engine)
    array_list = [user_1, user_2, user_3, user_sub_1, user_sub_2, user_sub_3]

    # Comment out if not going to create Tables and Users

    try:
        session.begin()
        session.add_all(array_list)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()

    RootSqlalchemy = session.query(Root).all()
    for root in RootSqlalchemy:
        # todo Add to Many2Many Table by Root.subs (relationship attribute) and Sub Content
        root.subs.append(user_sub_1)
        root.subs.append(user_sub_2)

    session.commit()

    list(print(_) for _ in RootSqlalchemy)
    SubRootSqlalchemy = session.query(Sub).all()
    list(print(_) for _ in SubRootSqlalchemy)


























# from sqlalchemy import or_, and_, ForeignKey
