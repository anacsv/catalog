-- description
    -- Product table that has relashionships with:
    -- product_brand
    -- product_condition
    -- shipping_country
    -- product_hating


CREATE TABLE product (
    id int NOT NULL AUTO_INCREMENT,
    description text,
    name varchar(128),
    price NUMERIC,
    gtin varchar(128),
    brand_id int,
    product_condition_id int,
    shipping_country_id int,
    product_hating_id int,
    PRIMARY KEY (id)
);
ALTER TABLE product
ADD CONSTRAINT fk_product_brand
FOREIGN KEY (brand_id) REFERENCES product_brand(id);
ALTER TABLE product
ADD CONSTRAINT fk_product_condition
FOREIGN KEY (product_condition_id) REFERENCES product_condition(id);
ALTER TABLE product
ADD CONSTRAINT fk_shipping_country
FOREIGN KEY (shipping_country_id) REFERENCES shipping_country(id);
ALTER TABLE product
ADD CONSTRAINT fk_product_hating
FOREIGN KEY (product_hating_id) REFERENCES product_hating(id);