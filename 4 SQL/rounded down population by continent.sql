#/tailwind
select country.continent, floor(avg(city.population)) from country, city where city.countrycode=country.code group by country.continent
