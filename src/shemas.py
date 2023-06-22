"""Схемы для валидации."""
from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class ScriptEnum(str, Enum):
    """Список скриптов."""

    STUDENTS_MATH = "Выбрать всех студентов, обучающихся на курсе Математика."
    UPDATE_GRADE = "Обновить оценку студента по курсу."
    TEACHERS_BUILDING = """Выбрать всех преподавателей,
                        которые преподают в здании №3."""
    DELETE_ASSIGNMENT = """Удалить задание для самостоятельной работы,
                        которое было создано более года назад."""
    ADD_SEMESTER = "Добавить новый семестр в учебный год."


class StudentCreate(BaseModel):
    """Схема для создания студента."""

    name: str
    surname: str
    date_of_birth: date
    email: Optional[str]
    phone: Optional[str]
    group_id: int = Field(..., gt=0)


class StudentGet(BaseModel):
    """Схема для получения студента."""

    id: int
    name: str
    surname: str
    date_of_birth: date
    email: Optional[str]
    phone: Optional[str]
    group_id: int


class StudentUpdate(BaseModel):
    """Схема для обновления студента."""

    name: Optional[str]
    surname: Optional[str]
    date_of_birth: Optional[date]
    email: Optional[str]
    phone: Optional[str]
    group_id: Optional[int]


class Teacher(BaseModel):
    """Схема учителя."""

    id: int
    name: str
    surname: str
    position: str
    email: str
    phone: str


class Course(BaseModel):
    """Схема курса."""

    name: str
    description: str
    duration: int
    course_type: str


class Grade(BaseModel):
    """Схема оценки."""

    student_id: int
    course_id: int
    grade: float
    grade_date: date
