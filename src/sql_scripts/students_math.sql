-- Выбрать всех студентов, обучающихся на курсе "Математика":
SELECT Student.*
FROM Student
JOIN StudentGroups ON Student.group_id = StudentGroups.id
JOIN CourseGroup ON StudentGroups.id = CourseGroup.group_id
JOIN Course ON CourseGroup.course_id = Course.id
WHERE Course.name = 'Математика';

