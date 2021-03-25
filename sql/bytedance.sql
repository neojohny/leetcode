--id, date
--1, 2010-01-01
--2, 2010-01-01
--3, 2010-01-01
--1, 2010-01-02
--3, 2010-01-02
--1, 2010-01-03

with dif as (
    select id,date,row_number() over (partition by id) -
                datediif(date - min(date) over (partition by id order by date)) as class
    from table
), result as (
    select id,class,min(date),max(date),count(1)
    from dif
    group by 1,2
)