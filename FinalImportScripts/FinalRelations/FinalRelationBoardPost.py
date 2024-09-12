#Library für Neointerface für die Verbindung zu Neo4j
import neointerface
#Verbindung zu Neo4j 
neodb = neointerface.NeoInterface(host="neo4j://ma-lschloemer.bas.uni-koblenz.de:7687" , credentials=("neo4j", "neo4jneo4j"))

#Cypher Queries für Relations
queryRelationBoardPost_board_post_contained_in_message_board_MessageBoard = """
//Relation Realation BoardPost <-> Messageboard
MATCH (bp:BoardPost)
MATCH (mebo:MessageBoard)
WHERE bp.FORUMUUID = mebo.ID
MERGE (bp)-[rbpcimb:board_post_contained_in_message_board {cardinality: "exactly 1"}]->(mebo)
MERGE (mebo)-[rmbcbp:message_board_contains_board_post]->(bp)
"""

queryRelationBoardPost_intellectual_entity_has_component_Attachment = """
//Relation BoardPost <-> Attachment 
MATCH (bp:BoardPost)
MATCH (att:Attachment)
WHERE bp.ID = att.TOPICID
MERGE (att)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(bp)
MERGE (bp)-[riehc:intellectual_entity_has_component]->(att)
"""

queryRelationBoardPost_intellectual_entity_has_component_Comment = """
//Relation  BoardPost <-> Comment
MATCH (bp:BoardPost)
MATCH (com:Comment)
WHERE bp.ID = com.TOPICID
MERGE (com)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(bp)
MERGE (bp)-[riehc:intellectual_entity_has_component]->(com)
"""

queryRelationBoardPost_intellectual_entity_has_component_Follow = """
//Relation Real BoardPost <-> Follow
MATCH (bp:BoardPost)
MATCH (fol:Follow)
WHERE bp.TOPICID = fol.TOPICID
MERGE (fol)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(bp)
MERGE (bp)-[riehc:intellectual_entity_has_component]->(fol)
"""

queryRelationBoardPost_intellectual_entity_has_component_Like = """
//Relation Real BoardPost <-> Like
MATCH (bp:BoardPost)
MATCH (like:Like)
WHERE bp.ID = like.NODEID
MERGE (like)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(bp)
MERGE (bp)-[riehc:intellectual_entity_has_component]->(like)
"""

queryRelationBoardPost_intellectual_entity_has_component_Tag = """
//Relation Real BoardPost <-> Tag
MATCH (bp:BoardPost)
MATCH (tag:Tag)
WHERE bp.ID = tag.NODEUUID
MERGE (tag)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(bp)
MERGE (bp)-[riehc:intellectual_entity_has_component]->(tag)
"""

neodb.query(queryRelationBoardPost_board_post_contained_in_message_board_MessageBoard)
neodb.query(queryRelationBoardPost_intellectual_entity_has_component_Attachment)
neodb.query(queryRelationBoardPost_intellectual_entity_has_component_Comment)
neodb.query(queryRelationBoardPost_intellectual_entity_has_component_Follow)
neodb.query(queryRelationBoardPost_intellectual_entity_has_component_Like)
neodb.query(queryRelationBoardPost_intellectual_entity_has_component_Tag)