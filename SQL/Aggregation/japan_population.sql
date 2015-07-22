/*
Japan Population
================
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

you have to print the sum of population of all the cities of Japan. The CountryCode for Japan is "JPN".
*/

SELECT SUM(Population)
FROM City
WHERE CountryCode='JPN';
