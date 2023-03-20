# Write your MySQL query statement below
select name, bonus
FROM Employee left outer join Bonus
on Employee.empId = Bonus.empId
where bonus < 1000
or bonus is null
