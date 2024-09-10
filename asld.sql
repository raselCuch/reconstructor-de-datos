CREATE DEFINER=`root`@`localhost` PROCEDURE `bdrebomarket`.`SpArticuloCreaStAlm`(
    IN `nempresa1` VARCHAR(11), 
    IN `nalmacen1` VARCHAR(3), 
    IN `nempresa2` VARCHAR(11), 
    IN `nalmacen2` VARCHAR(3)
)
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE xcont INTEGER;
    DECLARE xcod VARCHAR(10);
    DECLARE xmsg VARCHAR(50);

    DECLARE cur1 CURSOR FOR 
        SELECT codarti 
        FROM tblstarticulo 
        WHERE codalm = nalmacen1 AND ruc = nempresa1;

    DECLARE CONTINUE HANDLER FOR SQLSTATE '02000' SET done = 1;

    OPEN cur1;
    REPEAT
        FETCH cur1 INTO xcod;
        IF NOT done THEN
            SET xcont = (
                SELECT COUNT(*) 
                FROM tblstarticulo 
                WHERE codarti = xcod 
                  AND ruc = nempresa2 
                  AND codalm = nalmacen2
            );

            IF xcont > 0 THEN
                SELECT xmsg = 'Encontrado';
            ELSE
                INSERT INTO tblstarticulo(ruc, codalm, codarti, stock, feccreacion, UserCreacion) 
                VALUES (nempresa2, nalmacen2, xcod, 0, NOW(), 'ADMIN');
            END IF;
        END IF;
    UNTIL done
    END REPEAT;

    CLOSE cur1;
END;
