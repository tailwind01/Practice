-- It may be noted that Neetcode runs PostgreSQL only

Select 
    employee_id,
    Case
        When employee_id%2=1 and name not like 'M%' then salary
        Else 0
    END as bonus
From
    employees
Order by
    employee_id Asc;
