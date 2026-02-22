Select p.product_id, p.product_name
from Product p
join Sales s on s.product_id = p.product_id
Group by p.product_id, p.product_name
Having min(s.sale_date)>='2019-01-01' and max(s.sale_date)<='2019-03-31';
