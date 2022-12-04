from sqlalchemy import create_engine, Column, Integer, String, or_, and_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from infos import url


engine = create_engine(url=url, echo=False)
session = sessionmaker(bind=engine)()
Base = declarative_base()


class Student(Base):
    __tablename__ = 'TableName'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))

    def __init__(self, age, name, grade):
        self.age = age
        self.name = name
        self.grade = grade

    def __repr__(self):
        return f'id: {self.id}, name: {self.name}, age:{self.age}, grade: {self.grade}'


Base.metadata.create_all(engine)

# todo Add Student by assigning attributes in Student Class
student1 = Student(
    name="SomeName1",
    age=32,
    grade="SomeType1"
)
student2 = Student(
    name="SomeName2",
    age=26,
    grade="SomeType2"
)
student3 = Student(
    name="SomeName3",
    age=61,
    grade="SomeType4"
)
student4 = Student(
    name="SomeName4",
    age=58,
    grade="SomeType4"
)

if __name__ == "__main__":

    session.add(student1)
    session.add(student2)
    # # todo or just do
    session.add_all([student3, student4])
    session.commit()

    # todo Get all data
    students = session.query(Student)
    for student in students:
        print(student.id, student.name, student.age, student.grade)
    print('----------------------------')
    # todo Get Data in order
    students = session.query(Student).order_by(Student.name)
    for student in students:
        print(student.id, student.name, student.age, student.grade)
    print('----------------------------')
    # todo Get Data by filtering
    students = session.query(Student).filter(Student.age >= 32)
    for student in students:
        print(student.id, student.name, student.age, student.grade)
    print('----------------------------')
    # todo or bring the first result
    students = session.query(Student).filter(Student.age == 32).first()
    print(students.id, students.name, students.age, students.grade)
    print('----------------------------')
    # todo Common Filter Operators
    # todo do a or statement
    students = session.query(Student).filter(or_(Student.age == 32, Student.name == 'Koray'))
    for student in students:
        print(student.id, student.name, student.age, student.grade)
    print('----------------------------')
    # todo do a and statement
    students = session.query(Student).filter(and_(Student.age == 32, Student.name == 'Berkay'))
    for student in students:
        print(student.id, student.name, student.age, student.grade)
    print('----------------------------')
    # todo do a like statement
    students_like = session.query(Student).filter(Student.name.like('%be%')).first()
    print(students_like)
    print('----------------------------')
    # todo Count of results
    students_count = session.query(Student).filter(Student.age > 26).count()
    print(students_count)
    print('----------------------------')


    # todo update record by
    student_to_update = session.query(Student).filter(Student.age == 32).first()
    student_to_update.name = 'Berkay Karatay'
    session.commit()

    # todo delete record by
    student_to_delete = session.query(Student).filter(Student.age == 32).first()
    session.delete(student_to_delete)
    session.commit()
