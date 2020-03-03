-- Script to displays the average temperature (Fahrenheit) by city
-- ordered descending by temperature
SELECT city, AVG(value) as avg_temp FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
