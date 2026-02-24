Select id,
        sum(case when month='Jan' then revenue else Null end) as Jan_Revenue,
        sum(case when month='Feb' then revenue else Null end) as Feb_Revenue,
        sum(case when month='Mar' then revenue else Null end) as Mar_Revenue,
        sum(case when month='Apr' then revenue else Null end) as Apr_Revenue,
        sum(case when month='May' then revenue else Null end) as May_Revenue,
        sum(case when month='Jun' then revenue else Null end) as Jun_Revenue,
        sum(case when month='Jul' then revenue else Null end) as Jul_Revenue,
        sum(case when month='Aug' then revenue else Null end) as Aug_Revenue,
        sum(case when month='Sep' then revenue else Null end) as Sep_Revenue,
        sum(case when month='Oct' then revenue else Null end) as Oct_Revenue,
        sum(case when month='Nov' then revenue else Null end) as Nov_Revenue,
        sum(case when month='Dec' then revenue else Null end) as Dec_Revenue
    From Department
    Group by id
    Order by id
