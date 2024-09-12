//Purge von Mapping Properties von BoardPost
MATCH (bopo:BoardPost)
SET bopo.FORUMUUID = null
SET bopo.EXID = null
SET bopo.TOPICID = null

