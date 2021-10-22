select lr.name, trunc(lr.omega* 1.618, 3) "Factor N"
from life_registry lr
join dimensions d on d.id = lr.dimensions_id
where lr.name like 'Richard%'
and d.name in ('C875', 'C774')
order by 2 asc;