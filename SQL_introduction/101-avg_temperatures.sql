-- Import in hbtn_0c_0 database the table dump
SELECT city, AVG(value) AS avg_tmp
FROM temperatures
GROUP BY city
ORDER BY avg_tmp DESC