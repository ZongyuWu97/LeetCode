# Write your MySQL query statement belo
SELECT Department.name AS Department, Employee.name as Employee, Employee.salary AS Salary
FROM Employee JOIN Department
ON Department.id = Employee.departmentId
WHERE(Department.id, Employee.salary) IN
(
    SELECT Employee.departmentId, MAX(Employee.salary)
    FROM Employee
    GROUP BY Employee.departmentId
)
