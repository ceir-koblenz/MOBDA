//Purge von Mapping Properties von MicroblogPost
MATCH (mipo:MicroblogPost)
SET mipo.CONTAINER_ID = null
SET mipo.EXID = null
