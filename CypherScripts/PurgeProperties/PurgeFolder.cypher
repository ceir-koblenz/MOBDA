//Purge von Mapping Properties von Folder
MATCH (fol:Folder)
SET fol.DIRECTORY_ID = null
SET fol.MEDIA_ID = null
SET fol.MATCH_FOLDER_ID = null
SET fol.PARENT_ID = null
