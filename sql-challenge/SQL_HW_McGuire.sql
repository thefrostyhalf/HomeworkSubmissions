use sakila;

#1a
select first_name as "First Name", last_name as "Last Name" from actor;
# 1b
select upper(concat(first_name,' ', last_name)) as 'Actor Name'
from actor;
# 2a
SELECT actor_id, first_name, last_name from actor where actor.first_name = 'Joe';
# 2b
SELECT * from actor where last_name like '%gen%';
# 2c
SELECT last_name, first_name from actor where last_name like '%li%' 
ORDER BY last_name, first_name asc;
# 2d
SELECT country_id, country from country where 
country in ('Afghanistan', 'Bangladesh', 'China');
#3a
ALTER TABLE actor
add COLUMN middle_name varchar(50) AFTER first_name;
# 3b
alter table actor 
change column middle_name middle_name BLOB;
# 3c
alter table actor
drop column middle_name;
# 4a
select last_name,  count(*) as 'Count' 
from actor group by last_name;
# 4b
select last_name, count(*) as 'Count'
from actor group by last_name having count(*) >= 2;
# 4c
UPDATE actor
set first_name = (case when first_name = 'groucho' then 'HARPO'
else  'MUCHO GROUCHO'
end)
WHERE first_name = 'GROUCHO' and last_name = 'WILLIAMS';
# 4d
select staff.first_name, staff.last_name, address.address
from staff
inner join address on staff.address_id = address.address_id;
# 5a
select table_schema from information_schema.TABLES where table_name = 'address';
#6a
select staff.first_name, staff.last_name, address.address from staff
join address on staff.address_id = address.address_id;
#6b
select staff.first_name, staff.last_name, sum(payment.amount) as 'Total' 
from staff 
inner join payment on staff.staff_id = payment.staff_id
where payment.payment_date like '2005-08%'
group by staff.staff_id;
# 6c
select title, count(film_actor.actor_id) as 'Actor Count'
from film inner join film_actor on film.film_id = film_actor.film_id
group by film_actor.film_id;
# 6d
select count(*) as 'Inventory Count' from inventory
where film_id in (select film_id from film
where title="Hunchback Impossible");
# 6e
select customer.last_name, customer.first_name, sum(payment.amount) as 'customer_total'
from customer
inner join payment on customer.customer_id = payment.customer_id
group by customer.customer_id
ORDER BY customer.last_name asc;
# 7a
select title from film where film_id in 
(select film_id from language where language_id in(select language_id from language where name = 'English') )
and title like 'q%' or title like 'k%';
# 7b
select actor.first_name as 'First Name',actor.last_name as 'Last Name' from actor where actor_id in 
(select actor_id from film_actor where film_id in
(select film_id from film where title = 'Alone Trip')
);
# 7c
select customer.first_name, customer.last_name, customer.email from customer 
join address on customer.address_id = address.address_id 
join city on address.city_id = city.city_id
join country on city.country_id = country.country_id
where country = 'Canada';
# 7d
select film.film_id as 'Film ID', film.title as 'Film Title' from film where film_id in 
(select film_id from film_category where category_id in
(select category_id from category where name = 'family'));
# 7e
select film.title, count(rental.rental_date) as Count from film
join inventory on film.film_id = inventory.film_id
join rental on rental.inventory_id = inventory.inventory_id
group by film.title
order by Count desc;
#  7f
select store.store_id, sum(payment.amount) as Sales from store
join staff on store.store_id = staff.store_id
join payment on staff.staff_id = payment.staff_id
group by store.store_id;
# 7g
select store.store_id as ID, city.city as City, country.country as Country from store
join address on store.address_id = address.address_id
join city on address.city_id = city.city_id
join country on city.country_id = country.country_id
group by store.store_id;
# 7h
select category.name, sum(payment.amount) as Sales from category
join film_category on category.category_id = film_category.category_id
join film on film_category.film_id = film.film_id
join inventory on film.film_id = inventory.film_id
join rental on inventory.inventory_id = rental.inventory_id
join payment on rental.rental_id = payment.rental_id
group by category.name
order by Sales desc
limit 5;
# 8a
create view top_five_genres as
select category.name, sum(payment.amount) as Sales from category
join film_category on category.category_id = film_category.category_id
join film on film_category.film_id = film.film_id
join inventory on film.film_id = inventory.film_id
join rental on inventory.inventory_id = rental.inventory_id
join payment on rental.rental_id = payment.rental_id
group by category.name
order by Sales desc
limit 5;
# 8b
select * from top_five_genres;
# 8c
drop view top_five_genres;
