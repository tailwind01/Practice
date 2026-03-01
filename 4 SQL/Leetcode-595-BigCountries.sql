Select
    name,
    population,
    area
From
    world
Where
    area>=3000000 or
    population>=25000000;

-- Alternative solution if OR is inefficient

SELECT name, population, area
FROM world
WHERE area >= 3000000

UNION

SELECT name, population, area
FROM world
WHERE population >= 25000000;
