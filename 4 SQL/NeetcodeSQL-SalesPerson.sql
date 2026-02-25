Select
    name
From
    sales_person
Where
    sales_id not in
    (select sales_id from orders where com_id=1)
