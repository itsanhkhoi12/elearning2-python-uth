CREATE DATABASE IF NOT EXISTS course_registration;
USE course_registration;

CREATE TABLE students(
	student_id VARCHAR(10) PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    student_dob DATE NOT NULL,
    student_email VARCHAR(100) UNIQUE NOT NULL,
    student_phonenumber VARCHAR(15) UNIQUE NOT NULL,
    student_address TEXT NOT NULL
    );

CREATE TABLE courses(
	course_id VARCHAR(10) PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    course_description TEXT,
    course_credits INT CHECK (course_credits > 0)
    );

CREATE TABLE enrollment(
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id VARCHAR(10) NOT NULL,
    course_id VARCHAR(10) NOT NULL,
    enrolled_date DATE DEFAULT (CURRENT_DATE),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);