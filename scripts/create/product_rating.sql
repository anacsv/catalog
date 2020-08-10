-- description
-- Table to save products hating, for example if the product
-- is good or bad, depending on its score.
-- Has relahionship with:
--     product (1:1)

CREATE TABLE product_rating (
    id int NOT NULL AUTO_INCREMENT,
    score int NOT NULL,
    status varchar(64) NOT NULL,
    PRIMARY KEY (id)
);
