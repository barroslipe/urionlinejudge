select c.name, sum(p.amount)
from products p
join categories c on c.id = p.id_categories
group by c.name;