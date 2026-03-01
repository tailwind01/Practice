Select
    u.unique_id,
    e.name
From
    EmployeeUNI u
Right join
    Employees e
    on e.id = u.id;
