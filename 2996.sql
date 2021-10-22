select p.year, u.name "sender", u2.name "receiver"
from packages p
join users u on u.id = p.id_user_sender
join users u2 on u2.id = p.id_user_receiver
where (p.color = 'blue'
or p.year = 2015)
and u.address != 'Taiwan'
and u2.address != 'Taiwan';