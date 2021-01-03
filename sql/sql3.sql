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


--13
select songid
from table1
where time=curdate()
group by 1
order by count(time) desc
limit 1

select userid1,userid2
from table2 t2 left join table1 t1 on t2.userid1 = t1.userid
left join table1 t3 t2.userid2 =  t3.userid 
where t1.songid = t3.songid
group by 1,2
having count(distinct t2.songid) >= 2

--12
select sum(message_sends)/count(distinct userid)
from t1
where date = somedate and userid not in (select userid from t2 where date = somedate)


select sum(messange_sends-failed_message_sends)/count(distinct t1.userid)
from t1 left join t2 on t1.date = t2.date and t1.userid = t2.userid  
where t2.userid is not null and t1.date = somedate


--11
select u1,u2,count(u1)
from t1 left join t2 on t1.u1 = t2.sender and t1.u2=t2.recipient or t1.u2 = t2.sender or t1.u1 = t2.recepient
group by 1,2


--10
select count(accept_id)/count(1)
from t1 left join t2 on t1.sender_id = t2.request_id and t1.send_to_id = t2.accepter_id
and t1.time <= t2.time
where t2.date = xxx
group by 1,2

select r,count(a)
from 
(select r,a
from r
union
select a,r
from r)
group by 1
order by 2 desc