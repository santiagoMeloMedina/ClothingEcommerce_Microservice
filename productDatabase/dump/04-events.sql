
DELIMITER $$
DROP EVENT IF EXISTS deleteDiscount;
CREATE EVENT deleteDiscount
ON SCHEDULE EVERY 30 MINUTE
STARTS CURRENT_TIMESTAMP
DO
BEGIN
	DELETE FROM discount WHERE deadline <= NOW();
END$$
DELIMITER ;