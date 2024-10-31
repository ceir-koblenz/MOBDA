import pandas as pd
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
import logging

logging.basicConfig(level=logging.INFO)

def createRelationEvents(cnxn, graph) -> None:
    
    """
    creating all relations related to Event data
    graph as neo4j (Target DB) connector
    cnxn as dremio (Source DB) connector
    1. SQL queries
    2. read data from dremio in dataframe
    3. cypher queries
    4. execute cypher queries with data from dataframes using pyneoinstance
    """
    start_time = time.time()


    #SQL Queries
    sqlRelationEventsBlogPost_event_affects_item= """
    SELECT itemid, eventid
    FROM MOBDA_Datastore.Relations.Events.Uniconnect_Relation_Events_BlogPost_event_affects_item
     """

    sqlRelationEventsAttachment_event_affects_item= """
    SELECT eventid, attid
    FROM MOBDA_Datastore.Relations.Events.Uniconnect_Relation_Events_Attachment_event_affects_item
    
    """
    sqlRelationEventsBoardPost_event_affects_item= """
    SELECT eventid, boardid
    FROM MOBDA_Datastore.Relations.Events.Uniconnect_Relation_Events_BoardPost_event_affects_item
    
    """
    sqlRelationEventsComment_event_affects_item= """
    SELECT eventid, comid
    FROM "MOBDA_Datastore".Relations.Events."Uniconnect_Relation_Events_Comment_event_affects_item"
    
    """
    sqlRelationEventsFile_event_affects_item= """
    SELECT eventid, fileid
    FROM MOBDA_Datastore.Relations.Events.Uniconnect_Relation_Events_File_event_affects_item
    
    """
    sqlRelationEventsFolder_event_affects_item= """
    SELECT eventid, folderid
    FROM MOBDA_Datastore.Relations.Events.Uniconnect_Relation_Events_Folder_event_affects_item
    
    """
    sqlRelationEventsFollow_event_affects_item= """
    SELECT eventid, followid
    FROM MOBDA_Datastore.Relations.Events.Uniconnect_Relation_Events_Follow_event_affects_item
    
    """
    sqlRelationEventsLike_event_affects_item= """
    SELECT eventid, likeid
    FROM MOBDA_Datastore.Relations.Events.Uniconnect_Relation_Events_Like_event_affects_item
    
    """
    sqlRelationEventsSocialProfile_event_affects_item= """
    SELECT eventid, sprofileid
    FROM MOBDA_Datastore.Relations.Events.Uniconnect_Relation_Events_SocialProfile_event_affects_item
    
    """
    sqlRelationEventsMicroblogPost_event_affects_item= """
    SELECT eventid, mblogid
    FROM MOBDA_Datastore.Relations.Events.Uniconnect_Relation_Events_MicroblogPost_event_affects_item
    
    """
    sqlRelationEventsTask_event_affects_item= """
    SELECT eventid, taskid
    FROM MOBDA_Datastore.Relations.Events.Uniconnect_Relation_Events_Task_event_affects_item
    
    """
    sqlRelationEventsWikiPage_event_affects_item= """
    SELECT eventid, wikiid
    FROM MOBDA_Datastore.Relations.Events.Uniconnect_Relation_Events_WikiPage_event_affects_item
    """

    #Load Dataframes
    dfRelationEventsBlogPost_event_affects_item= pd.read_sql(sqlRelationEventsBlogPost_event_affects_item,cnxn)
    print (dfRelationEventsBlogPost_event_affects_item)
    dfRelationEventsAttachment_event_affects_item= pd.read_sql(sqlRelationEventsAttachment_event_affects_item,cnxn)
    print (dfRelationEventsAttachment_event_affects_item)
    dfRelationEventsBoardPost_event_affects_item= pd.read_sql(sqlRelationEventsBoardPost_event_affects_item,cnxn)
    print (dfRelationEventsBoardPost_event_affects_item)
    dfRelationEventsComment_event_affects_item= pd.read_sql(sqlRelationEventsComment_event_affects_item,cnxn)
    print (dfRelationEventsComment_event_affects_item)
    dfRelationEventsFile_event_affects_item= pd.read_sql(sqlRelationEventsFile_event_affects_item,cnxn)
    print (dfRelationEventsFile_event_affects_item)
    dfRelationEventsFolder_event_affects_item= pd.read_sql(sqlRelationEventsFolder_event_affects_item,cnxn)
    print (dfRelationEventsFolder_event_affects_item)
    dfRelationEventsFollow_event_affects_item= pd.read_sql(sqlRelationEventsFollow_event_affects_item,cnxn)
    print (dfRelationEventsFollow_event_affects_item)
    dfRelationEventsLike_event_affects_item= pd.read_sql(sqlRelationEventsLike_event_affects_item,cnxn)
    print (dfRelationEventsLike_event_affects_item)
    dfRelationEventsSocialProfile_event_affects_item= pd.read_sql(sqlRelationEventsSocialProfile_event_affects_item,cnxn)
    print (dfRelationEventsSocialProfile_event_affects_item)
    dfRelationEventsMicroblogPost_event_affects_item= pd.read_sql(sqlRelationEventsMicroblogPost_event_affects_item,cnxn)
    print (dfRelationEventsMicroblogPost_event_affects_item)
    dfRelationEventsTask_event_affects_item= pd.read_sql(sqlRelationEventsTask_event_affects_item,cnxn)
    print (dfRelationEventsTask_event_affects_item)
    dfRelationEventsWikiPage_event_affects_item= pd.read_sql(sqlRelationEventsWikiPage_event_affects_item,cnxn)
    print (dfRelationEventsWikiPage_event_affects_item)

    logging.info(("DataFrame finished --- %s seconds ---" % (time.time() - start_time)))

    #Cypher Queries
    RelationEventsBlogPost_event_affects_item= """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (ev:Event{id:row.eventid})
    MATCH (b:BlogPost{id:row.itemid})
    CREATE (ev)-[reai:event_affects_item {cardinality: "exactly 1"}]->(b)
    CREATE (b)-[rmbcbp:item_affected_by_event]->(ev)
    """
    RelationEventsAttachment_event_affects_item= """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (ev:Event{id:row.eventid})
    MATCH (at:Attachment{id:row.attid})
    CREATE (ev)-[reai:event_affects_item {cardinality: "exactly 1"}]->(at)
    CREATE (at)-[rmbcbp:item_affected_by_event]->(ev)
    """
    RelationEventsBoardPost_event_affects_item= """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (ev:Event{id:row.eventid})
    MATCH (bp:BoardPost{id:row.boardid})
    CREATE (ev)-[reai:event_affects_item {cardinality: "exactly 1"}]->(bp)
    CREATE (bp)-[rmbcbp:item_affected_by_event]->(ev)
    """

    RelationEventsComment_event_affects_item= """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (ev:Event{id:row.eventid})
    MATCH (co:Comment{id:row.comid})
    CREATE (ev)-[reai:event_affects_item {cardinality: "exactly 1"}]->(co)
    CREATE (co)-[rmbcbp:item_affected_by_event]->(ev)
    """

    RelationEventsFile_event_affects_item= """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (ev:Event{id:row.eventid})
    MATCH (f:File{id:row.fileid})
    CREATE (ev)-[reai:event_affects_item {cardinality: "exactly 1"}]->(f)
    CREATE (f)-[rmbcbp:item_affected_by_event]->(ev)
    """

    RelationEventsFolder_event_affects_item= """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (ev:Event{id:row.eventid})
    MATCH (f:Folder{id:row.folderid})
    CREATE (ev)-[reai:event_affects_item {cardinality: "exactly 1"}]->(f)
    CREATE (f)-[rmbcbp:item_affected_by_event]->(ev)
    """

    RelationEventsFollow_event_affects_item= """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (ev:Event{id:row.eventid})
    MATCH (f:Follow{id:row.followid})
    CREATE (ev)-[reai:event_affects_item {cardinality: "exactly 1"}]->(f)
    CREATE (f)-[rmbcbp:item_affected_by_event]->(ev)
    """

    RelationEventsLike_event_affects_item= """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (ev:Event{id:row.eventid})
    MATCH (li:Like{id:row.likeid})
    CREATE (ev)-[reai:event_affects_item {cardinality: "exactly 1"}]->(li)
    CREATE (li)-[rmbcbp:item_affected_by_event]->(ev)
    """

    RelationEventsSocialProfile_event_affects_item= """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (ev:Event{id:row.eventid})
    MATCH (so:SocialProfile{id:row.sprofileid})
    CREATE (ev)-[reai:event_affects_item {cardinality: "exactly 1"}]->(so)
    CREATE (so)-[rmbcbp:item_affected_by_event]->(ev)
    """

    RelationEventsMicroblogPost_event_affects_item= """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (ev:Event{id:row.eventid})
    MATCH (mb:MicroblogPost{id:row.mblogid})
    CREATE (ev)-[reai:event_affects_item {cardinality: "exactly 1"}]->(mb)
    CREATE (mb)-[rmbcbp:item_affected_by_event]->(ev)
    """

    RelationEventsTask_event_affects_item= """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (ev:Event{id:row.eventid})
    MATCH (ta:Task{id:row.taskid})
    CREATE (ev)-[reai:event_affects_item {cardinality: "exactly 1"}]->(ta)
    CREATE (ta)-[rmbcbp:item_affected_by_event]->(ev)
    """

    RelationEventsWikiPage_event_affects_item= """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (ev:Event{id:row.eventid})
    MATCH (wi:WikiPage{id:row.wikiid})
    CREATE (ev)-[reai:event_affects_item {cardinality: "exactly 1"}]->(wi)
    CREATE (wi)-[rmbcbp:item_affected_by_event]->(ev)
    """

    #Execute Import

    graph.execute_write_query_with_data(RelationEventsBlogPost_event_affects_item,dfRelationEventsBlogPost_event_affects_item, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationEventsAttachment_event_affects_item,dfRelationEventsAttachment_event_affects_item, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationEventsBoardPost_event_affects_item,dfRelationEventsBoardPost_event_affects_item, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationEventsComment_event_affects_item,dfRelationEventsComment_event_affects_item, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationEventsFile_event_affects_item,dfRelationEventsFile_event_affects_item, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationEventsFolder_event_affects_item,dfRelationEventsFolder_event_affects_item, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationEventsFollow_event_affects_item,dfRelationEventsFollow_event_affects_item, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationEventsLike_event_affects_item,dfRelationEventsLike_event_affects_item, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationEventsSocialProfile_event_affects_item,dfRelationEventsSocialProfile_event_affects_item, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationEventsMicroblogPost_event_affects_item,dfRelationEventsMicroblogPost_event_affects_item, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationEventsTask_event_affects_item,dfRelationEventsTask_event_affects_item, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationEventsWikiPage_event_affects_item,dfRelationEventsWikiPage_event_affects_item, database="neo4j", partitions= 12, parallel= True, workers= 12)
    
    ("ProcessEvent finished --- %s seconds ---" % (time.time() - start_time))


    # Close the Neo4j driver
    logging.info(("Process Relation Event finished --- %s seconds ---" % (time.time() - start_time)))
    
#Main method
if __name__ == "__main__":
    createRelationEvents()