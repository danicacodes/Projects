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
	
--Data Engineering--
--Drop Tables if Existing
DROP TABLE departments;
DROP TABLE dept_emp;
DROP TABLE dept_manager;
DROP TABLE employees;
DROP TABLE salaries;
DROP TABLE titles;

-- Create Tables
-- Import Data Using Import/Export Option in PgAdmin
CREATE TABLE "departments" (
	"dept_no" VARCHAR(10) NOT NULL,
	"dept_name" VARCHAR(30) NOT NULL,
	CONSTRAINT "pk_departments" PRIMARY KEY (
	"dept_no"
	)
);

SELECT * FROM departments;

CREATE TABLE "dept_emp" (
	"emp_no" INT NOT NULL,
	"dept_no" VARCHAR(10) NOT NULL,
	"from_date" DATE NOT NULL,
	"to_date" DATE NOT NULL
);

SELECT * FROM dept_emp;

