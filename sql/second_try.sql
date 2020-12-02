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

select date, user_id
from (
select date,send_id user_id ,receive_id to_id from message
union
select date,receive_id,send_id from message) as total
group by 1,2
having count(distinct to_id) > 5