Select
    seller_name
From
    seller
Where
    seller_id not in
    (select seller_id from orders where to_char(sale_date,'YYYY')='2020')
Order by
    seller_name Asc;
