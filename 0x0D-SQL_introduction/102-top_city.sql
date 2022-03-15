-- Top 3 cities temperature in july an august.
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month BETWEEN 7 and 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
