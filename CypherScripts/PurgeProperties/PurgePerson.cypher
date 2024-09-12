//Purge von Mapping Properties von Person
MATCH (per:Person)
SET per.PROF_GUID = null