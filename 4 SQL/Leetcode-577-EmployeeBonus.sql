-- #v2
Select e.name, b.bonus
from Employee e
Left Join Bonus b on e.empId=b.empId
WHERE e.empId NOT IN (
    SELECT empId 
    FROM Bonus 
    WHERE bonus >= 1000
);

-- #v1
Select e.name, b.bonus
from Employee e
Left join Bonus b on b.empId=e.empId
where bonus<1000 or b.bonus is NULL
