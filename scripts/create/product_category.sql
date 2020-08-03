-- description
-- Table to save products categories, for example eletronics or games
-- Has relahionship with:
--     product (N:N)

CREATE TABLE product_category (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(64) NOT NULL,
    description text,
    PRIMARY KEY (id)
);
