
INSERT INTO Food_Category(category_id, category_value)
VALUES (1, 'Pizza');

INSERT INTO Food_Category(category_id, category_value)
VALUES (2, 'Salad');

INSERT INTO Food_Category(category_id, category_value)
VALUES (3, 'Burger');

INSERT INTO Food_Category(category_id, category_value)
VALUES (4, 'Drink');

-- Create Food Data

INSERT INTO Food(id, name, category_id, price)
VALUES (1, 'House Special', 1, 19.99);

INSERT INTO Food(id, name, category_id, price)
VALUES (2, 'Thai Dye', 1, 14.99);

INSERT INTO Food(id, name, category_id, price)
VALUES (3, 'Holy Shitake', 1, 21.00);

INSERT INTO Food(id, name, category_id, price)
VALUES (4, 'House Salad', 2, 7.99);

INSERT INTO Food(id, name, category_id, price)
VALUES (5, 'Greek Salad', 2, 7.99);

INSERT INTO Food(id, name, category_id, price)
VALUES (6, 'Ceasar Salad', 2, 9.99);

INSERT INTO Food(id, name, category_id, price)
VALUES (7, 'Cheese Burger', 3, 8.99);

INSERT INTO Food(id, name, category_id, price)
VALUES (8, 'Bacon Burger', 3, 9.99);

INSERT INTO Food(id, name, category_id, price)
VALUES (9, 'My Happy Burger', 3, 12.99);

INSERT INTO Food(id, name, category_id, price)
VALUES (10, 'Soft Drink', 4, 2.99);

INSERT INTO Food(id, name, category_id, price)
VALUES (11, 'Domestic Beer', 4, 1.99);

INSERT INTO Food(id, name, category_id, price)
VALUES (12, 'European Beer', 4, 2.99);

-- Create Server
INSERT INTO Server(id, last_name, first_name)
VALUES (1, 'Son', 'Goku');

INSERT INTO Server(id, last_name, first_name)
VALUES (2, 'Simpson', 'Homer');

INSERT INTO Server(id, last_name, first_name)
VALUES (3, 'Wayne', 'Bruce');

--Create Table
INSERT INTO Restaurant_Table(id, guest_number)
VALUES(1,2);

INSERT INTO Restaurant_Table(id, guest_number)
VALUES(2,4);

INSERT INTO Restaurant_Table(id, guest_number)
VALUES(3,4);

INSERT INTO Restaurant_Table(id, guest_number)
VALUES(4,4);

INSERT INTO Restaurant_Table(id, guest_number)
VALUES(5,6);

INSERT INTO Restaurant_Table(id, guest_number)
VALUES(6,8);