# Write your MySQL query statement below
SELECT email AS Email
FROM Person
GROUP BY Person.email
HAVING COUNT(Person.email) > 1
