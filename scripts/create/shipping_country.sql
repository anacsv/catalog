-- description
--     Product shipping country table that has relahionship with:
--     product

CREATE TABLE shipping_country (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(64) NOT NULL,
    imported bool,
    PRIMARY KEY (id)
);
