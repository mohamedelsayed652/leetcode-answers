# Write your MySQL query statement below
DELETE T1
FROM Person T1
INNER JOIN Person T2
ON T1.email = T2.email 
AND T1.id > T2.id; 