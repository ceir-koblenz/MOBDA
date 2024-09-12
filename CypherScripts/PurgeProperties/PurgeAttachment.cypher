//Purge von Mapping Properties von Attachement
MATCH (att:Attachment)
SET att.EXID = null
SET att.ITEM_ID = null
SET att.OBJECT_EXTERNAL_ID = null
SET att.MEMBERTYPE = null
SET att.PARENTUUID = null
SET att.MEDIA_ID = null
SET att.DIRECTORY_ID = null
SET att.MATCH_ID = null
SET att.ENTRY_ID = null
SET att.TOPICID = null
