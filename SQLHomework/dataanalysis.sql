-- Database: Employee80s90s_db

-- DROP DATABASE "Employee80s90s_db";

CREATE DATABASE "Employee80s90s_db"
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

COMMENT ON DATABASE "Employee80s90s_db"
    IS 'SQL Homework';
	
	--Data Analysis--
	-- 1. List the following details of each employee: employee number, last name, first name, gender, and salary
	
	SELECT e.emp_no AS Employee_Number, e.last_name AS Last_Name, e.first_name AS First_Name, e.gender AS Gender, 
	s.salary AS Salary
	FROM employees e
	JOIN salaries s
	ON e.emp_no = s.emp_no;
	
	-- 2. List employees who were hired in 1986
	
	SELECT * 
	FROM employees e
	WHERE hire_date BETWEEN '1986-01-01' AND '1986-12-31'
	
	-- 3. List the manager of each department with the following information: department number,
	-- department name, the manager's employee number, last name, first name, and start and end employment dates.
	SELECT d.dept_no AS Department_Number, d.dept_name AS Department_Name, 
	m.emp_no AS Managers_Employee_Number, e.last_name AS Last_Name, e.first_name AS First_Name, 
	m.from_date AS Start_Employment_Dates, m.to_date AS End_Employment_Dates  
	FROM departments d
	JOIN dept_manager m
	ON (d.dept_no = m.dept_no)
		JOIN employees e
		ON (m.emp_no = e.emp_no);
		
	-- 4. List the department of each employee with the following information: employee number, last name, first name
	-- and, department name.
	
	
	
	
	
	
	
	
	
	
	
	
	
	