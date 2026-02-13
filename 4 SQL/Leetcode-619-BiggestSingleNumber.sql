select coalesce(
              (Select num From MyNumbers group by num Having (count(num)=1) Order by num Desc Limit 1),
              Null) 
            as num 
        from MyNumbers 
    limit 1;
