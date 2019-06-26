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
	-- Once there is a complete database, do the following: 
	-------------------------------------------------------------------------------------------------------------
	
	-- 1. List the following details of each employee: employee number, last name, first name, gender, and salary
	-- Results: 300,024 rows affected
	SELECT e.emp_no AS Employee_Number, e.last_name AS Last_Name, e.first_name AS First_Name, e.gender AS Gender, 
	s.salary AS Salary
	FROM employees e
	JOIN salaries s
	ON e.emp_no = s.emp_no;
	
	
	-- 2. List employees who were hired in 1986
	-- Results: 36,150 rows affected
	
	SELECT * 
	FROM employees e
	WHERE hire_date BETWEEN '1986-01-01' AND '1986-12-31';
	
	
	-- 3. List the manager of each department with the following information: department number,
	-- department name, the manager's employee number, last name, first name, and start and end employment dates.
	-- Results: 24 rows affected
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
	-- Results: 331,603 rows affected
	SELECT de.emp_no AS Employee_Number, e.last_name AS Last_Name, e.first_name AS First_Name, d.dept_name AS Department_Name   
	FROM dept_emp de
	JOIN employees e
	ON (de.emp_no = e.emp_no)
		JOIN departments d
		ON (de.dept_no = d.dept_no);
		
	-- This also gets us the same results for question #4
	-- Results: 331,603 rows affected
	SELECT e.emp_no AS Employee_Number, e.last_name AS Last_Name, e.first_name AS First_Name, d.dept_name AS Department_Name   
	FROM departments d
	JOIN dept_emp de
	ON (d.dept_no = de.dept_no)
		JOIN employees e
		ON (de.emp_no = e.emp_no);
		
	-- 5. List all employees whose first name is "Hercules" and last name begins with "B."
	-- Results: 20 rows affected
	SELECT e.first_name, e.last_name
	FROM employees e
	WHERE e.first_name = 'Hercules'
	AND e.last_name LIKE 'B%';
	
	
	
	
	
	
	
	
	
	
	
	
	