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
where question_id in (select question_id from survey_log 
where event = 'imp'
group by 1
having count(1)>10
) and user_id in (select user_id from survey_log  where question_id = someid  and event = 'answer')
group by 1
order by 2 desc
) q
on u.question_id = q.question_id
where question_id not in (someid)
order by con desc
limit 1



-- 14 
select sum( spend )/count(1)
from (
select advertiser_id,case when sum(price) >0 then 1 else 0 end as spend
from adv_info v left join ad_info i on v.ad_id = v.ad_id
group by 1) result

select advertiser_id,sum(price),sum(spend)
from adv_info v left join ad_info i on v.ad_id = v.ad_id
group by 1

