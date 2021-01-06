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


--9
select date,count(sessionid)/count(distinct userid)
from session
where datediff(day,date,curdate())<=30

select total,count(user)
from (
select user,sum(time_spent) total 
from
session s left join time t on t.sessionid = s.sessionid
group by 1) result


--8
select to,count(target_id) from (
select target_id,count(content_id) to
from comment
where target_id is not null)
group by 1

select type,to,count(content_id) from (
select p.type,p.content_id,count(c.content_id) as to
from comment p left join comment c on p.content_id = c.target_id 
group by 1,2
) result 
group by 1,2

--7

select sum(case when status = 'fraud' then 1 else 0 end)/count(ad_account)
from table
where spend >0

select count(distinct account)
from table
where status = 'fraud' and date = curdate()

--6
select sum(clicks),sum(displays)
from table 
where date = somedate

select user,sum(clicks)/sum(displays)*1.0
from table
group by 1

select group,sum(clicks)/sum(display)
from table
group by 1


--5 
select extra,count(distinct post_id)
from spam
where date - curdate() = 1 and action = 'report'
group by 1


select date,user,sum(case when review_id is not null then 1 else 0 end)/ count(distinct post_id)
from table t left join remove r on t.post_id = r.post_id
where action = 'report'
group by 1,2


select user,count(review_id),count(distinct post_id)
from table t left join remove r on t.post_id = r.post_id
where action = 'report'  and datediff(date,curdate()) <= 30
group by 1 


--4
select country,ifnull(sum(cost),0)
from  users u left join ad4ad a on a.user_id = u.user_id
where datediff(date,curdate())<=30
group by 1


select t.user_id,sum(case when event = impression then 1 else 0 end)
(select * from table where event = 'create_ad') c
left join table t on t.ad_id = c.ad_id and t.user_id = c.user_id
group by 1


-- 1
select date,sum(when event = 'post' then 1 else 0 end)/nullif(sum(case when event = 'enter' then 1 else 0 end),0)
from composer 
where datediff(date,curdate) <=7
group by 1


select date,country,sum(case when event = 'post' then 1 else 0)/count(distinct u.user_id)
from user u left join composer c on c.user_id = u.user_id and c.date = u.date
where dau_flag = 1 and date = curdate() 
group by 1,2

-- 2
select date,sum(num)/count(num)
from (
select date,send_id,sum(case when count(distinct receive_id)>5 then 1 else 0 end)/count(send_id) num
from
(select * from message
union
select * from message) result 
group by 1,2)
group by 1
--having count(distinct receive_id)


--3 
select country,sum(type)
from sms 
where datediff(date,curdate())=1 and type = 'confirmation'
group by 1

select cell_number 
from sms
where type = 'confirmation' and datediff(date,curdate())<=7
having count(distinct date)>=7
group by 1

select date,count(distinct c.cell_number)/count(distinct s.cell_number)
from sms s left join confirmation c on s.cell_number = c.cell_number
where datediff(date,curdate()) <= 30 and type = 'confirmation'
group by 1


---------------------
-- spam 刷

select extra,count(distinct post_id)
from user_actions
where curdate() - ds = 1 and action = 'report'
group by 1


select u.ds, count(distinct r.postid)/count(distinct u.post_id)
from user_actions u left join revewer_removals r on u.post_id = r.post_id
group by u.ds

select user_id, count(distinct r.postid)/count(distinct u.post_id)
from user_actions u left join review r on r.post_id = u.post_id
where u.action = 'report' and datediff(curdate(),ds) < = 30
group by 1