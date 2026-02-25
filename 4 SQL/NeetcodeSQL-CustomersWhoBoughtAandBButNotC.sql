Select 
    c.customer_id,
    c.customer_name
From
    Customers c
Join
    Orders o
    on c.customer_id=o.customer_id
    where
        c.customer_id in
        (Select distinct customer_id 
        from orders 
        where product_name='A') 
        and
        c.customer_id in 
        (Select distinct customer_id 
        from orders 
        where product_name='B') 
        and
        c.customer_id not in 
        (Select distinct customer_id 
        from orders 
        where product_name='C')
Group by
    c.customer_id
Order by
    c.customer_name Asc;
