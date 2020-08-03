-- description
--     Product brand table that has relahionship with:
--     product

CREATE TABLE product_brand (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(64) NOT NULL,
    full_name varchar(128),
    PRIMARY KEY (id)
);
