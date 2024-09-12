#Skript um alle Mapping IDs zu bereinigen
#Alle Properties die nicht in der ColActDOnt vorgesehen sind werden auf "null" gesetzt und damit gelöcht

import neointerface

neodb = neointerface.NeoInterface(host="neo4j://ma-lschloemer.bas.uni-koblenz.de:7687" , credentials=("neo4j", "neo4jneo4j"))

#Queries für den Purge der MappingIDs

queryPurgeAttachment ="""
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
"""

queryPurgeComment = """
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
"""

queryPurgeFollow = """
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
"""

queryPurgeLike = """
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
"""

queryPurgeTag = """
//Purge von Mapping Properties von Tag
MATCH (tag:Tag)
SET tag.EXTID = null
SET tag.ENTRYID = null
SET tag.EXID = null
SET tag.NODEUUID = null
SET tag.USERID = null
SET tag.MEDIA_ID = null
SET tag.PROF_GUID = null
"""

neodb.query(queryPurgeAttachment) 
#tested ^^
neodb.query(queryPurgeComment)
neodb.query(queryPurgeFollow)
neodb.query(queryPurgeLike)
neodb.query(queryPurgeTag)
