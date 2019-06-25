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
	
	SELECT e.emp_no, e.last_name, e.first_name, e.gender, s.salary
	FROM employees e
	JOIN salaries s
	ON e.emp_no = s.emp_no;
	
	-- 2. List employees who were hired in 1986
	
	
	
	
	
	