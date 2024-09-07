CREATE DEFINER=`root`@`localhost` PROCEDURE `bdrebomarket_dev`.`MigraVentas`() -- Define procedimiento almacenado y especifica el usuario con permiso
BEGIN
    DECLARE done INT DEFAULT 0;  -- Declaran variables
    DECLARE xfecreg VARCHAR(15);
    DECLARE xcli VARCHAR(11);
    DECLARE xtipcli VARCHAR(3);
    DECLARE xdocu VARCHAR(3);
    DECLARE xdoc VARCHAR(3);
    DECLARE xdocserie VARCHAR(3);
    DECLARE xdocnum VARCHAR(11);
    DECLARE xmon VARCHAR(1);
    DECLARE xped VARCHAR(1);
    DECLARE xtc DOUBLE;
    DECLARE xtipven VARCHAR(1);
    DECLARE xdiacre INT;
    DECLARE xfecvenc VARCHAR(15);
    DECLARE xmonbru DOUBLE;
    DECLARE xmonigv DOUBLE;
    DECLARE xmonven DOUBLE;
    DECLARE xestven VARCHAR(1);
    DECLARE xestanul VARCHAR(1);
    DECLARE xestadoc VARCHAR(1);
    DECLARE xrucemp VARCHAR(11);
    DECLARE xalm VARCHAR(3);
    DECLARE xusuario VARCHAR(12);
    DECLARE xidventa VARCHAR(50);
    DECLARE xcodcli VARCHAR(11);
    DECLARE xhora VARCHAR(11);
    DECLARE a INT;

    -- Declara cursor 'cur1' que selecciona datos de la tabla 'ventascab_dbf'
    DECLARE cur1 CURSOR FOR 
        SELECT v.FECREGISTR, v.CLIENTE_ID, 
               (SELECT DISTINCT IFNULL(c.TIPOCODIGO,'') FROM clientes_dbf c WHERE c.CLIENTE_ID = v.CLIENTE_ID) AS TipDoc, 
                v.DOCU_ID, v.DOCUSERIE, v.DOCUNUM, v.MONEDA_ID, 
                '' AS pedido, IFNULL(v.TIPOCAMBIO,0) AS TipCambio, 
                v.TIPOVENTA_, v.DIAS_CRED, v.FECULTPAGO, 
                v.MONTO_BRUT, 0 AS MontoIgv, v.MONTO_NETO, 
                'C' AS Estado, v.DOCU_ANUL, v.USUARIO_ID, v.HORACREA
        FROM ventascab_dbf v 
        WHERE v.TIPOPER_ID = '2' 
          AND v.TIPMOVI_ID = '001' 
          AND v.DOCU_ID IN ('001','002','003') 
          AND v.ALMACEN_ID = '104' 
          AND v.EMPRESA_ID = '001'
          AND v.FECREGISTR = '2016-12-24';

    -- Define manejador
    DECLARE CONTINUE HANDLER FOR SQLSTATE '02000' SET done = 1; -- No Data Found

    SET a = 0;

    OPEN cur1; -- Abre cursor

    REPEAT  -- Inicia bucle para procesar cada fila del cursor
        -- Los datos se extraen en variables
        FETCH cur1 INTO xfecreg, xcli, xtipcli, xdocu, xdocserie, xdocnum, xmon, xped, xtc, xtipven, xdiacre, xfecvenc, xmonbru, xmonigv, xmonven, xestven, xestanul, xusuario, xhora;
        SET a = a + 1;

        IF NOT done THEN -- si 'done' no es 0
            -- Asigna el tipo de documento
            CASE xdocu
                WHEN '001' THEN SET xdoc = '005';
                WHEN '002' THEN SET xdoc = '004';
                WHEN '003' THEN SET xdoc = '006';
            END CASE;

            -- Asigna el estado del documento
            CASE xestanul
                WHEN 'S' THEN SET xestadoc = 'N';
                ELSE SET xestadoc = 'A';
            END CASE;

            SET xrucemp = '20352471578';
            SET xalm = '104';

            -- Asigna el código de cliente
            CASE IFNULL(xcli,'') 
                WHEN '' THEN SET xcodcli = 'C0000000001';
                ELSE SET xcodcli = xcli;
            END CASE;

            -- Define IdVenta
            SET xidventa := CONCAT(xcodcli, xdoc, xdocserie, '-', xdocnum, xalm, xrucemp);

            -- Inserta los datos en la tabla 'TblVenta'
            INSERT INTO TblVenta (
                IdVenta, Fecha, Cliente, TipDocCli, Doc, Serie, Numero, TMoneda, NPedido, TCambio, TVenta, NDias, FVence, TBruto, TIgv, Total, TEst, Est, Empresa, Almacen, Vendedor, Usuario, FecCreacion, UserCreacion
            ) VALUES (
                xidventa, xfecreg, 
                CASE IFNULL(xcli,'') WHEN '' THEN 'C0000000001' ELSE xcli END,
                CASE IFNULL(xtipcli,'') WHEN 'R' THEN '6' WHEN 'D' THEN '1' ELSE '' END,
                xdoc, xdocserie, xdocnum, 
                CASE IFNULL(xmon,'') WHEN '1' THEN '001' WHEN '2' THEN '002' ELSE '' END, 
                xped, xtc, 
                CASE IFNULL(xtipven,'') WHEN '1' THEN '001' WHEN '2' THEN '002' ELSE '' END, 
                xdiacre, xfecvenc, xmonbru, xmonigv, xmonven, xestven, xestadoc, xrucemp, xalm, xusuario, xusuario, 
                CONCAT(xfecreg, ' ', TRIM(xhora)), 'ADMIN'
            );

            -- Inserta datos en tabla 'tbldetventa'
            INSERT INTO tbldetventa (
                IdVenta, Codigo, Marca, Unidad, Proced, PVenta, Cantidad, Igv, Importe, Almacen, Empresa, FecCreacion, UserCreacion
            ) 
            SELECT xidventa, SUBSTR(PRODUCTO_I,3,6), 
                   (SELECT ar.CodMarca FROM tblarticulos ar WHERE ar.CodArt = SUBSTR(PRODUCTO_I,3,6)),
                   (SELECT ar.CodUnidad FROM tblarticulos ar WHERE ar.CodArt = SUBSTR(PRODUCTO_I,3,6)),
                   (SELECT ar.CodProced FROM tblarticulos ar WHERE ar.CodArt = SUBSTR(PRODUCTO_I,3,6)),
                   d.PRECIO_UNI, d.CANTIDAD, d.VALOR_IGV, d.VALOR_VENT, xalm, xrucemp, 
                   CONCAT(FECREGISTR, ' ', TRIM(HORACREA)), 'ADMIN'
            FROM ventasdet_dbf AS d
            WHERE d.TIPOPER_ID = '2' 
              AND d.TIPMOVI_ID = '001' 
              AND d.DOCU_ID IN ('001','002','003') 
              AND d.ALMACEN_ID = '104' 
              AND d.EMPRESA_ID = '001' 
              AND d.DOCU_ID = xdocu 
              AND d.DOCUSERIE = xdocserie 
              AND d.DOCUNUM = xdocnum;
        END IF;

    UNTIL done
    END REPEAT;

END;
