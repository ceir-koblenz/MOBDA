//Purge von Mapping Properties von Microblog
MATCH (mibl:Microblog)
SET mibl.EXID = null
