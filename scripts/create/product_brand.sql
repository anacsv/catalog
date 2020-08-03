-- description
-- Table to save products brands, for example Olist.
-- Has relahionship with:
--     product (1:1)

CREATE TABLE product_brand (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(64) NOT NULL,
    full_name varchar(128),
    PRIMARY KEY (id)
);
