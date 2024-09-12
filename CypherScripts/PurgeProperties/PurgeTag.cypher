//Purge von Mapping Properties von Tag
MATCH (tag:Tag)
SET tag.EXTID = null
SET tag.ENTRYID = null
SET tag.EXID = null
SET tag.NODEUUID = null
SET tag.USERID = null
SET tag.MEDIA_ID = null
SET tag.PROF_GUID = null
