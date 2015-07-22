/*
Population Density Difference
=============================
Given a City table, whose fields are described as

+-------------+----------+
| Field       | Type     |
+-------------+----------+
| ID          | int(11)  |
| Name        | char(35) |
| CountryCode | char(3)  |
| District    | char(20) |
| Population  | int(11)  |
+-------------+----------+

print the difference between the maximum and minimum city populations.
*/

SELECT MAX(Population) - MIN(Population)
FROM City;
