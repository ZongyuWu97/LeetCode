# Write your MySQL query statement below
SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE -30 < DATEDIFF(activity_date, '2019-07-27') AND DATEDIFF(activity_date, '2019-07-27') <= 0
GROUP BY day