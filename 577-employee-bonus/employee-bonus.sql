# Write your MySQL query statement below

# Join both Employee and Bonus tables based on their empId
# Return each employee name and bonus amount that recieved a bonus less than 1000 or null


SELECT e.name , b.bonus
FROM Employee e
LEFT JOIN Bonus b ON e.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS NULL; 