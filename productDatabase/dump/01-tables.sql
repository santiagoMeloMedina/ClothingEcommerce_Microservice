
-- tables
-- Table: category
CREATE TABLE category (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(100) NOT NULL,
    description text NOT NULL,
    CONSTRAINT category_pk PRIMARY KEY (id)
);

-- Table: discount
CREATE TABLE discount (
    id int NOT NULL AUTO_INCREMENT,
    product_id int NOT NULL,
    state bool NOT NULL,
    deadline date NOT NULL,
    porcentage double NOT NULL,
    CONSTRAINT discount_pk PRIMARY KEY (id)
);

CREATE INDEX discount_product_id ON discount (product_id);

-- Table: product
CREATE TABLE product (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(100) NOT NULL,
    description text NOT NULL,
    price double(50,4) NOT NULL,
    created date NOT NULL,
    active bool NOT NULL,
    CONSTRAINT product_pk PRIMARY KEY (id)
);

-- Table: characteristic
CREATE TABLE characteristic (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(100) NOT NULL,
    content json NOT NULL,
    CONSTRAINT characteristic_pk PRIMARY KEY (id)
);

-- Table: product_characteristic
CREATE TABLE product_characteristic (
    id int NOT NULL AUTO_INCREMENT,
    charact_id int NOT NULL,
    product_id int NOT NULL,
    CONSTRAINT product_characteristic_pk PRIMARY KEY (id)
);

-- Table: product_category
CREATE TABLE product_category (
    id int NOT NULL AUTO_INCREMENT,
    category_id int NOT NULL,
    product_id int NOT NULL,
    CONSTRAINT product_category_pk PRIMARY KEY (id)
);

-- foreign keys
-- Reference: discount_product (table: discount)
ALTER TABLE discount ADD CONSTRAINT discount_product FOREIGN KEY discount_product (product_id)
    REFERENCES product (id) ON DELETE CASCADE;

-- Reference: product_category_category (table: product_category)
ALTER TABLE product_category ADD CONSTRAINT product_category_category FOREIGN KEY product_category_category (category_id)
    REFERENCES category (id) ON DELETE CASCADE;

-- Reference: product_category_product (table: product_category)
ALTER TABLE product_category ADD CONSTRAINT product_category_product FOREIGN KEY product_category_product (product_id)
    REFERENCES product (id) ON DELETE CASCADE;

ALTER TABLE product_characteristic ADD CONSTRAINT product_characteristic_characteristic FOREIGN KEY product_characteristic_characteristic (charact_id)
    REFERENCES characteristic (id) ON DELETE CASCADE;

ALTER TABLE product_characteristic ADD CONSTRAINT product_characteristic_product FOREIGN KEY product_characteristic_product (product_id)
    REFERENCES product (id) ON DELETE CASCADE;