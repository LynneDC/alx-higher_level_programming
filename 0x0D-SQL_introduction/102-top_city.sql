-- Import in hbtn_0c_0 database this table dump
-- displays top 3 of cities tempe during July and Aug ordered by temp desc
SELECT city, AVG(value) AS avg_temp FROM temperature WHERE month=7 OR month=8 GROUP BY avg_temp DESC LIMIT 3;
