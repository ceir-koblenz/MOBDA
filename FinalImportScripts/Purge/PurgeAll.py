#Skript um alle Mapping IDs zu bereinigen
#Alle Properties die nicht in der ColActDOnt vorgesehen sind werden auf "null" gesetzt und damit gelöcht

import neointerface

neodb = neointerface.NeoInterface(host="neo4j://ma-lschloemer.bas.uni-koblenz.de:7687" , credentials=("neo4j", "neo4jneo4j"))

#Queries für den Purge der MappingIDs

queryPurgeAccount = """
//Purge von Mapping Properties von Account
MATCH (acc:Account)
SET acc.PROF_GUID = null
"""

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

queryPurgeBlogPost = """
//Purge von Mapping Properties von BlogPost
MATCH (bp:BlogPost)
SET bp.WEBSITEID = null
SET bp.USERID = null
SET bp.EXTID = null
"""

queryPurgeBoardPost = """
//Purge von Mapping Properties von BoardPost
MATCH (bopo:BoardPost)
SET bopo.FORUMUUID = null
SET bopo.EXID = null
SET bopo.TOPICID = null
"""
queryPurgeComment = """
//Purge von Mapping Properties von Comment
MATCH (com:Commment)
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
queryPurgeEvent25 = """
//Purge von Mapping Properties von Event
MATCH (ev:Event)
WHERE ev.ID <= 2500000
SET ev.UUID = null
SET ev.ITEM_UUID = null
SET ev.SOURCE_ID = null
SET ev.MATCH_ITEM_UUID = null
"""

queryPurgeEvent2565 = """
//Purge von Mapping Properties von Event
MATCH (ev:Event)
WHERE ev.ID > 2500000 AND ev.ID <=6500000
SET ev.UUID = null
SET ev.ITEM_UUID = null
SET ev.SOURCE_ID = null
SET ev.MATCH_ITEM_UUID = null
"""

queryPurgeEvent65 = """
//Purge von Mapping Properties von Event
MATCH (ev:Event)
WHERE ev.ID > 6500000 
SET ev.UUID = null
SET ev.ITEM_UUID = null
SET ev.SOURCE_ID = null
SET ev.MATCH_ITEM_UUID = null
"""

queryPurgeEvent = """
//Purge von Mapping Properties von Event
MATCH (ev:Event)
SET ev.UUID = null
SET ev.ITEM_UUID = null
SET ev.SOURCE_ID = null
SET ev.MATCH_ITEM_UUID = null
"""
queryPurgeFile = """
//Purge von Mapping Properties von File
MATCH (fil:File)
SET fil.MEDIA_ID = null
SET fil.DIRECTORY_ID = null
SET fil.CURRENT_REVISION_ID = null
SET fil.MATCH_MEDIA_ID = null
SET fil.SUB_ID = null
SET fil.PREVIOUSID = null
"""

queryPurgeFileLibrary = """
//Purge von Mapping Properties von FileLibrary
MATCH (fili:FileLibrary)
SET fili.EXTERNAL_CONTAINER_ID = null
"""

queryPurgeFolder = """
//Purge von Mapping Properties von Folder
MATCH (fol:Folder)
SET fol.DIRECTORY_ID = null
SET fol.MEDIA_ID = null
SET fol.MATCH_FOLDER_ID = null
SET fol.PARENT_ID = null
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
queryPurgeGroupWorkspace = """
//Purge von Mapping Properties von GroupWorkspace
MATCH (gws:GroupWorkspace)
SET gws.DIRECTORY_UUID = null
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

queryPurgeMessageBoard = """
//Purge von Mapping Properties von MessageBoard
MATCH (mebo:MessageBoard)
SET mebo.COMMUNITYID = null
"""

queryPurgeMicroblog = """
//Purge von Mapping Properties von Microblog
MATCH (mibl:Microblog)
SET mibl.EXID = null
"""
queryPurgeMicroblogPost = """
//Purge von Mapping Properties von MicroblogPost
MATCH (mipo:MicroblogPost)
SET mipo.CONTAINER_ID = null
SET mipo.EXID = null
"""
queryPurgePerson = """
//Purge von Mapping Properties von Person
MATCH (per:Person)
SET per.PROF_GUID = null
"""
queryPurgeSocialProfile = """
//Purge von Mapping Properties von SocialProfile
MATCH (sopo:SocialProfile)
SET sopo.ENTRY_ID = null
SET sopo.EXID = null
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

queryPurgeTask = """
//Purge von Mapping Properties von Task
MATCH (tas:Task)
SET tas.EXID = null
SET tas.PARENTUUID = null
"""

queryPurgeTaskContainer = """
//Purge von Mapping Properties von TaskContainer
MATCH (taco:TaskContainer)
SET taco.EXID = null
"""

queryPurgeWeblog = """
//Purge von Mapping Properties von Weblog
MATCH (web:Weblog)
SET web.ASSOCID = null
"""

queryPurgeWiki = """
//Purge von Mapping Properties von Wiki
MATCH (wi:Wiki)
SET wi.MEDIA_ID= null
SET wi.EXTERNAL_CONTAINER_ID = null
"""

queryPurgeWikiPage = """
//Purge von Mapping Properties von WikiPage
MATCH (wipa:WikiPage)
SET wipa.MEDIA_ID = null
SET wipa.DIRECTORY_ID = null
SET wipa.MATCH_MEDIA_ID = null
SET wipa.CHILD_ID = null
SET wipa.PARENT_ID = null
SET wipa.CURRENT_REVISION_ID = null
SET wipa.SUB_ID = null
SET wipa.PREVIOUS_ID = null
"""

#Ausführen der Queries mit NeoInterface

neodb.query(queryPurgeAccount)#
neodb.query(queryPurgeAttachment)# 
neodb.query(queryPurgeBlogPost)#
neodb.query(queryPurgeBoardPost)#
#tested ^^
neodb.query(queryPurgeComment)#
neodb.query(queryPurgeEvent25)
neodb.query(queryPurgeEvent2565)
neodb.query(queryPurgeEvent65)
neodb.query(queryPurgeEvent)#
neodb.query(queryPurgeFile)#
neodb.query(queryPurgeFileLibrary)#
neodb.query(queryPurgeFolder)#
neodb.query(queryPurgeFollow)#
neodb.query(queryPurgeGroupWorkspace)#
neodb.query(queryPurgeLike)#
neodb.query(queryPurgeMessageBoard)#
neodb.query(queryPurgeMicroblog)#
neodb.query(queryPurgeMicroblogPost)#
neodb.query(queryPurgePerson)#
neodb.query(queryPurgeSocialProfile)#
neodb.query(queryPurgeTag)#
neodb.query(queryPurgeTask)#
neodb.query(queryPurgeTaskContainer)#
neodb.query(queryPurgeWeblog)#
neodb.query(queryPurgeWiki)#
neodb.query(queryPurgeWikiPage)#