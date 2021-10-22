select e.cpf, e.enome, d.dnome
from empregados e
inner join departamentos d on d.dnumero = e.dnumero
where not exists (select 1 from trabalha where cpf_emp = e.cpf);