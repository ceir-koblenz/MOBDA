#Library für Neointerface für die Verbindung zu Neo4j
import neointerface
#Verbindung zu Neo4j 
neodb = neointerface.NeoInterface(host="neo4j://ma-lschloemer.bas.uni-koblenz.de:7687" , credentials=("neo4j", "neo4jneo4j"))

#Cypher Queries für Relations
queryRelationWikiPage_intellectual_entity_has_component_Attachment = """
//Relation WikiPage <-> Attachment
MATCH (wipa:WikiPage)
MATCH (att:Attachment)
WHERE wipa.MEDIA_ID = att.MEDIA_ID
MERGE (att)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(wipa)
MERGE (wipa)-[riehc:intellectual_entity_has_component]->(att)
"""

queryRelationWikiPage_intellectual_entity_has_component_Comment = """
//Relation WikiPage <-> Comment
MATCH (wipa:WikiPage)
MATCH (com:Comment)
WHERE wipa.MEDIA_ID = com.MEDIA_ID
MERGE (com)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(wipa)
MERGE (wipa)-[riehc:intellectual_entity_has_component]->(com)
"""

queryRelationWikiPage_intellectual_entity_has_component_Follow = """
//Relation  WikiPage  <-> Follow
MATCH (wipa:WikiPage)
MATCH (fol:Follow)
WHERE wipa.ID = fol.WIKI_ID
MERGE (wipa)-[riehc:intellectual_entity_has_component {cardinality: "exactly 1"}]->(fol)
MERGE (fol)-[rcoie:component_of_intellectual_entity]->(wipa)
"""

queryRelationWikiPage_intellectual_entity_has_component_Like = """
//Relation  WikiPage  <-> Like
MATCH (wipa:WikiPage)
MATCH (like:Like)
WHERE wipa.ID = like.WIKI_ID
MERGE (wipa)-[riehc:intellectual_entity_has_component {cardinality: "exactly 1"}]->(like)
MERGE (like)-[rcoie:component_of_intellectual_entity]->(wipa)
"""

queryRelationWikipage_intellectual_entity_has_previous_version_WikiPage = """
//Relation WikiPage < previous Version > Wikipage
MATCH (wipanext:WikiPage)
MATCH (wipapre:WikiPage)
WHERE wipanext.SUB_ID = wipapre.PREVIOUS_ID
MERGE (wipanext)-[riehpv:intellectual_entity_has_previous_version {cardinality: "maximal 1"}]->(wipapre)
MERGE (wipapre)-[richnv:intellectual_entity_has_next_version {cardinality: "maximal 1"}]->(wipanext)
"""

queryRelationWikiPage_intellectual_entity_has_recent_version_Wikipage = """
//Relation WikiPage < recent Version > WikiPage
MATCH (wipaold:WikiPage)
MATCH (wiparecent:WikiPage)
WHERE wipaold.ID = wiparecent.CURRENT_REVISION_ID
MERGE (wipaold)-[riehrv:intellectual_entity_has_recent_version {cardinality: "exactly 1"}]->(wiparecent)
MERGE (wiparecent)-[ricov:intellectual_entity_has_old_version ]->(wipaold)
"""

#Ausführen der Cypher Queries (durch auskommentieren kann auch nur ein Teil ausgeführt werden)
neodb.query(queryRelationWikiPage_intellectual_entity_has_component_Attachment)
neodb.query(queryRelationWikiPage_intellectual_entity_has_component_Comment )
neodb.query(queryRelationWikiPage_intellectual_entity_has_component_Follow)
neodb.query(queryRelationWikiPage_intellectual_entity_has_component_Like)
neodb.query(queryRelationWikipage_intellectual_entity_has_previous_version_WikiPage)
neodb.query(queryRelationWikiPage_intellectual_entity_has_recent_version_Wikipage)
