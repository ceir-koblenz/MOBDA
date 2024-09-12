#Library für Neointerface für die Verbindung zu Neo4j
import neointerface
#Verbindung zu Neo4j 
neodb = neointerface.NeoInterface(host="neo4j://ma-lschloemer.bas.uni-koblenz.de:7687" , credentials=("neo4j", "neo4jneo4j"))

#Cypher Queries für Relations
queryRelationAttachment_intellectual_component_has_simple_component_LikeSP = """
//1. Step Relation Real SocialProfile Comment Attachment <-> SocialProflie Commment Attachemnt Like
MATCH (att:Attachment)
MATCH (lik:Like)
WHERE att.ID = lik.OBJECT_ID
MERGE (lik)-[rscoic:simple_component_of_intellectual_component {cardinality: "exactly 1"}]->(att)
MERGE (att)-[richsc:intellectual_component_has_simple_component]->(lik)
"""

queryRelationAttachment_intellectual_component_has_simple_component_LikeMbP = """
//2. Step Relation Real MicroblogPost Attachment <-> MicroblogPost Attachemnt Like
MATCH (att:Attachment)
MATCH (lik:Like)
WHERE att.OBJECT_EXTERNAL_ID = lik.MATCH_MEDIA_ID
MERGE (lik)-[rscoic:simple_component_of_intellectual_component {cardinality: "exactly 1"}]->(att)
MERGE (att)-[richsc:intellectual_component_has_simple_component]->(lik)
"""

queryRelationComment_intellectual_component_has_simple_component_LikeBP = """
//1. Step Relation BlogPost Comment <-> BlogPost Comment Like
MATCH (com:Comment)
MATCH (lik:Like)
WHERE com.ID = lik.COMMENTID
MERGE (lik)-[rscoic:simple_component_of_intellectual_component {cardinality: "exactly 1"}]->(com)
MERGE (com)-[richsc:intellectual_component_has_simple_component]->(lik)
"""

queryRelationComment_intellectual_component_has_simple_component_LikeBoP = """
//2. Step Relation BoardPost Comment <-> BoardPost Comment Like
MATCH (com:Comment)
MATCH (lik:Like)
WHERE com.ID = lik.NODEID
MERGE (lik)-[rscoic:simple_component_of_intellectual_component {cardinality: "exactly 1"}]->(com)
MERGE (com)-[richsc:intellectual_component_has_simple_component]->(lik)

"""

queryRelationComment_intellectual_component_has_simple_component_LikeMP = """
//3. Step Relation MicroblogPost Comment <-> MicroblogPost Comment Like
MATCH (com:Comment)
MATCH (lik:Like)
WHERE com.ID = lik.COMMENT_ID
MERGE (lik)-[rscoic:simple_component_of_intellectual_component {cardinality: "exactly 1"}]->(com)
MERGE (com)-[richsc:intellectual_component_has_simple_component]->(lik)
"""

queryRelationComment_intellectual_component_has_simple_component_LikeSP = """
//4. Step Relation SocialProflie Comment <-> SocialProfile Comment Like
MATCH (com:Comment)
MATCH (lik:Like)
WHERE com.ID = lik.ENTRY_ID
MERGE (lik)-[rscoic:simple_component_of_intellectual_component {cardinality: "exactly 1"}]->(com)
MERGE (com)-[richsc:intellectual_component_has_simple_component]->(lik)
"""

queryRelationPerson_agent_related_to_organisation_Organisation = """
//Relation Organisation <-> Person
MATCH (org:Organisation)
MATCH (per:Person)
MERGE (org)-[rorta:organisation_related_to_agent]->(per)
MERGE (per)-[raha:agent_related_to_organisation]->(org)
"""

neodb.query(queryRelationAttachment_intellectual_component_has_simple_component_LikeSP)
neodb.query(queryRelationAttachment_intellectual_component_has_simple_component_LikeMbP)
neodb.query(queryRelationComment_intellectual_component_has_simple_component_LikeBP)
neodb.query(queryRelationComment_intellectual_component_has_simple_component_LikeBoP)
neodb.query(queryRelationComment_intellectual_component_has_simple_component_LikeMP)
neodb.query(queryRelationComment_intellectual_component_has_simple_component_LikeSP)
neodb.query(queryRelationPerson_agent_related_to_organisation_Organisation)