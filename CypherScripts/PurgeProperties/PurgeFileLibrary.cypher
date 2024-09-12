//Purge von Mapping Properties von FileLibrary
MATCH fili:FileLibrary)
SET fili.EXTERNAL_CONTAINER_ID = null