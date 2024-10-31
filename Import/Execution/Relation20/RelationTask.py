import pandas as pd
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
import logging

logging.basicConfig(level=logging.INFO)

def createRelationTask(cnxn, graph) -> None:

    """
    creating all relations related to Activities database
    graph as neo4j (Target DB) connector
    cnxn as dremio (Source DB) connector
    1. SQL queries
    2. read data from dremio in dataframe
    3. cypher queries
    4. execute cypher queries with data from dataframes using pyneoinstance
    """
    start_time = time.time()

    #SQL Queries
    sqlRelationTasksTaskContainer= """
    SELECT taskid, containerid
    FROM MOBDA_Datastore.Relations.Tasks.Uniconnect_Relation_Task_TaskContainer
    """

    sqlRelationTasksComment_intellectual_entity_has_component = """
    SELECT taskid, commentid
    FROM MOBDA_Datastore.Relations.Tasks.Uniconnect_Relation_Tasks_Comment_intellectual_entity_has_component
    """
    sqlRelationTasksAttachment_intellectual_entity_has_component = """
    SELECT taskid, attachmentid
    FROM MOBDA_Datastore.Relations.Tasks.Uniconnect_Relation_Tasks_Attachment_intellectual_entity_has_component
    """
    sqlRelationTasksFollow_intellectual_entity_has_component = """
    SELECT taskid, followid
    FROM MOBDA_Datastore.Relations.Tasks.Uniconnect_Relation_Tasks_Follow_intellectual_entity_has_component
    """
    sqlRelationTasksTag_intellectual_entity_has_component = """
    SELECT tagid, taskid
    FROM MOBDA_Datastore.Relations.Tasks.Uniconnect_Relation_Tasks_Tag_intellectual_entitiy_has_component
    """
    sqlRelationTasks_task_has_parent = """
    SELECT parentid, childid
    FROM MOBDA_Datastore.Relations.Tasks.Uniconnect_Relation_Tasks_task_has_parent
    """


    #Load Dataframes
    dfRelationTasksAttachment_intellectual_entity_has_component= pd.read_sql(sqlRelationTasksAttachment_intellectual_entity_has_component,cnxn)
    print (dfRelationTasksAttachment_intellectual_entity_has_component)
    dfRelationTasksTaskContainer = pd.read_sql(sqlRelationTasksTaskContainer,cnxn)
    print (dfRelationTasksTaskContainer)
    dfRelationTasksComment_intellectual_entity_has_component= pd.read_sql(sqlRelationTasksComment_intellectual_entity_has_component,cnxn)
    print (dfRelationTasksComment_intellectual_entity_has_component)
    dfRelationTasksFollow_intellectual_entity_has_component= pd.read_sql(sqlRelationTasksFollow_intellectual_entity_has_component,cnxn)
    print (dfRelationTasksFollow_intellectual_entity_has_component)
    dfRelationTasksTag_intellectual_entity_has_component= pd.read_sql(sqlRelationTasksTag_intellectual_entity_has_component,cnxn)
    print (dfRelationTasksTag_intellectual_entity_has_component)
    dfRelationTasks_task_has_parent= pd.read_sql(sqlRelationTasks_task_has_parent,cnxn)
    print (dfRelationTasks_task_has_parent)
    

    logging.info(("DataFrame finished --- %s seconds ---" % (time.time() - start_time)))

    #Cypher Queries
    RelationTasksTaskContainer_task_contained_in_task_container= """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (t:Task{id:row.taskid})
    MATCH (tc:TaskContainer{id:row.containerid})
    CREATE (t)-[rbpcimb:task_contained_in_task_container {cardinality: "exactly 1"}]->(tc)
    CREATE (tc)-[rmbcbp:task_container_contains_task]->(t)
    """
    RelationTasksTaskContainer_intellecutal_entity_contained_in_container = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (t:Task{id:row.taskid})
    MATCH (tc:TaskContainer{id:row.containerid})
    CREATE (t)-[riecic:intellectual_entity_contained_in_container {cardinality: "exactly 1"}]->(tc)
    CREATE (tc)-[rccie:container_contains_intellectual_entity]->(t)
    """

    RelationTasksComment_intellectual_entity_has_component = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (t:Task{id:row.taskid})
    MATCH (c:Comment{id:row.commentid})
    CREATE (c)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(t)
    CREATE (t)-[riehc:intellectual_entity_has_component]->(c)
    """
    RelationTasksAttachment_intellectual_entity_has_component = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (t:Task{id:row.taskid})
    MATCH (at:Attachment{id:row.attachmentid})
    CREATE (at)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(t)
    CREATE (t)-[riehc:intellectual_entity_has_component]->(at)
    """
    RelationTasksFollow_intellectual_entity_has_component = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (t:Task{id:row.taskid})
    MATCH (f:Follow{id:row.followid})
    CREATE (f)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(t)
    CREATE (t)-[riehc:intellectual_entity_has_component]->(f)
    """
    
    RelationTasks_task_has_parent = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (tp:Task{id:row.parentid})
    MATCH (tc:Task{id:row.childid})
    CREATE (tc)-[rthp:task_has_parent {cardinality: "maximal 1"}]->(tp)
    CREATE (tp)-[rthc:task_has_child]->(tc)
    """
    RelationTasksTag_intellectual_entity_has_component = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (t:Task{id:row.taskid})
    MATCH (ta:Tag{id:row.tagid})
    CREATE (ta)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(t)
    CREATE (t)-[riehc:intellectual_entity_has_component]->(ta)
    """

    #Execute Import
    graph.execute_write_query_with_data(RelationTasksAttachment_intellectual_entity_has_component,dfRelationTasksAttachment_intellectual_entity_has_component, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_queries_with_data([RelationTasksTaskContainer_intellecutal_entity_contained_in_container, RelationTasksTaskContainer_task_contained_in_task_container], data=dfRelationTasksTaskContainer, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationTasksComment_intellectual_entity_has_component,dfRelationTasksComment_intellectual_entity_has_component, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationTasksTag_intellectual_entity_has_component,dfRelationTasksTag_intellectual_entity_has_component, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationTasksFollow_intellectual_entity_has_component,dfRelationTasksFollow_intellectual_entity_has_component, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationTasks_task_has_parent,dfRelationTasks_task_has_parent, database="neo4j", partitions= 12, parallel= True, workers= 12)

    

    ("ProcessEvent finished --- %s seconds ---" % (time.time() - start_time))


    # Close the Neo4j driver
    logging.info(("Process Relation Task finished --- %s seconds ---" % (time.time() - start_time)))

#Main method
if __name__ == "__main__":
    createRelationTask()