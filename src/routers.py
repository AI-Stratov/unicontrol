from typing import List

from fastapi import APIRouter, HTTPException, Query

from src.database import Database
from src.shemas import (Course, Grade, ScriptEnum, StudentCreate, StudentGet,
                        StudentUpdate, Teacher)

router = APIRouter()
db = Database()
db.connect()


@router.get("/execute_script")
def execute_script(
    script: ScriptEnum = Query(
        ..., description="Выберите скрипт для выполнения"
    )
):
    script_path = f"src/sql_scripts/{script.name.lower()}.sql"
    try:
        db.execute_script(script_path)

        result = []
        message = f"Скрипт {script.value} выполнен успешно"

        if (
            script == ScriptEnum.STUDENTS_MATH
            or script == ScriptEnum.TEACHERS_BUILDING
        ):
            result = db.fetchall()

        elif script == ScriptEnum.UPDATE_GRADE:
            message = "Оценка студента обновлена успешно"

        elif script == ScriptEnum.DELETE_ASSIGNMENT:
            message = "Задание удалено успешно"

        elif script == ScriptEnum.ADD_SEMESTER:
            message = "Новый семестр добавлен успешно"

        return {"message": message, "result": result}

    except Exception as e:
        return {"error": str(e)}


@router.post("/students", response_model=StudentCreate)
def create_student(student: StudentCreate):
    try:
        query = """
            INSERT INTO Student (name, surname, date_of_birth, email, phone, group_id)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id, name, surname, date_of_birth, email, phone, group_id
        """
        values = (
            student.name,
            student.surname,
            student.date_of_birth,
            student.email,
            student.phone,
            student.group_id,
        )
        db.execute_query(query, values)

        created_students = db.fetchall()
        db.conn.commit()

        if created_students:
            created_student = created_students[0]
            return StudentCreate(
                id=created_student[0],
                name=created_student[1],
                surname=created_student[2],
                date_of_birth=created_student[3],
                email=created_student[4],
                phone=created_student[5],
                group_id=created_student[6],
            )
    except Exception as e:
        db.conn.rollback()
        raise HTTPException(
            status_code=500, detail="Ошибка при добавлении студента"
        ) from e


@router.get("/students/{student_id}", response_model=StudentGet)
def get_student(student_id: int):
    try:
        query = """
            SELECT id, name, surname, date_of_birth, email, phone, group_id
            FROM Student
            WHERE id = %s
        """
        values = (student_id,)
        db.execute_query(query, values)

        student_data = db.fetchone()

        if student_data is not None:
            return StudentGet(
                id=student_data[0],
                name=student_data[1],
                surname=student_data[2],
                date_of_birth=student_data[3],
                email=student_data[4],
                phone=student_data[5],
                group_id=student_data[6],
            )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="Ошибка при получении студента"
        ) from e


@router.put("/students/{student_id}", response_model=StudentUpdate)
def update_student(student_id: int, updated_data: StudentUpdate):
    try:
        query = """
            UPDATE Student
            SET name = %s, surname = %s, date_of_birth = %s, email = %s, phone = %s, group_id = %s
            WHERE id = %s
            RETURNING id, name, surname, date_of_birth, email, phone, group_id
        """
        values = (
            updated_data.name,
            updated_data.surname,
            updated_data.date_of_birth,
            updated_data.email,
            updated_data.phone,
            updated_data.group_id,
            student_id,
        )
        db.execute_query(query, values)

        updated_student = db.fetchone()
        db.conn.commit()

        if updated_student:
            return StudentUpdate(
                id=updated_student[0],
                name=updated_student[1],
                surname=updated_student[2],
                date_of_birth=updated_student[3],
                email=updated_student[4],
                phone=updated_student[5],
                group_id=updated_student[6],
            )
    except Exception as e:
        db.conn.rollback()
        raise HTTPException(
            status_code=500, detail="Ошибка при обновлении данных о студенте"
        ) from e


@router.delete("/students/{student_id}")
def delete_student(student_id: int):
    try:
        query = "DELETE FROM Student WHERE id = %s"
        values = (student_id,)
        db.execute_query(query, values)
        rows_affected = db.cursor.rowcount
        db.conn.commit()
        if rows_affected == 0:
            raise HTTPException(status_code=404, detail="Студент не найден.")
        return {"message": "Студент успешно удален."}
    except Exception as e:
        db.conn.rollback()
        raise HTTPException(
            status_code=500, detail="Ошибка при удалении студента."
        ) from e


