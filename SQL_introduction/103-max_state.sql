-- Import in hbtn_0c_0 database the table dump
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state DESC
LIMIT 3