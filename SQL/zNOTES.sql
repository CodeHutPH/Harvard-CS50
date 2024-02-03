-- SELECT -- Retrieve all columns from the 'employees' table where salary is greater than 50000
SELECT * FROM employees WHERE salary > 50000;

-- INSERT a new employee into the 'employees' table
INSERT INTO employees (employee_id, first_name, last_name, salary) VALUES (101, 'John', 'Doe', 60000);

-- UPDATE the salary of the employee with ID 101
UPDATE employees SET salary = 65000 WHERE employee_id = 101;

-- DELETE the employee with ID 101 from the 'employees' table
DELETE FROM employees WHERE employee_id = 101;


--CLAUSES
-- WHERE -- Retrieve employees from the 'sales' department
SELECT * FROM employees WHERE department = 'sales';

-- ORDER BY -- Retrieve employees sorted by their salary in descending order
SELECT * FROM employees ORDER BY salary DESC;

-- GROUP BY -- Calculate the average salary for each department
SELECT department, AVG(salary) as avg_salary FROM employees GROUP BY department;

-- JOIN -- Retrieve employee names along with their department names using a JOIN
SELECT employees.first_name, employees.last_name, departments.department_name
FROM employees
JOIN departments ON employees.department_id = departments.department_id;


--DATA TYPES
-- Create a table 'students' with different data types
CREATE TABLE students (
    student_id INT,
    first_name VARCHAR(50),
    birthdate DATE
);

--PRIMARY AND FOREIGN KEYS
-- Create a table 'orders' with a primary key and a foreign key
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

--NORMALIZATION
-- Before normalization
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    department_location VARCHAR(50)
);

-- After normalization
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department_id INT,
);

CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50),
    location VARCHAR(50)
);

--TRANSACTIONS
-- Start a transaction
--After starting a transaction, any changes made to the database will not be permanent until the transaction is committed.
START TRANSACTION;

-- Perform multiple SQL statements

-- Commit the transaction
COMMIT;

--ROLLBACK
-- Rollback the transaction, undoing any changes made within it
ROLLBACK;


--VIEWS
-- Create a view that combines information from 'employees' and 'departments' tables
CREATE VIEW employee_info AS
SELECT employees.employee_id, employees.first_name, employees.last_name, departments.department_name
FROM employees
JOIN departments ON employees.department_id = departments.department_id;
-- Query the view
SELECT * FROM employee_info;

--INDEXING
-- Create an index on the 'email' column of the 'users' table
CREATE INDEX idx_email ON users(email);


-----------------------------------------------------------------------------------
CSV - comma separated values files
Name,Age,City
John,25,New York
Alice,30,Los Angeles
Bob,22,Chicago
Eva,28,Miami
-----------------------------------------------------------------------------------


