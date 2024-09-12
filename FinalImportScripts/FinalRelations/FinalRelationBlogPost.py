#Library für Neointerface für die Verbindung zu Neo4j
import neointerface
#Verbindung zu Neo4j 
neodb = neointerface.NeoInterface(host="neo4j://ma-lschloemer.bas.uni-koblenz.de:7687" , credentials=("neo4j", "neo4jneo4j"))

#Cypher Queries für Relations
queryRelationBlogPost_blog_post_contained_in_Weblog_Weblog = """
//Relation Real BlogPost <-> Weblog
MATCH (b:BlogPost)
MATCH (wb:Weblog)
WHERE b.WEBSITEID = wb.ID
MERGE (b)-[rbpciw:blog_post_contained_in_weblog {cardinality: "exactly 1"}]->(wb)
MERGE (wb)-[rwcbp:weblog_contains_blog_post]->(b)
"""

queryRelationBlogPost_intellectual_entity_has_component_Comment = """
//Relation Real BlogPost <-> Comment
MATCH (b:BlogPost)
MATCH (com:Comment)
WHERE b.ID = com.ENTRYID
MERGE (com)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(b)
MERGE (b)-[riehc:intellectual_entity_has_component]->(com)
"""

queryRelationBlogPost_intellectual_entity_has_component_Like = """
//Relation Real BlogPost <-> Like
MATCH (b:BlogPost)
MATCH (like:Like)
WHERE b.ID = like.ENTRYID
MERGE (like)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(b)
MERGE (b)-[riehc:intellectual_entity_has_component]->(like)
"""
queryRelationBlogPost_intellectual_entity_has_component_Tag = """
//Relation Real BlogPost <-> Tag
MATCH (b:BlogPost)
MATCH (tag:Tag)
WHERE b.ID = tag.ENTRYID
MERGE (tag)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(b)
MERGE (b)-[riehc:intellectual_entity_has_component]->(tag)
"""

neodb.query(queryRelationBlogPost_blog_post_contained_in_Weblog_Weblog)
neodb.query(queryRelationBlogPost_intellectual_entity_has_component_Comment)
neodb.query(queryRelationBlogPost_intellectual_entity_has_component_Like)
neodb.query(queryRelationBlogPost_intellectual_entity_has_component_Tag)
