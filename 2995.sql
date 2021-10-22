select temperature, number_of_records
from (
select temperature, mark, count(*) "number_of_records"
from records
group by temperature, mark
order by mark
) t;