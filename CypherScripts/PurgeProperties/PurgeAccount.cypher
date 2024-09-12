//Purge von Mapping Properties von Account
MATCH (acc:Account)
SET acc.PROF_GUID = null