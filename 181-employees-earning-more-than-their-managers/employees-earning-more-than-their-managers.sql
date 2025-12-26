# Write your MySQL query statement below
SELECT e.name as Employee 
FROM employee as e 
JOIN employee as m 
    ON e.managerId = m.Id
WHERE e.salary > m.salary;