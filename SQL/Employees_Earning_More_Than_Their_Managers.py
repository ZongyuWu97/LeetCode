# Write your MySQL query statement below
SELECT e1.name AS Employee
FROM Employee AS e1, Employee AS e2
WHERE e1.salary > e2.salary AND e1.managerID = e2.id
