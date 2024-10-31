CREATE OR REPLACE FUNCTION hexedToID(hexValue VARBINARY)
RETURNS VARCHAR
RETURN  CONCAT(SUBSTR(hexValue, 1, 8), '-', 
        SUBSTR(hexValue, 9, 4), '-', 
        SUBSTR(hexValue, 13, 4), '-', 
        SUBSTR(hexValue, 17, 4), '-', 
        SUBSTR(hexValue, 21))