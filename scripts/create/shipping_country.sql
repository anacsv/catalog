-- description
-- Table to save products shipping country, for example
-- if its national ou imported
-- Has relahionship with:
--     product (1:1)

CREATE TABLE shipping_country (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(64) NOT NULL,
    imported bool,
    PRIMARY KEY (id)
);
