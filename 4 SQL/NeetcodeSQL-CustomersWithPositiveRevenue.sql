Select 
    customer_id
From 
    customers
Group by
    customer_id, year
Having
    sum(revenue)>0 and
    year = '2020'
