select name, (extract(day from payday))::int
from loan;