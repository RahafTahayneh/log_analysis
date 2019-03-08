create view popular_articles as
select title, count (log.time) as num from log, articles
where path = concat('/article/', slug)
and status = '200 OK'
group by title
order by num desc
limit 3;


create view popular_authors as
select name, count(log.time) as num from authors, articles, log
where author = authors.id
and path = concat('/article/', slug)
and status = '200 OK'
group by authors.name
order by num desc;

create view days_with_more_than_one_percent_errors as
select date(time) as log_date, round(count(error_log.id) * 100 /count(log.id)::decimal, 2) as percent
from log left join (select id from log where status LIKE '4%' or status LIKE '5%') as error_log
on log.id = error_log.id
group by log_date
having round(count(error_log.id) * 100 /count(log.id)::decimal, 2) > 1;
