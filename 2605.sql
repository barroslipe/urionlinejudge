select prod.name, prov.name 
from products prod
join providers prov on prov.id = prod.id_providers
where prod.id_categories = 6;