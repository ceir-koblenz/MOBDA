//Purge von Mapping Properties von Task
MATCH (tas:Task)
SET tas.EXID = null
SET tas.PARENTUUID = null