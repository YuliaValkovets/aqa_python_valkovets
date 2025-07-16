from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lesson_22.orm_base_table import Base


class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    course_name = Column(String)

    relations = relationship("Relation", back_populates="courses")