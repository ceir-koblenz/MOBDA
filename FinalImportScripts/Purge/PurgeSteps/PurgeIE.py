#Skript um alle Mapping IDs zu bereinigen
#Alle Properties die nicht in der ColActDOnt vorgesehen sind werden auf "null" gesetzt und damit gelöcht

import neointerface

neodb = neointerface.NeoInterface(host="neo4j://ma-lschloemer.bas.uni-koblenz.de:7687" , credentials=("neo4j", "neo4jneo4j"))

#Queries für den Purge der MappingIDs

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

queryPurgeFolder = """
//Purge von Mapping Properties von Folder
MATCH (fol:Folder)
SET fol.DIRECTORY_ID = null
SET fol.MEDIA_ID = null
SET fol.MATCH_FOLDER_ID = null
SET fol.PARENT_ID = null
"""

queryPurgeMicroblogPost = """
//Purge von Mapping Properties von MicroblogPost
MATCH (mipo:MicroblogPost)
SET mipo.CONTAINER_ID = null
SET mipo.EXID = null
"""

queryPurgeSocialProfile = """
//Purge von Mapping Properties von SocialProfile
MATCH (sopo:SocialProfile)
SET sopo.ENTRY_ID = null
SET sopo.EXID = null
"""

queryPurgeTask = """
//Purge von Mapping Properties von Task
MATCH (tas:Task)
SET tas.EXID = null
SET tas.PARENTUUID = null
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

neodb.query(queryPurgeBlogPost)
neodb.query(queryPurgeBoardPost)
neodb.query(queryPurgeFile)
neodb.query(queryPurgeFolder)
neodb.query(queryPurgeMicroblogPost)
neodb.query(queryPurgeSocialProfile)
neodb.query(queryPurgeTask)
neodb.query(queryPurgeWikiPage)