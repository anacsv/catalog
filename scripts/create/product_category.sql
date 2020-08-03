-- description
--     Product category that has relahionship with:
--     product_category 

CREATE TABLE product_category (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(64) NOT NULL,
    description text,
    PRIMARY KEY (id)
);
