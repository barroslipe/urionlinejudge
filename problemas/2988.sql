select
name,
matches,
victories,
defeats,
draws,
(victories*3 + draws*1) "score"
from (
select name,
(select count(*) from matches where t.id in (team_1, team_2)) "matches",
(select count(*) from matches where (t.id = team_1 and team_1_goals > team_2_goals) or (t.id = team_2 and team_2_goals > team_1_goals)) "victories",
(select count(*) from matches where (t.id = team_1 and team_2_goals > team_1_goals) or (t.id = team_2 and team_1_goals > team_2_goals))  "defeats",
(select count(*) from matches where t.id in (team_1, team_2) and (team_1_goals = team_2_goals)) "draws"
from teams t
) nt
order by 6 desc;