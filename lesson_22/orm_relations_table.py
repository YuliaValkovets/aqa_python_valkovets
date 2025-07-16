from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from lesson_22.orm_base_table import Base


class Relation(Base):
    __tablename__ = 'relations'

    id = Column(Integer, primary_key=True)
    id_student = Column(Integer, ForeignKey("students.id", ondelete="CASCADE"))
    id_course = Column(Integer, ForeignKey("courses.id", ondelete="CASCADE"))

    students = relationship("Student", back_populates="relations")
    courses = relationship("Course", back_populates="relations")


