#Library für Neointerface für die Verbindung zu Neo4j
import neointerface
#Verbindung zu Neo4j 
neodb = neointerface.NeoInterface(host="neo4j://ma-lschloemer.bas.uni-koblenz.de:7687" , credentials=("neo4j", "neo4jneo4j"))

#Cypher Queries für Relations

queryRelationTask_intellectual_entity_has_component_Attachment = """
//Relation Real Task  <-> Attachment
MATCH (task:Task)
MATCH (att:Attachment)
WHERE task.ID = att.PARENTUUID
MERGE (att)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(task)
MERGE (task)-[riehc:intellectual_entity_has_component]->(att)
"""

queryRelationTask_intellectual_entity_has_component_Comment = """
//Relation Task  <-> Comment
MATCH (task:Task)
MATCH (com:Comment)
WHERE task.ID = com.PARENTUUID
MERGE (com)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(task)
MERGE (task)-[riehc:intellectual_entity_has_component]->(com)
"""

queryRelationTask_intellectual_entity_has_component_Follow = """
//Relation Task  <-> Follow
MATCH (task:Task)
MATCH (fol:Follow)
WHERE task.ID = fol.PARENTUUID
MERGE (fol)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(task)
MERGE (task)-[riehc:intellectual_entity_has_component]->(fol)
"""

queryRelationTask_intellectual_entity_has_component_Tag = """
//Relation Real Task  <-> Tag
MATCH (task:Task)
MATCH (tag:Tag)
WHERE task.ID = tag.NODEUUID
MERGE (tag)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(task)
MERGE (task)-[riehc:intellectual_entity_has_component]->(tag)
"""

queryRelationTask_task_contained_task_container_TaskContainer = """
//Relation  Task  <-> TaskContainer
MATCH (task:Task)
MATCH (taskc:TaskContainer)
WHERE task.ACTIVITYUUID = taskc.ID
MERGE (task)-[rtcitc:task_contained_in_task_container {cardinality: "exactly 1"}]->(taskc)
MERGE (taskc)-[rtcct:task_container_contains_task]->(task)
"""

queryRelationTask_task_has_child_Task = """
//Relation  Task  <-> Task Parent/Child
MATCH (childtask:Task)
MATCH (parenttask:Task)
WHERE parenttask.PARENTUUID = childtask.ID 
MERGE (childtask)-[rthp:task_has_parent {cardinality: "maximal 1"}]->(parenttask)
MERGE (parenttask)-[rthc:task_has_child]->(childtask)
"""

neodb.query(queryRelationTask_intellectual_entity_has_component_Attachment)
neodb.query(queryRelationTask_intellectual_entity_has_component_Comment)
neodb.query(queryRelationTask_intellectual_entity_has_component_Follow)
neodb.query(queryRelationTask_intellectual_entity_has_component_Tag)
neodb.query(queryRelationTask_task_contained_task_container_TaskContainer)
neodb.query(queryRelationTask_task_has_child_Task)