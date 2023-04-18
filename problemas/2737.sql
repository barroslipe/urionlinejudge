select name, customers_number
from
(
    (select l.name "name", max(l.customers_number) "customers_number"
        from lawyers l
        group by 1 order by 2 desc
        limit 1)
    union all
    (select l.name "name", min(l.customers_number) "customers_number"
        from lawyers l
        group by 1 order by 2 asc
        limit 1)
    union all
    (select 'Average' as "name" , (avg(l.customers_number))::int "customers_number"
        from lawyers l)
)t;