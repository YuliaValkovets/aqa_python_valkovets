from sqlalchemy import create_engine, select, update, delete
from sqlalchemy.orm import sessionmaker
from lesson_22.orm_students_table import Student
from lesson_22.orm_base_table import Base
from lesson_22.orm_courses_table import Course
from lesson_22.orm_relations_table import Relation
from faker import Faker
import random

local_faker = Faker()

# PostgreSQL connection
psql_connect_str = "postgresql://test_user:5248969Blond@localhost:5432/test_db"

# Create database engine and session
engine = create_engine(psql_connect_str)
Session = sessionmaker(bind=engine)
session = Session()

# Create tables
Base.metadata.create_all(engine)

# Add random courses into the database
courses = [Course(course_name=local_faker.job()) for k in range(5)]
session.add_all(courses)
session.commit()

# Add random students into the database
students = [Student(student_name=local_faker.name()) for i in range(20)]
session.add_all(students)
session.commit()

# Create random many to many relations between students and courses
relations = []
for student in students:
    chosen_courses = random.sample(courses, k=random.randint(1, len(courses)))
    for course in chosen_courses:
        relation = Relation(id_student=student.id, id_course=course.id)
        relations.append(relation)
session.add_all(relations)
session.commit()


# Add a new student and assign them to a random course
new_student = Student(student_name="Vasyl Dibrova")
session.add(new_student)
session.commit()

random_course = random.choice(courses)
new_relation = Relation(id_student=new_student.id, id_course=random_course.id)
session.add(new_relation)
session.commit()

# Identify courses assigned to a specific student
student_name = "Vasyl Dibrova"
student = select(Student).where(Student.student_name == student_name)
selected_student = session.execute(student).scalars().first()

if selected_student:
    courses_of_student = (
        select(Course)
        .join(Relation, Course.id == Relation.id_course)
        .where(Relation.id_student == selected_student.id)
                          )
    courses = session.execute(courses_of_student).scalars().all()

    print(f"Student {student_name} attends the following courses:", end = ' ')
    for course in courses:
        print(f"{course.course_name} (id: {course.id})")
else:
    print(f"Student {student_name} isn't found")

# Update course names for courses with a specific id
update_courses = update(Course).where(Course.id < 3).values(course_name = 'IT')
session.execute(update_courses)
session.commit()

# Delete students whose name starts with 'A'
delete_students = delete(Student).where(Student.student_name.like('A%'))
session.execute(delete_students)
session.commit()
