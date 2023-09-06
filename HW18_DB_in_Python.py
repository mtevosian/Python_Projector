# Add models for student, subject and student_subject from previous lessons in SQLAlchemy.
import psycopg2
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

connection = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='masyas',
    port=5432,
)

cursor = connection.cursor()
with connection.cursor() as curs:
    curs.execute("CREATE TABLE student (id serial PRIMARY KEY, name VARCHAR(50) NOT NULL, age INT NOT NULL);")
    curs.execute("CREATE TABLE subject (id serial PRIMARY KEY, name VARCHAR(50) NOT NULL)")
    curs.execute("CREATE TABLE student_subject (id serial PRIMARY KEY, student_id INT NOT NULL, subject_id INT NOT NULL, FOREIGN KEY (student_id) REFERENCES student (id), FOREIGN KEY (subject_id) REFERENCES subject (id));")
    curs.execute("INSERT INTO student (name, age) VALUES ('Bae', 18), ('Eddy', 21), ('Lily', 22), ('Jenny', 19);")
    curs.execute("INSERT INTO subject (name) VALUES ('English'), ('Math'), ('Spanish'), ('Ukrainian');")
    curs.execute("INSERT INTO student_subject (student_id, subject_id) VALUES (1, 1), (2, 2), (3, 3), (4, 4), (1, 3);")


Base = sqlalchemy.orm.declarative_base()

class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

class Subject(Base):
    __tablename__ = 'subject'

    id = Column(Integer, primary_key=True)
    name = Column(String)

class student_subject(Base):
    __tablename__ = 'student_subject'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'))
    subject_id = Column(Integer, ForeignKey('subject.id'))


# Find all students` name that visited 'English' classes.

DATABASE_URI = 'postgresql://{user}:{password}@{host}:{port}/{database}'

engine = create_engine(
    DATABASE_URI.format(
        host='localhost',
        database='postgres',
        user='postgres',
        password='masyas',
        port=5432,
    )
)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

english = session.query(Subject).filter(Subject.name == 'English').first()
english_students = session.query(student_subject).filter(student_subject.subject_id == english.id).order_by(student_subject.student_id.asc()).all()
english_students_names = session.query(Student).filter(Student.id == english_students.student_id).order_by(Student.name.asc()).all()

print(english_students_names.name)

