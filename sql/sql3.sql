--15.
select question_id,
sum(case when event = 'answered' then 1 else 0 end)/sum(case when event = 'imp' then 1 else 0 end) as con
from survey_log
where id in (select question_id from survey_log 
where event = 'imp'
group by 1
having count(1)>10
)
group by 1
order by 2 desc

select u.question_id from
(select user_id , question_id from survey_log where user_id = some id) u
inner join 
(select question_id,
sum(case when event = 'answered' then 1 else 0 end)/sum(case when event = 'imp' then 1 else 0 end) as con
from survey_log
where id in (select question_id from survey_log 
where event = 'imp'
and question_id = someid
group by 1
having count(1)>10 and question_id
)
group by 1
order by 2 desc
) q
on u.question_id = q.question_id
where question_id not in (someid)
order by con desc
limit 1