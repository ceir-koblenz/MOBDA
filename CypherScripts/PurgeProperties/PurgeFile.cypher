//Purge von Mapping Properties von File
MATCH (fil:File)
SET fil.MEDIA_ID = null
SET fil.DIRECTORY_ID = null
SET fil.CURRENT_REVISION_ID = null
SET fil.MATCH_MEDIA_ID = null
SET fil.SUB_ID = null
SET fil.PREVIOUSID = null
