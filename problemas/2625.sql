select substring(np.cpf, 1, 3) || '.' || 
       substring(np.cpf, 4, 3) || '.' ||
       substring(np.cpf, 7, 3) || '-' || 
       substring(np.cpf, 10, 2)  "cpf"
from customers c
join natural_person np on np.id_customers = c.id;