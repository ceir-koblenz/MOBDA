#Skript um alle Mapping IDs zu bereinigen
#Alle Properties die nicht in der ColActDOnt vorgesehen sind werden auf "null" gesetzt und damit gelöcht

import neointerface

neodb = neointerface.NeoInterface(host="neo4j://ma-lschloemer.bas.uni-koblenz.de:7687" , credentials=("neo4j", "neo4jneo4j"))

#Queries für den Purge der MappingIDs

queryPurgeFileLibrary = """
//Purge von Mapping Properties von FileLibrary
MATCH fili:FileLibrary)
SET fili.EXTERNAL_CONTAINER_ID = null
"""

queryPurgeGroupWorkspace = """
//Purge von Mapping Properties von GroupWorkspace
MATCH (gws:GroupWorkspace)
SET gws.DIRECTORY_UUID = null
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

queryPurgeTaskContainer = """
//Purge von Mapping Properties von TaskContainer
MATCH (taco:TaskContainer)
SET taco.EXID = null
"""
queryPurgeWeblog = """
//Purge von Mapping Properties von Weblog
MATCH (web.Weblog)
SET web.ASSOCID = null
"""

queryPurgeWiki = """
//Purge von Mapping Properties von Wiki
MATCH (wi:Wiki)
SET wi.MEDIA_ID= null
SET wi.EXTERNAL_CONTAINER_ID = null
"""

#Ausführen der Queries mit NeoInterface

neodb.query(queryPurgeFileLibrary)
neodb.query(queryPurgeGroupWorkspace)
neodb.query(queryPurgeMessageBoard)
neodb.query(queryPurgeMicroblog)
neodb.query(queryPurgeTaskContainer)
neodb.query(queryPurgeWeblog)
neodb.query(queryPurgeWiki)
