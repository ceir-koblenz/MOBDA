//Purge von Mapping Properties von MessageBoard
MATCH (mebo:MessageBoard)
SET mebo.COMMUNITYID = null
