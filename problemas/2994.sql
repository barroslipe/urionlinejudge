select d.name, round(sum(a.hours*150 + a.hours*150*ws.bonus/100), 1) "salary"
from attendances a
join work_shifts ws on ws.id = a.id_work_shift
join doctors d on d.id = a.id_doctor
group by 1
order by 2 desc;