@router.get("/teachers", response_model=List[Teacher])
def get_teachers():
    try:
        query = """
            SELECT id, name, surname, position, email, phone
            FROM Teacher
        """
        db.execute_query(query)
        teachers_data = db.fetchall()

        teachers = []
        for row in teachers_data:
            teacher = Teacher(
                id=row[0],
                name=row[1],
                surname=row[2],
                position=row[3],
                email=row[4],
                phone=row[5],
            )
            teachers.append(teacher)

        return teachers
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Ошибка при получении списка преподавателей.",
        ) from e


@router.post("/courses", response_model=dict)
def create_course(course: Course):
    try:
        query = """
            INSERT INTO Course (name, description, duration, course_type)
            VALUES (%s, %s, %s, %s)
            RETURNING id
        """
        values = (
            course.name,
            course.description,
            course.duration,
            course.course_type,
        )
        db.execute_query(query, values)
        db.conn.commit()

        course_id = db.fetchone()[0]
        return {"course_id": course_id, "message": "Курс создан успешно"}
    except Exception as e:
        db.conn.rollback()
        raise HTTPException(
            status_code=500, detail="Ошибка при создании курса."
        ) from e


@router.get("/courses/{course_id}", response_model=Course)
def get_course(course_id: int):
    try:
        query = "SELECT * FROM Course WHERE id = %s"
        values = (course_id,)
        db.execute_query(query, values)
        course = db.fetchone()
        if course:
            return Course(
                course_id=course[0],
                name=course[1],
                description=course[2],
                duration=course[3],
                course_type=course[4],
            )
        else:
            raise HTTPException(status_code=404, detail="Курс не найден")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="Ошибка при получении курса"
        ) from e


@router.get("/courses/{course_id}/students", response_model=List[StudentGet])
def get_course_students(course_id: int):
    try:
        course_exists = db.check_data_exists("course", "id", course_id)
        if not course_exists:
            raise HTTPException(status_code=404, detail="Курс не найден.")

        query = """
        SELECT s.id, s.name, s.surname, s.date_of_birth, s.email, s.phone
        FROM Student s
        INNER JOIN StudentGroups sg ON s.group_id = sg.id
        INNER JOIN CourseGroup cg ON sg.id = cg.group_id
        WHERE cg.course_id = %s
        """
        values = (course_id,)
        db.execute_query(query, values)
        students = db.fetchall()

        student_list = []
        for student in students:
            student_info = StudentGet(
                id=student[0],
                name=student[1],
                surname=student[2],
                date_of_birth=student[3],
                email=student[4],
                phone=student[5],
            )
            student_list.append(student_info)

        return student_list

    except Exception as e:
        raise HTTPException(
            status_code=500, detail="Ошибка при получении студентов."
        ) from e


@router.post("/grades", response_model=Grade)
def create_grade(grade: Grade):
    try:
        if not db.check_data_exists("student", "id", grade.student_id):
            raise HTTPException(status_code=404, detail="Студент не найден")
        if not db.check_data_exists("course", "id", grade.course_id):
            raise HTTPException(status_code=404, detail="Курс не найден")

        query = """
        INSERT INTO Grade (student_id, course_id, grade, grade_date)
        VALUES (%s, %s, %s, %s)
        """
        values = (
            grade.student_id,
            grade.course_id,
            grade.grade,
            grade.grade_date,
        )
        db.execute_query(query, values)
        db.conn.commit()

        return Grade(
            student_id=grade.student_id,
            course_id=grade.course_id,
            grade=grade.grade,
            grade_date=grade.grade_date,
        )
    except Exception as e:
        db.conn.rollback()
        raise HTTPException(
            status_code=500, detail="Ошибка при создании оценки."
        ) from e


@router.put("/grades/{grade_id}", response_model=Grade)
def update_grade(grade_id: int, grade: Grade):
    try:
        if not db.check_data_exists("grade", "id", grade_id):
            raise HTTPException(status_code=404, detail="Оценка не найдена")

        query = """
        UPDATE Grade
        SET grade = %s
        WHERE id = %s
        """
        values = (grade.grade, grade_id)
        db.execute_query(query, values)
        db.conn.commit()

        return grade
    except Exception as e:
        db.conn.rollback()
        raise HTTPException(
            status_code=500, detail="Ошибка при изменении оценки",
        ) from e
