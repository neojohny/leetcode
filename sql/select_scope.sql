--subjects
--students

select s.id, ifnull(count(name), 0)
from subjects s left join students st on st.subjectid = s.subjectid
group by 1;


select name, s.id
from subjects s left join students st on st.subjectid = s.subjectid
where name = 'Jack';

select *
from subjects 
where subjectid not in (
    select subjectid
    from students
    where name in ('Jack','Alice')
);

with phy as (
    select * from students 
    where subjectid = 2
), chem as (
    select * from students
    where subjectid = 3
)
select DISTINCT phy.name 
from phy inner join chem on phy.name = chem.name


-----------------------

SELECT TABLE.*, LEAD(QUERY,1) OVER (partition BY USERID ORDER BY TIMESTAMP) AS NEWCOLUMN
FROM TABLE ;



SELECT DISTINCT USERID, LAST_vALUE(QUERY) OVER (partition BY USERID ORDER BY TIMESTAMP) AS LASTQUERY
FROM TABLE;


SELECT USERID, ARRAY_AGG(MARKET)
FROM TABLE 
GROUP BY 1;

WITH 
SELECT DISTINCT USERID,MARKET
FROM TABLE

--MARKETS
--A,EN-US EN-US,EN-CA
--A,EN-CA  EN-US,EN-CA

----------------

