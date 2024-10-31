import pandas as pd
import pyodbc
import numpy
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
import logging

logging.basicConfig(level=logging.INFO)

def importingNodeEvent()-> None:
    """
    creating all nodes related to Event data
    1. Initiate connection to Neo4j and Dremio
    2. SQL queries
    3. read data from dremio in dataframe
    4. cypher queries
    5. execute cypher queries with data from dataframes using pyneoinstance
    """
    
    start_time = time.time()

    # Set up connections
    config = load_yaml_file('C:/Users/lschloemer/Nextcloud/MOBDA 2.0/VSCodeMOBDARepository/Python/a.yaml')
    db_info = config['db_infoneo']
    graph = Neo4jInstance(db_info['uri'],db_info['database'],db_info['password'])
    
    DSN = "Arrow Flight SQL ODBC DSN"

    cnxn = pyodbc.connect(DSN=DSN ,autocommit=True)

    #SQL Queries
    sqlEvent= """
    SELECT "Event ID" as id, Activity as title, "Event Action" as action, "Event Local Timestamp" as created 
    FROM "MOBDA_Datastore".Nodes."Uniconnect_Node_Event" 
    """

    #Load Dataframes
    dfEvent = pd.read_sql(sqlEvent,cnxn)
    dfEvent['created'] = pd.to_datetime(dfEvent['created'])

    logging.info(("DataFrame finished --- %s seconds ---" % (time.time() - start_time)))

    #Data Preprocessing

    #Cypher Queries

    NodeEvent = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Event {id:row.id, title:row.title, action:row.action, created:row.created})
    """

    #Execute Import

    graph.execute_write_query_with_data(NodeEvent, dfEvent, database="neo4j", partitions= 12, parallel= True, workers= 12)
    ("ProcessEvent finished --- %s seconds ---" % (time.time() - start_time))

    logging.info(("Process finished --- %s seconds ---" % (time.time() - start_time)))

#Main Method
if __name__ == "__main__":
    importingNodeEvent()