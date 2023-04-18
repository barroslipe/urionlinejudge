(select 'Podium: ' || team "name"
    from league
    order by position asc
    limit 3
)
union all
(select 'Demoted: ' || t.team "name"
from (
    select position, team
    from league
    order by position desc
    limit 2
) t order by t.position asc);