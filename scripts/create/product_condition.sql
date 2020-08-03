-- description
--     Product condition table that has relahionship with:
--     product

CREATE TABLE product_condition (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(32) NOT NULL,
    description text,
    PRIMARY KEY (id)
);
