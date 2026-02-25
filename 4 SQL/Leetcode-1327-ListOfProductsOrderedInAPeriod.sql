Select
    p.product_name,
    sum(o.unit) as unit
From
    Products p
Join Orders o
    on o.product_id=p.product_id
Where
    o.order_date>='2020-02-01' and
    o.order_date<='2020-02-29'
Group by 
    p.product_name
Having
    sum(o.unit)>=100;
