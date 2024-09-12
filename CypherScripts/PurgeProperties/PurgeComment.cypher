//Purge von Mapping Properties von Comment
MATCH (com:Comment)
SET com.EXTID = null
SET com.ENTRYID = null
SET com.EXID = null
SET com.TOPICID = null
SET com.MEDIA_ID = null
SET com.DIRECTORY_ID = null
SET com.MATCH_COMMENT_ID = null
SET com.ITEM_ID = null
SET com.MATCH_COM_ID = null
