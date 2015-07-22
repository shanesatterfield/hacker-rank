/*
Weather Observation Station 2
=============================
Given a table STATION that holds data for five fields namely ID, CITY, STATE, NORTHERN LATITUDE and WESTERN LONGITUDE.

+-------------+------------+
| Field       |   Type     |
+-------------+------------+
| ID          | INTEGER    |
| CITY        | VARCHAR(21)|
| STATE       | VARCHAR(2) |
| LAT_N       | NUMERIC    |
| LONG_W      | NUMERIC    |
+-------------+------------+

Write a query to print the sum of LAT_N and LONG_W up to 2 decimal places separated by space.
*/

SELECT CAST(SUM(LAT_N) AS NUMERIC(36,2)), CAST(SUM(LONG_W) AS NUMERIC(36,2))
FROM STATION;
