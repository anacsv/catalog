-- description
--     Product product category that has relahionship with:
--     product 
--     product_category 


CREATE TABLE product_product_category (
    product_category_id int,
    product_id int
);
ALTER TABLE product_product_category
ADD CONSTRAINT fk_product_category
FOREIGN KEY (product_category_id) REFERENCES product_category(id);
ALTER TABLE product_product_category
ADD CONSTRAINT fk_product
FOREIGN KEY (product_id) REFERENCES product(id);
