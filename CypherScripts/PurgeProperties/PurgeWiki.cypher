//Purge von Mapping Properties von Wiki
MATCH (wi:Wiki)
SET wi.MEDIA_ID= null
SET wi.EXTERNAL_CONTAINER_ID = null
