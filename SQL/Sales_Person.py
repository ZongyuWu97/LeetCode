# Write your MySQL query statement below
SELECT name FROM SalesPerson AS s
WHERE s.sales_id
NOT IN (
SELECT o.sales_id FROM Orders AS o
WHERE o.com_id 
IN (SELECT c.com_id FROM Company AS c WHERE c.name = 'RED'))