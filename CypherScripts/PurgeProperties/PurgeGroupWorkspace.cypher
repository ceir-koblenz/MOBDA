//Purge von Mapping Properties von GroupWorkspace
MATCH (gws:GroupWorkspace)
SET gws.DIRECTORY_UUID = null