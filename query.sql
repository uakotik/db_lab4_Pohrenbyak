--1.Запит, вивести на екран вміст цукру у сніданках кожгого виробника

select m.manufacturer_name,c.sugar
from cereal c
join manufacturer m on m.manufacturer_id=c.manufacturer_id


--2.Запит, вивести на екран частку протеїну у кожному сніданку

select c.name,c.protein
from cereal c


--3.Запит, вивести на екран графік залежності рейтингу від кількості цукру

select r.rating_score,c.sugar 
from rating r 
join cereal c on r.cereal_id=c.cereal_id
join manufacturer m on m.manufacturer_id=c.manufacturer_id
order by rating_score
