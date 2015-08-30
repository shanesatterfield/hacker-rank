/*
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

Write a query to find the sum of the Northern Latitudes having values greater than 38.7880 and less than 137.2345 up to 4 decimal places.
*/

SELECT ROUND(SUM(LAT_N),4)
FROM STATION
WHERE 38.7880 <= LAT_N AND LAT_N <= 137.2345;
