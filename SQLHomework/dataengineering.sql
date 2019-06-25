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
	"dept_no" VARCHAR NOT NULL,
	"dept_name" VARCHAR NOT NULL,
	CONSTRAINT "pk_departments" PRIMARY KEY (
	"dept_no"
	)
);

SELECT * FROM departments;

CREATE TABLE "dept_emp" (
	"emp_no" INT NOT NULL,
	"dept_no" VARCHAR NOT NULL,
	"from_date" DATE NOT NULL,
	"to_date" DATE NOT NULL
);

SELECT * FROM dept_emp;

CREATE TABLE "dept_manager" (
	"dept_no" VARCHAR(10) NOT NULL,
	"emp_no" INT NOT NULL,
	"from_date" DATE NOT NULL,
	"to_date" DATE NOT NULL
);

SELECT * FROM dept_manager;

CREATE TABLE "employees" (
	"emp_no" INT NOT NULL,
	"birth_date" DATE NOT NULL,
	"first_name" VARCHAR NOT NULL,
	"last_name" VARCHAR NOT NULL,
	"gender" VARCHAR NOT NULL,
	"hire_date" DATE NOT NULL,
	CONSTRAINT "pk_employees" PRIMARY KEY (
	"emp_no"
	)
);

SELECT * FROM employees;

CREATE TABLE "salaries" (
	"emp_no" INT NOT NULL,
	"salary" INT NOT NULL,
	"from_date" DATE NOT NULL,
	"to_date" DATE NOT NULL
);

SELECT * FROM salaries;

CREATE TABLE "titles" (
	"emp_no" INT NOT NULL,
	"title" VARCHAR NOT NULL,
	"from_date" DATE NOT NULL,
	"to_date" DATE NOT NULL
);

SELECT * FROM titles;

-- Create Foreign Keys
ALTER TABLE "dept_emp" ADD CONSTRAINT "fk_dept_emp_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

ALTER TABLE "dept_emp" ADD CONSTRAINT "fk_dept_emp_dept_no" FOREIGN KEY("dept_no")
REFERENCES "departments" ("dept_no");

ALTER TABLE "dept_manager" ADD CONSTRAINT "fk_dept_manager_dept_no" FOREIGN KEY("dept_no")
REFERENCES "departments" ("dept_no");

ALTER TABLE "dept_manager" ADD CONSTRAINT "fk_dept_manager_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

ALTER TABLE "salaries" ADD CONSTRAINT "fk_salaries_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

ALTER TABLE "titles" ADD CONSTRAINT "fk_titles_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");



