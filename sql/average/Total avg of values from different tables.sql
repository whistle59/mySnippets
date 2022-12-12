/*
drop table orders_issued;
drop table orders_executed;

create table orders_issued (
	distributor_id int,
	company_id int,
	quotation_date char(10)
);

create table orders_executed (
	orders_from int,
	executed_fron int,
	execited_date Char(10)
);

insert into orders_issued values  		   (101,       202,    '2019-11-15');
insert into orders_issued values             (101,       203,    '2019-11-15');
insert into orders_issued values             (101,       204,    '2019-11-15');
insert into orders_issued values             (102,       202,    '2019-11-16');
insert into orders_issued values             (102,       201,    '2019-11-15');
insert into orders_issued values             (103,       203,    '2019-11-17');
insert into orders_issued values             (103,       202,    '2019-11-17');
insert into orders_issued values             (104,       203,    '2019-11-18');
insert into orders_issued values             (104,       204,    '2019-11-18');


insert into orders_executed values (101,          202,   '2019-11-17');
insert into orders_executed values (101,          203,   '2019-11-17');
insert into orders_executed values (102,          202,   '2019-11-17');
insert into orders_executed values (103,          203,   '2019-11-18');
insert into orders_executed values (103,          202,   '2019-11-19');
insert into orders_executed values (104,          203,   '2019-11-20');
*/

/*WARNING: IN ORACLE YOU MUST SPECIFY A FROM CLAUSE. USE "FROM DUAL" IN SUCH A CASE (IT'S A PSEUDO-TABLE)*/
with tmp as (
select
	(select cast(count(*) as float) from orders_executed) as dividendo,
	(select cast(count(*) as float) from orders_issued) as divisor
)
select dividendo,
		divisor,
	cast(dividendo / divisor as decimal(10,2)) as result
from tmp;
