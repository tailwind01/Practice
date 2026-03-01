-- MySQL solution:

SELECT id
FROM (
    SELECT id,
           temperature > LAG(temperature) OVER (ORDER BY recordDate) AS increased,
           DATEDIFF(recordDate, LAG(recordDate) OVER (ORDER BY recordDate)) AS DayDiff
    FROM Weather    
) AS temp_check
WHERE increased IS TRUE AND DayDiff = 1;

-- PostgreSQL solution:

SELECT id
FROM (
    SELECT id,
           temperature > LAG(temperature) OVER (ORDER BY recordDate) AS increased,
           recordDate-LAG(recordDate) OVER (ORDER BY recordDate) AS DayDiff
    FROM Weather    
) AS temp_check
WHERE increased IS TRUE AND DayDiff = 1;
