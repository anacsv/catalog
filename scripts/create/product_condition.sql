-- description
-- Table to save products condition, for example if the product
-- is new.
-- Has relahionship with:
--    product (1:1)

CREATE TABLE product_condition (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(32) NOT NULL,
    description text,
    PRIMARY KEY (id)
);
