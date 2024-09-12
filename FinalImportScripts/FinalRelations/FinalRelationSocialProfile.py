#Library für Neointerface für die Verbindung zu Neo4j
import neointerface
#Verbindung zu Neo4j 
neodb = neointerface.NeoInterface(host="neo4j://ma-lschloemer.bas.uni-koblenz.de:7687" , credentials=("neo4j", "neo4jneo4j"))

#Cypher Queries für Relations
#zurückgestellt
#queryRelationSocialProfile_intellectual_entity_has_component_Comment = """
#//Relation Real SocialProfile <-> Comment
#MATCH (sop:SocialProfile)
#MATCH (com:Comment)
#WHERE sop.ENTRY_ID = com.ENTRY_ID
#MERGE (com)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(sop)
#MERGE (sop)-[riehc:intellectual_entity_has_component]->(com)
#"""

queryRelationSocialProfile_intellectual_entity_has_component_Follow = """
//Relation Real SocialProfile <-> Follow
MATCH (sop:SocialProfile)
MATCH (fol:Follow)
WHERE sop.ID = fol.PERSON_ID
MERGE (fol)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(sop)
MERGE (sop)-[riehc:intellectual_entity_has_component]->(fol)
"""

queryRelationSocialProfile_intellectual_entity_has_component_Tag = """
//Relation Real SocialProfile <-> Tag
MATCH (sop:SocialProfile)
MATCH (tag:Tag)
WHERE sop.EXID = tag.PROF_GUID
MERGE (tag)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(sop)
MERGE (sop)-[riehc:intellectual_entity_has_component]->(tag)
"""
#Ausführung der Cypher Queries mit NeoInterface
#neodb.query(queryRelationSocialProfile_intellectual_entity_has_component_Comment)
neodb.query(queryRelationSocialProfile_intellectual_entity_has_component_Follow)
neodb.query(queryRelationSocialProfile_intellectual_entity_has_component_Tag)