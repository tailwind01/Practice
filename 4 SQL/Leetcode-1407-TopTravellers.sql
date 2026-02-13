Select u.name, Coalesce(sum(r.distance),0) as travelled_distance
From Users u
Left Join Rides r 
    on u.id=r.user_id
Group by u.name, u.id
Order by travelled_distance Desc, u.name Asc;
