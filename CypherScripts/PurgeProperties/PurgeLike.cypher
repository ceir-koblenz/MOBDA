//Purge von Mapping Properties von Like
MATCH (lik:Like)
SET lik.ENTRYID = null
SET lik.EXTID = null
SET lik.COMMENTID = null
SET lik.NODEID = null
SET lik.FILE_ID = null
SET lik.DIRECTORY_ID = null
SET lik.MATCH_MEDIA_ID = null
SET lik.EXID = null
SET lik.ENTRY_ID = null
SET lik.COMMENT_ID = null
SET lik.OBJECT_ID = null
SET lik.WIKI_ID = null