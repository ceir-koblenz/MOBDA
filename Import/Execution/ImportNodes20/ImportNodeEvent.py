import pandas as pd
import pyodbc
import numpy
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
import logging

logging.basicConfig(level=logging.INFO)

def importingNodeEvent(cnxn, graph) -> None:
    """
    graph as neo4j (Target DB) connector
    cnxn as dremio (Source DB) connector
    creation of Event Nodes
    1 SQL query
    2 Load data into dataframe
    3 preprocess data
    4 cypher query
    5 execute cypher query with data from the dataframe
    """
    start_time = time.time()

    #SQL Queries
    sqlEvent= """
    SELECT "Event ID" as id, Activity as title, "Event Action" as action, "Event Local Timestamp" as created 
    FROM "MOBDA_Datastore".Nodes."Uniconnect_Node_Event" 
    """

    #Load Dataframes
    dfEvent = pd.read_sql(sqlEvent,cnxn)

    #Data Preprocessing
    dfEvent['created'] = pd.to_datetime(dfEvent['created'])
    
    logging.info("DataFrame finished --- %s seconds ---" % (time.time() - start_time))

    #Cypher Queries

    NodeEvent = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Event {id:row.id, title:row.title, action:row.action, created:row.created})
    """
    #Execute Import
    graph.execute_write_query_with_data(NodeEvent, dfEvent, database="neo4j", partitions= 12, parallel= True, workers= 12)

    logging.info("Process Node Event finished --- %s seconds ---" % (time.time() - start_time))
#Main method
if __name__ == "__main__":
    importingNodeEvent()