select name, trunc(0.1*salary, 2)
from people
where salary > 3000;