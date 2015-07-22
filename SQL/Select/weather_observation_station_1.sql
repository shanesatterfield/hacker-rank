/*
Weather Observation Station 1
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

Write a query to print the list of CITY and STATE in lexicographical order of city and state, i.e., if there are two or more cities with same name arrange these by lexicographical order of state.
*/

SELECT CITY, STATE
FROM STATION
ORDER BY CITY, STATE;
