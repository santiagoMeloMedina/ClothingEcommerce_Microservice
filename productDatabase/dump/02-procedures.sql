
DELIMITER $$
DROP PROCEDURE IF EXISTS addProduct;
CREATE PROCEDURE addProduct(IN nm varchar(100), IN dsc text, IN prc double(50,4))
BEGIN
    INSERT INTO product (name, description, price, created, active) VALUES (nm, dsc, prc, NOW(), false);
    SELECT LAST_INSERT_ID() as rows;
END$$
DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS addProductCategory;
CREATE PROCEDURE addProductCategory(IN pid int, IN cid int)
BEGIN
    INSERT INTO product_category (product_id, category_id) VALUES (pid, cid);
    SELECT LAST_INSERT_ID() as rows;
END$$
DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS addDiscount;
CREATE PROCEDURE addDiscount(IN pid int, IN st bool, IN dline date, IN porctg double)
BEGIN
    INSERT INTO discount (product_id, state, deadline, porcentage) VALUES (pid, st, dline, porctg);
    SELECT LAST_INSERT_ID() as rows;
END$$
DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS addCharacteristic;
CREATE PROCEDURE addCharacteristic(IN nm varchar(100), IN contnt json)
BEGIN
    INSERT INTO characteristic (name, content) VALUES (nm, contnt);
    SELECT LAST_INSERT_ID() as rows;
END$$
DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS addCharacteristicProduct;
CREATE PROCEDURE addCharacteristicProduct(IN cid int, IN pid int)
BEGIN
    INSERT INTO product_characteristic (charact_id, product_id) VALUES (cid, pid);
    SELECT LAST_INSERT_ID() as rows;
END$$
DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS updateProductState;
CREATE PROCEDURE updateProductState(IN pid int)
BEGIN
    UPDATE product SET active=true WHERE id=pid;
    SELECT active as rows FROM product WHERE id=pid;
END$$
DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS updateDiscountState;
CREATE PROCEDURE updateDiscountState(IN did int)
BEGIN
    UPDATE discount SET state=NOT state WHERE id=did;
    SELECT state as rows FROM discount WHERE id=did;
END$$
DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS updateProduct;
CREATE PROCEDURE updateProduct(IN pid int, IN nm varchar(100), IN dsc text, IN prc double(50,4), IN crtd date)
BEGIN
    UPDATE product SET name=nm, description=dsc, price=prc, created=crtd WHERE id=pid;
    SELECT ROW_COUNT() as rows;
END$$
DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS updateCharacteristic;
CREATE PROCEDURE updateCharacteristic(IN cid int, IN nm varchar(100), IN cntnt json)
BEGIN
    UPDATE characteristic SET name=nm, content=cntnt WHERE id=cid;
    SELECT ROW_COUNT() as rows;
END$$
DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS deleteProduct;
CREATE PROCEDURE deleteProduct(IN pid int)
BEGIN
    DELETE FROM product WHERE id=pid;
    SELECT ROW_COUNT() as rows;
END$$
DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS addCategory;
CREATE PROCEDURE addCategory(IN nm varchar(100), IN dsc text)
BEGIN
    INSERT INTO category (name, description) VALUES (nm, dsc);
    SELECT LAST_INSERT_ID() as rows;
END$$
DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS updateCategory;
CREATE PROCEDURE updateCategory(IN cid int, IN nm varchar(100), IN dsc text)
BEGIN
    UPDATE category SET name=nm, description=dsc WHERE id=cid;
    SELECT ROW_COUNT() as rows;
END$$
DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS deleteCategory;
CREATE PROCEDURE deleteCategory(IN cid int)
BEGIN
    DELETE FROM category WHERE id=cid;
    SELECT ROW_COUNT() as rows;
END$$
DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS deleteCharacteristic;
CREATE PROCEDURE deleteCharacteristic(IN cid int)
BEGIN
    DELETE FROM characteristic WHERE id=cid;
    SELECT ROW_COUNT() as rows;
END$$
DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS deleteProductCategory;
CREATE PROCEDURE deleteProductCategory(IN rid int, IN pid int, IN cid int)
BEGIN
    SET SQL_SAFE_UPDATES = 0;
    DELETE FROM product_category WHERE id=rid OR (category_id=cid AND product_id=pid);
    SELECT ROW_COUNT() as rows;
END$$
DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS deleteProductCharacteristic;
CREATE PROCEDURE deleteProductCharacteristic(IN rid int, IN pid int, IN cid int)
BEGIN
    SET SQL_SAFE_UPDATES = 0;
    DELETE FROM product_characteristic WHERE id=rid OR (charact_id=cid AND product_id=pid);
    SELECT ROW_COUNT() as rows;
END$$
DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS deleteDiscount;
CREATE PROCEDURE deleteDiscount(IN did int)
BEGIN
    DELETE FROM discount WHERE id=did;
    SELECT ROW_COUNT() as rows;
END$$
DELIMITER ;