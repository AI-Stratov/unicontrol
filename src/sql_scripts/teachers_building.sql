-- Выбрать всех преподавателей, которые преподают в здании №3:
SELECT DISTINCT Teacher.*
FROM Teacher
JOIN TeacherDepartment ON Teacher.id = TeacherDepartment.teacher_id
JOIN Department ON TeacherDepartment.department_id = Department.id
JOIN StudentGroups ON Department.id = StudentGroups.department_id
JOIN CourseGroup ON StudentGroups.id = CourseGroup.group_id
JOIN Course ON CourseGroup.course_id = Course.id
JOIN Schedule ON Course.id = Schedule.course_id
JOIN Building ON Schedule.building_id = Building.id
WHERE Building.name = 'Здание №3';


