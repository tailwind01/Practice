Select 
    distinct v.customer_id,
    count(v.visit_id) as count_no_trans
From
    Visits v
Where
    v.visit_id not in
        (select visit_id from Transactions)
Group by
    v.customer_id
Order by
    count_no_trans desc, v.customer_id asc;
