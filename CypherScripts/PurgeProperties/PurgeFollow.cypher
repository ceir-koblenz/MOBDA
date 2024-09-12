//Purge von Mapping Properties von Follow
MATCH (foll:Follow)
SET foll.TOPICID = null
SET foll.EXID = null
SET foll.DIRECTORY_ID = null
SET foll.MEDIA_ID = null
SET foll.MATCH_MEDIA_ID = null
SET foll.COLLECTION_ID = null
SET foll.MATCH_FOLDER_ID = null
SET foll.PERSON_ID = null
SET foll.NODEUUID = null
SET foll.PARENTUUID = null
SET foll.WIKI_ID = null
