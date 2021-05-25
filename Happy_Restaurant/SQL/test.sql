select * from Food_Category

select *
from Food  join  Food_Category ON Food.category_id = Food_Category.category_id
where (category_value = 'Pizza' or category_value = 'Burger')
    and price > 5
order by category_value


select * from Food

select * from Food

select fc.category_value, count(*)
from Food inner join Food_Category FC on Food.category_id = FC.category_id
group by fc.category_value
