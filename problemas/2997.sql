select 
    nome_departamento "Departamento", 
    empregado "Empregado",
    credito "Salario Bruto" ,
    debito "Total Desconto",
    credito - debito "Salario Liquidoaws"
from (
    select
        nome_departamento,
        nome_divisao,
        matricula,
        empregado,
        credito,
        sum(coalesce(descont.valor, 0)) "debito"
    from (
        select 
            depart.nome "nome_departamento", 
            divi.nome "nome_divisao", 
            emp.matr "matricula",
            emp.nome "empregado",
            sum(coalesce(venc.valor, 0)) "credito"
        from divisao divi
        join departamento depart on depart.cod_dep = divi.cod_dep
        join empregado emp on emp.lotacao_div = divi.cod_divisao
        left join emp_venc empvenc on empvenc.matr = emp.matr
        left join vencimento venc on venc.cod_venc = empvenc.cod_venc
        group by 1, 2, 3, 4
    )t1 left join emp_desc empdesc on empdesc.matr = t1.matricula
    left join desconto descont on descont.cod_desc = empdesc.cod_desc
    group by 1, 2, 3, 4, 5
)t2
order by 5 desc;