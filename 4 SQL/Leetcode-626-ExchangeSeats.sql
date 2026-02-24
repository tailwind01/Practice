Select 
    Case
        when id % 2=0 then id-1
        when id%2 !=0 and id<(select max(id) from seat) then id+1
        else id
    END as id,
         student
From Seat
Order by id Asc;
