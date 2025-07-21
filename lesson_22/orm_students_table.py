from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lesson_22.orm_base_table import Base


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    student_name = Column(String)

    relations = relationship("Relation", back_populates="students")