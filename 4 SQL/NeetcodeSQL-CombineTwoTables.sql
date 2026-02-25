Select 
    p.first_name,
    p.last_name,
    a.city,
    a.state
From
    person p
Left join
    address a
    on p.person_id=a.person_id

