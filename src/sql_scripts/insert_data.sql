-- Добавление тестовых данных для таблицы Faculty
INSERT INTO Faculty (id, name)
VALUES (1, 'Математический факультет'),
       (2, 'Физический факультет'),
       (3, 'Исторический факультет');

-- Добавление тестовых данных для таблицы Department
INSERT INTO Department (id, name, faculty_id)
VALUES (1, 'Отделение математики', 1),
       (2, 'Отделение физики', 2),
       (3, 'Отделение истории', 3);

-- Добавление тестовых данных для таблицы Teacher
INSERT INTO Teacher (id, name, surname, position, email, phone)
VALUES (1, 'Иван', 'Иванов', 'Профессор', 'ivan.ivanov@example.com', '123456789'),
       (2, 'Мария', 'Петрова', 'Доцент', 'maria.petrova@example.com', '987654321'),
       (3, 'Алексей', 'Сидоров', 'Старший преподаватель', 'alexey.sidorov@example.com', '555555555');

-- Добавление тестовых данных для таблицы TeacherDepartment
INSERT INTO TeacherDepartment (teacher_id, department_id)
VALUES (1, 1),
       (2, 2),
       (3, 3);

-- Добавление тестовых данных для таблицы StudentGroups
INSERT INTO StudentGroups (id, name, department_id)
VALUES (1, 'Группа 1', 1),
       (2, 'Группа 2', 2),
       (3, 'Группа 3', 3);

INSERT INTO Student (id, name, surname, date_of_birth, email, phone, group_id)
VALUES (100, 'John', 'Doe', '1995-05-15', 'john.doe@example.com', '123456789', 1),
       (101, 'Jane', 'Smith', '1998-09-20', 'jane.smith@example.com', '987654321', 2),
       (102, 'Alex', 'Johnson', '1997-02-10', 'alex.johnson@example.com', '555555555', 1);

-- Добавление тестовых данных для таблицы Course
INSERT INTO Course (id, name, description, duration, course_type)
VALUES (100, 'Математика', 'Основы математики', 36, 'Обязательный'),
       (101, 'Физика', 'Основы физики', 48, 'Обязательный'),
       (102, 'История', 'Введение в историю', 24, 'Обязательный');

-- Добавление тестовых данных для таблицы TeacherCourse
INSERT INTO TeacherCourse (teacher_id, course_id)
VALUES (1, 100),
       (2, 101),
       (3, 102);

-- Добавление тестовых данных для таблицы CourseGroup
INSERT INTO CourseGroup (course_id, group_id)
VALUES (100, 1),
       (101, 2),
       (102, 3);

-- Добавление тестовых данных для таблицы Building
INSERT INTO Building (id, name, address, city, postal_code)
VALUES (1, 'Здание №1', 'Улица Первая, 1', 'Город', '12345'),
       (2, 'Здание №2', 'Улица Вторая, 2', 'Город', '54321'),
       (3, 'Здание №3', 'Улица Третья, 3', 'Город', '67890');

-- Добавление тестовых данных для таблицы Audience
INSERT INTO Audience (id, name, capacity, audience_type, building_id)
VALUES (1, 'Аудитория 101', 50, 'Лекционная', 1),
       (2, 'Аудитория 201', 30, 'Лекционная', 2),
       (3, 'Аудитория 301', 20, 'Лекционная', 3);

-- Добавление тестовых данных для таблицы Semester
INSERT INTO Semester (number, start_date, end_date)
VALUES (1, '2023-09-01', '2023-12-31'),
       (2, '2024-01-01', '2024-05-31'),
       (3, '2024-09-01', '2024-12-31');

-- -- Добавление тестовых данных для таблицы Grade
-- INSERT INTO Grade (id, student_id, course_id, grade, grade_date)
-- VALUES (1, 1, 100, 4.5, '2023-12-15'),
--        (2, 2, 101, 3.7, '2023-12-15'),
--        (3, 3, 102, 4.2, '2023-12-15');

-- Добавление тестовых данных для таблицы Schedule
INSERT INTO Schedule (course_id, teacher_id, building_id, audience_id, day, start_time, end_time, semester, lesson_type)
VALUES (100, 1, 1, 1, 'Понедельник', '09:00', '11:00', '1', 'Лекция'),
       (101, 2, 2, 2, 'Вторник', '14:00', '16:00', '1', 'Лекция'),
       (102, 3, 3, 3, 'Среда', '10:00', '12:00', '1', 'Лекция');

-- Добавление тестовых данных для таблицы Exam
INSERT INTO Exam (course_id, date, start_time, duration, audience_id)
VALUES (100, '2023-12-20', '10:00', 120, 1),
       (101, '2023-12-22', '14:00', 90, 2),
       (102, '2023-12-25', '09:00', 60, 3);

-- Добавление тестовых данных для таблицы Assignment
INSERT INTO Assignment (id, course_id, description, assignment_date)
VALUES (1, 100, 'Лабораторная работа №3', '2023-09-15'),
       (2, 101, 'Исследовательский проект', '2023-09-15'),
       (3, 102, 'Эссе по истории', '2023-09-15'),
       (4, 100, 'Лабораторная работа №1', '2020-09-15');


-- Добавление тестовых данных для таблицы CourseProgram
INSERT INTO CourseProgram (description, duration, topics, course_id)
VALUES ('Введение в математику', 8, 'Тема 1, Тема 2', 100),
       ('Основы физики', 12, 'Тема 1, Тема 2, Тема 3', 101),
       ('История Древнего мира', 6, 'Тема 1, Тема 2', 102);

-- Добавление тестовых данных для таблицы EducationalPlan
INSERT INTO EducationalPlan (semester_id, course_id, group_id, study_form, hours)
VALUES (1, 100, 1, 'Очная', 100),
       (1, 101, 2, 'Очная', 120),
       (2, 102, 3, 'Очная', 80);
