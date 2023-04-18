select c.id, c.name
from customers c
where not exists (select 1 from locations where id_customers = c.id)
order by c.id;