Select 
    name
From 
    customers
Where
    id not in 
        (select distinct customer_id from orders)
