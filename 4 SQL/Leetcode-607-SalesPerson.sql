Select distinct(sp.name) from SalesPerson sp
Left Join orders o on o.sales_id=sp.sales_id
Where sp.sales_id not in 
(Select sales_id from orders o 
    join Company c on c.com_id = o.com_id
    where c.name='RED')
