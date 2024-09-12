#Library für Neointerface für die Verbindung zu Neo4j
import neointerface
#Verbindung zu Neo4j 
neodb = neointerface.NeoInterface(host="neo4j://ma-lschloemer.bas.uni-koblenz.de:7687" , credentials=("neo4j", "neo4jneo4j"))

#Cypher Queries für Relations
#zurückgestellt
# queryRelationFile_file_contained_in_Folder_Folder = """
#//Relation  File  <-> Folder Wegen fehlender zurückgestellt
#MATCH (fi:File)
#MATCH (fo:Folder)
#WHERE fi.ACTIVITYUUID = taskc.ID
#MERGE (fi)-[rfcif:file_contained_in_folder {cardinality: "maximal 1"}]->(fo)
#MERGE (fo)-[rfcf:folder_contains_file]->(fi)
#"""
queryRelationFile_intellectual_entity_has_component_Comment = """
//Relation  File  <-> Comment
MATCH (fi:File)
MATCH (com:Comment)
WHERE fi.MEDIA_ID = com.MEDIA_ID
MERGE (fi)-[riehc:intellectual_entity_has_component {cardinality: "exactly 1"}]->(com)
MERGE (com)-[rcoie:component_of_intellectual_entity]->(fi)
"""
queryRelationFile_intellectual_entity_has_component_Like = """
//Relation  File  <-> Like
MATCH (fi:File)
MATCH (like:Like)
WHERE fi.ID = like.FILE_ID
MERGE (fi)-[riehc:intellectual_entity_has_component {cardinality: "exactly 1"}]->(like)
MERGE (like)-[rcoie:component_of_intellectual_entity]->(fi)
"""

queryRelationFile_intellectual_entity_has_previous_version_File = """
//Relation File < previous Version > File
MATCH (finext:File)
MATCH (fipre:File)
WHERE finext.SUB_ID = fipre.PREVIOUSID
MERGE (finext)-[riehpv:intellectual_entity_has_previous_version {cardinality: "maximal 1"}]->(fipre)
MERGE (fipre)-[richnv:intellectual_entity_has_next_version {cardinality: "maximal 1"}]->(finext)
"""
queryRelationFile_intellectual_entity_has_recent_version_File = """
//Relation File < recent Version > File
MATCH (fiold:File)
MATCH (firecent:File)
WHERE fiold.ID = firecent.CURRENT_REVISION_ID
MERGE (fiold)-[riehrv:intellectual_entity_has_recent_version {cardinality: "exactly 1"}]->(firecent)
MERGE (firecent)-[ricov:intellectual_entity_has_old_version ]->(fiold)"""

#zurückgestellt
#queryRelationFolder_intellectual_entity_has_component_Follow = """
#//Relation  Folder  <-> Follow
#MATCH (fo:Folder)
#MATCH (foll:Follow)
#WHERE fo.ID = foll.COLLECTION_ID
#MERGE (fo)-[riehc:intellectual_entity_has_component {cardinality: "exactly 1"}]->(foll)
#MERGE (foll)-[rcoie:component_of_intellectual_entity]->(fo)
#"""

#neodb.query(queryRelationFile_file_contained_in_Folder_Folder)
neodb.query(queryRelationFile_intellectual_entity_has_component_Comment)
neodb.query(queryRelationFile_intellectual_entity_has_component_Like)
neodb.query(queryRelationFile_intellectual_entity_has_previous_version_File)
neodb.query(queryRelationFile_intellectual_entity_has_recent_version_File)
#neodb.query(queryRelationFolder_intellectual_entity_has_component_Follow)

