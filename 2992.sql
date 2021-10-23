select 
	departamento,
	divisao,
	media
from(
	select
		departamento,
		divisao,
		media,
	    row_number() over(partition by departamento order by media desc)
	from (
		select 
		    nome_departamento "departamento", 
		    nome_divisao "divisao", 
		    round(avg(credito-debito), 2) "media"
		from (
		    select
		        nome_departamento,
		        nome_divisao,
		        matricula,
		        credito,
		        sum(coalesce(descont.valor, 0)) "debito"
		    from (
		        select 
		            depart.nome "nome_departamento", 
		            divi.nome "nome_divisao", 
		            emp.matr "matricula", 
		            sum(coalesce(venc.valor, 0)) "credito"
		        from divisao divi
		        join departamento depart on depart.cod_dep = divi.cod_dep
		        join empregado emp on emp.lotacao_div = divi.cod_divisao
		        left join emp_venc empvenc on empvenc.matr = emp.matr
		        left join vencimento venc on venc.cod_venc = empvenc.cod_venc
		        group by 1, 2, 3
		    )t1 left join emp_desc empdesc on empdesc.matr = t1.matricula
		    left join desconto descont on descont.cod_desc = empdesc.cod_desc
		    group by 1, 2, 3, 4
		)t2 group by 1, 2
	)t3
)t4 where row_number = 1
order by media desc;