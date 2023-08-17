-- Import in hbtn_0c_0 database this table dump:
--  display average temp by city ordered by temp desc
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
