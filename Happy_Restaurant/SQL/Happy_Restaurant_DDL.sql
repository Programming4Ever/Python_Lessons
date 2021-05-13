

/*
drop table Restaurant_Order_Items;
drop table Restaurant_Order;
drop table Restaurant_Table;
drop table Server;
drop table Food;
drop table Food_Category;


 */

CREATE TABLE Food_Category(
	category_id INT Primary Key,
	category_value VARCHAR(50)
);

CREATE TABLE Food(
	id INT primary key,
	name VARCHAR(100),
	category_id INT,
	price FLOAT,
	FOREIGN KEY(category_id) REFERENCES Food_Category(category_id)
);

CREATE TABLE Server(
	id INT Primary Key,
	first_name VARCHAR(50),
	last_name VARCHAR(50)
);

CREATE TABLE Restaurant_Table(
	id INT Primary Key,
	guest_number int
);

CREATE TABLE Restaurant_Order(
	id INT Primary Key,
	table_number int,
	server_id int,
	number_of_guest int,
	order_date timestamp,
	FOREIGN KEY (table_number) REFERENCES Restaurant_Table(id),
	FOREIGN KEY (server_id) REFERENCES Server(id)
);

CREATE TABLE Restaurant_Order_Items(
	id INT Primary Key,
	guest_number int,
	menu_item int,
	restaurant_order_id int,
    FOREIGN KEY(menu_item) REFERENCES Food(id),
    FOREIGN KEY(restaurant_order_id) REFERENCES Restaurant_Order(ID)
);





