--1. composer; userid event(enter, post, cancel) date
--1.1 post success rate for each day in the last week
select date, 
        round(
            ifnull(
                sum(case when event = 'post' then 1 else 0 end)/
                nullif(sum(case when event = 'enter' then 1 else 0 end),0)
            ,0),2)
from composer 
where datediff(curdate(),date)<=7
group by 1

-- 1.2 user: userid,date,country,dau_flag
-- average number of post per daily active user by country today

select country, sum(case when event = 'post' then 1 else 0 end)/count(distinct userid)
from country c left join composer cp on c.userid = cp.userid and c.date = cp.date
where dau_flag = 1 and date = curdate()
group by 1 


--2.  message date, timestamp,  send_id, receive_id
-- fraction of users communicatin to > 5 users in a day

select date, user_id,
round(ifnull(sum( case when count(distinct to_id) > 5 then 1 
else 0 end)/nullif(count(distinct user_id),0),0),2) as fraction
from (
select date,send_id user_id ,receive_id to_id from message
union
select date,receive_id,send_id from message) as total
group by 1,2
--having count(distinct to_id) > 5


-- 3. sms_message date, country cell_number, carrier, type
--confirmation date cell_number
--3.1 yesterday how many confirmation texts by country


select country,count(1)
from sms_message 
where datediff(curdate(),date) = 1 and type = 'confirmation'
group by 1

--3.2 number of users who received notification every single day during the last 7 days.
select cell_number
from sms_message
where datediff(curdate,date)<=7 and type = 'notification'
group by 1        
having count(distinct date ) = 7 

--3.3 last 30 day's confirmation rate
select sum(case when c.cell_number is not null then 1 else 0 end)/count(1)
from sms_message s left join confirmation c on c.date = s. date and c.cell_number = s.cell_number
where type = 'confirmation' and datediff(curdate(),date)<=30




-- 4 ad4ad date; user_id; event; unit_id, cost, spend, ad_id
--users user_uid,country,age

-- 4.1 
select country, date, sum(cost)
from ad4ad ad left join users u on u.user_id = ad.user_id
where datediff(curdate(),date)<=30 
group by 1,2

select user_id,unit_id,sum(case when event = 'impression' then 1 else 0 end) from ad4ad left join 
(select user_id,unit_id
from ad4ad
where ad_id is not null) c on c.user_id = ad4ad.user_id and ad4ad.unit_id = c.unit_id
group by 1,2


select avg(cc)
select unit_id,user_id,sum(case when event = 'impression' then 1 else 0) cc
(select distinct user_id, unit_id 
from ad4ad
where event = 'create_ad') c
left join ad4ad on c.user_id = a.user_id and c.unit_id = a.unit_id
group by 1,2