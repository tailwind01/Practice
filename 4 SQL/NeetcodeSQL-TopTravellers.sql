Select
    u.name,
    coalesce(sum(r.distance),0) as travelled_distance
From
    users u
Left Join
    rides r
    On u.id=r.user_id
Group by
    u.name, u.id
Order by
    travelled_distance Desc, u.name Asc;
