Select employee_id, 
       department_id
From Employee
Where 
    primary_flag='Y' or
    employee_id not in (select employee_id from Employee group by employee_id having count(employee_id)>1)
Order by employee_id;
