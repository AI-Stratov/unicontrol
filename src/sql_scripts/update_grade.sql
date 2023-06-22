-- Обновить оценку студента по курсу:
UPDATE Grade
SET grade = 5
WHERE student_id = 1 AND course_id = 1;
