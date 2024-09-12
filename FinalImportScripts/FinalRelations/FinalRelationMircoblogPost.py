#Library für Neointerface für die Verbindung zu Neo4j
import neointerface
#Verbindung zu Neo4j 
neodb = neointerface.NeoInterface(host="neo4j://ma-lschloemer.bas.uni-koblenz.de:7687" , credentials=("neo4j", "neo4jneo4j"))

#Cypher Queries für Relations
queryRelationMicroblogPost_intellectual_entity_has_component_Attachment = """
//Relation MicroblogPost <-> Attachment
MATCH (mbp:MicroblogPost)
MATCH (att:Attachment)
WHERE mbp.ID = att.ITEM_ID
MERGE (att)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(mbp)
MERGE (mbp)-[riehc:intellectual_entity_has_component]->(att)
"""

queryRelationMicroblogPost_intellectual_entity_has_component_Comment = """
//Relation MicroblogPost <-> Comment
MATCH (mbp:MicroblogPost)
MATCH (com:Comment)
WHERE mbp.ID = com.ENTRY_ID
MERGE (com)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(mbp)
MERGE (mbp)-[riehc:intellectual_entity_has_component]->(com)
"""

queryRelationMicroblogPost_intellectual_entity_has_component_Like = """
//Relation MicroblogPost <-> Like
MATCH (mbp:MicroblogPost)
MATCH (like:Like)
WHERE mbp.ID = like.ENTRY_ID
MERGE (like)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(mbp)
MERGE (mbp)-[riehc:intellectual_entity_has_component]->(like)
"""

queryRelationMicroblogPost_microblog_post_contained_in_microblog_Microblog = """
//Relation Realation MicroblogPost <-> Microblog
MATCH (mbp:MicroblogPost)
MATCH (mb:Microblog)
WHERE mb.ID= mbp.CONTAINER_ID
MERGE (mbp)-[rmpcim:microblog_post_contained_in_microblog {cardinality: "exactly 1"}]->(mb)
MERGE (mb)-[rmcmp:microblog_contains_microblog_post]->(mbp)
"""

neodb.query(queryRelationMicroblogPost_intellectual_entity_has_component_Attachment)
neodb.query(queryRelationMicroblogPost_intellectual_entity_has_component_Comment)
neodb.query(queryRelationMicroblogPost_intellectual_entity_has_component_Like)
neodb.query(queryRelationMicroblogPost_microblog_post_contained_in_microblog_Microblog)