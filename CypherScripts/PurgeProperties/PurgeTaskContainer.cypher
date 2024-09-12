//Purge von Mapping Properties von TaskContainer
MATCH (taco:TaskContainer)
SET taco.EXID = null