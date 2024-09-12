#Library für Neointerface für die Verbindung zu Neo4j
import neointerface
#Verbindung zu Neo4j 
neodb = neointerface.NeoInterface(host="neo4j://ma-lschloemer.bas.uni-koblenz.de:7687" , credentials=("neo4j", "neo4jneo4j"))

#Cypher Queries für Relations
queryRelationGroupWorkspace_space_contains_container_FileLibrary = """
//Relation GroupWorkspace <-> FileLibrary
MATCH (gws:GroupWorkspace)
MATCH (filib:FileLibrary)
WHERE filib.EXTERNAL_CONTAINER_ID = gws.ID
MERGE (filib)-[rccis:container_contained_in_space {cardinality: "exactly 1"}]->(gws)
MERGE (gws)-[rscc:space_contains_container]->(filib)
"""

queryRelationGroupWorkspace_space_contains_container_MessageBoard = """
//Relation GroupWorkspace <-> Messageboard
MATCH (gws:GroupWorkspace)
MATCH (mebo:MessageBoard)
WHERE mebo.COMMUNITYUUID = gws.ID
MERGE (mebo)-[rccis:container_contained_in_space {cardinality: "exactly 1"}]->(gws)
MERGE (gws)-[rscc:space_contains_container]->(mebo)
"""

queryRelationGroupWorkspace_space_contains_container_Microblog = """
//Relation Realation GroupWorkspace <-> Microblog
MATCH (gws:GroupWorkspace)
MATCH (mb:Microblog)
WHERE mb.EXID = gws.ID
MERGE (mb)-[rccis:container_contained_in_space {cardinality: "exactly 1"}]->(gws)
MERGE (gws)-[rscc:space_contains_container]->(mb)
"""

#zurückgestellt
#queryRelationGroupWorkspace_space_contains_container_TaskContainer = """
#//Relation Realation GroupWorkspace <-> TaskContainer
#MATCH (gws:GroupWorkspace)
#MATCH (taco:TaskContainer)
#WHERE taco.EXID = gws.ID
#MERGE (taco)-[rccis:container_contained_in_space {cardinality: "exactly 1"}]->(gws)
#MERGE (gws)-[rscc:space_contains_container]->(taco)
#"""

queryRelationGroupWorkspace_space_contains_container_Weblog = """
//Relation Realation GroupWorkspace <-> Weblog
MATCH (gws:GroupWorkspace)
MATCH (web:Weblog)
WHERE web.ASSOCID = gws.ID
MERGE (web)-[rccis:container_contained_in_space {cardinality: "exactly 1"}]->(gws)
MERGE (gws)-[rscc:space_contains_container]->(web)
"""

queryRelationGroupWorkspace_space_contains_container_Wiki = """
//Relation GroupWorkspace <-> Wiki
MATCH (gws:GroupWorkspace)
MATCH (wi:Wiki)
WHERE wi.EXTERNAL_CONTAINER_ID = gws.ID
MERGE (wi)-[rccis:container_contained_in_space {cardinality: "exactly 1"}]->(gws)
MERGE (gws)-[rscc:space_contains_container]->(wi)
"""

neodb.query(queryRelationGroupWorkspace_space_contains_container_FileLibrary)
neodb.query(queryRelationGroupWorkspace_space_contains_container_MessageBoard)
neodb.query(queryRelationGroupWorkspace_space_contains_container_Microblog)
#neodb.query(queryRelationGroupWorkspace_space_contains_container_TaskContainer)
neodb.query(queryRelationGroupWorkspace_space_contains_container_Weblog)
neodb.query(queryRelationGroupWorkspace_space_contains_container_Wiki)