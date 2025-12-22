#/ average population of city in California
select sum(population)/count(name) from city where district = "California"
