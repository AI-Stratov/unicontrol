CREATE TABLE IF NOT EXISTS Faculty (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Department (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  faculty_id INT,
  FOREIGN KEY (faculty_id) REFERENCES Faculty (id)
);

CREATE TABLE IF NOT EXISTS Teacher (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  surname VARCHAR(255),
  position VARCHAR(255),
  email VARCHAR(255),
  phone VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS TeacherDepartment (
  id SERIAL PRIMARY KEY,
  teacher_id INT,
  department_id INT,
  FOREIGN KEY (teacher_id) REFERENCES Teacher (id),
  FOREIGN KEY (department_id) REFERENCES Department (id)
);

CREATE TABLE IF NOT EXISTS StudentGroups (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  department_id INT,
  FOREIGN KEY (department_id) REFERENCES Department (id)
);

CREATE TABLE IF NOT EXISTS Course (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  description VARCHAR(255),
  duration INT,
  course_type VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS TeacherCourse (
  id SERIAL PRIMARY KEY,
  teacher_id INT,
  course_id INT,
  FOREIGN KEY (teacher_id) REFERENCES Teacher (id),
  FOREIGN KEY (course_id) REFERENCES Course (id)
);

CREATE TABLE IF NOT EXISTS CourseGroup (
  id SERIAL PRIMARY KEY,
  course_id INT,
  group_id INT,
  FOREIGN KEY (course_id) REFERENCES Course (id),
  FOREIGN KEY (group_id) REFERENCES StudentGroups (id)
);

CREATE TABLE IF NOT EXISTS Building (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  address VARCHAR(255),
  city VARCHAR(255),
  postal_code VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Audience (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  capacity INT,
  audience_type VARCHAR(255),
  building_id INT,
  FOREIGN KEY (building_id) REFERENCES Building (id)
);

CREATE TABLE IF NOT EXISTS Semester (
  id SERIAL PRIMARY KEY,
  number INT NOT NULL,
  start_date DATE,
  end_date DATE
);

CREATE TABLE IF NOT EXISTS Student (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  surname VARCHAR(255),
  date_of_birth DATE,
  email VARCHAR(255),
  phone VARCHAR(255),
  group_id INT,
  FOREIGN KEY (group_id) REFERENCES StudentGroups (id)
);

CREATE TABLE IF NOT EXISTS Grade (
  id SERIAL PRIMARY KEY,
  student_id INT,
  course_id INT,
  grade FLOAT,
  grade_date DATE,
  FOREIGN KEY (student_id) REFERENCES Student (id),
  FOREIGN KEY (course_id) REFERENCES Course (id)
);

CREATE TABLE IF NOT EXISTS Schedule (
  id SERIAL PRIMARY KEY,
  course_id INT,
  teacher_id INT,
  building_id INT,
  audience_id INT,
  day VARCHAR(15),
  start_time time,
  end_time time,
  semester VARCHAR(255),
  lesson_type VARCHAR(255),
  FOREIGN KEY (course_id) REFERENCES Course (id),
  FOREIGN KEY (teacher_id) REFERENCES Teacher (id),
  FOREIGN KEY (building_id) REFERENCES Building (id),
  FOREIGN KEY (audience_id) REFERENCES Audience (id)
);

CREATE TABLE IF NOT EXISTS Exam (
  id SERIAL PRIMARY KEY,
  course_id INT,
  date DATE,
  start_time TIME,
  duration INT,
  audience_id INT,
  FOREIGN KEY (course_id) REFERENCES Course (id),
  FOREIGN KEY (audience_id) REFERENCES Audience (id)
);

CREATE TABLE IF NOT EXISTS Assignment (
  id SERIAL PRIMARY KEY,
  course_id INT,
  description VARCHAR(255),
  assignment_date DATE,
  FOREIGN KEY (course_id) REFERENCES Course (id)
);

CREATE TABLE IF NOT EXISTS CourseProgram (
  id SERIAL PRIMARY KEY,
  description VARCHAR(255) NOT NULL,
  duration INT,
  topics VARCHAR(255),
  course_id INT NOT NULL,
  FOREIGN KEY (course_id) REFERENCES Course (id),
  UNIQUE (description, course_id)
);

CREATE TABLE IF NOT EXISTS EducationalPlan (
  id SERIAL PRIMARY KEY,
  semester_id INT NOT NULL,
  course_id INT NOT NULL,
  group_id INT NOT NULL,
  study_form VARCHAR(255),
  hours INT,
  FOREIGN KEY (semester_id) REFERENCES Semester (id),
  FOREIGN KEY (course_id) REFERENCES Course (id),
  FOREIGN KEY (group_id) REFERENCES StudentGroups (id),
  UNIQUE (semester_id, course_id, group_id)
);
