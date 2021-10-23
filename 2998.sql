select name, investment, month "mont_of_payback", retorno "return"
from (
	select * , row_number() over(partition by name order by month) "indice"
	from (
		select c.name, c.investment, o.month, sum(profit) over(partition by c.id order by month) - c.investment "retorno"
		from clients c
		join operations o on o.client_id = c.id
		order by c.id
	) t where t.retorno >= 0
)tn where indice = 1;