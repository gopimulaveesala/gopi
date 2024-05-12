use restaurant_db;


-- 1. view the menu_item table.
select * from menu_items;

-- 2. find the number of items on the menu.
select count(*)from menu_items;

-- 3. what are the least and most expensive item on the menu?
select* from menu_items
order by price desc;

-- 4. how many Italian dishes are on the menu?
select count(*) from menu_items
where category = "Italian";

-- 5. what are the least and most expensive Italian dishes on the menu?
select * from menu_items
where category = "Italian" order by price desc;

-- 6. How many dishes are in each category?
select category, count(menu_item_id) as num_dishes from menu_items group by category;

-- 7. what is the average dish price within each category?
select category, avg(price) as avg_price from menu_items group by category;
