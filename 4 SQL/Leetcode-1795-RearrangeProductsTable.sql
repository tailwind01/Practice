-- for postgres
SELECT p.product_id, s.store, s.price
FROM Products p
CROSS JOIN LATERAL (
    VALUES 
        ('store1', store1),
        ('store2', store2),
        ('store3', store3)
) AS s(store, price)
WHERE s.price IS NOT NULL;


-- for MSSQL Server/Oracle
--
Select product_id, store, price
From Products
UNPIVOT (
    price FOR Store in (store1,store2,store3)
) As unpivoted;
