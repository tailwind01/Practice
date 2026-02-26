Select
  name,
  ROUND(population/1000000,2) as popn_millions,
  ROUND(gdp/1000000000,2) as GDP_billions
From
  world
Where
  continent = 'South America'
