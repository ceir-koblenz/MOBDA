import pandas as pd
import pyodbc
import numpy
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
import logging

def importingNodeFolder(cnxn, graph) -> None:
    """
    graph as neo4j (Target DB) connector
    cnxn as dremio (Source DB) connector
    creation of File Nodes
    1 SQL query
    2 Load data into dataframe
    3 preprocess data
    4 cypher query
    5 execute cypher query with data from the dataframe
    """
        
    start_time = time.time()
   
    #SQL Queries
    sqlFolder= """
    SELECT ID as id, CREATE_DATE as created, LAST_UPDATE as last_updated, TITLE as title FROM "MOBDA_Datastore".Nodes."Uniconnect_Node_Folder" 
    """

    #Load Dataframes
    dfFolder = pd.read_sql(sqlFolder,cnxn)
    # print (dfFolder)

    logging.info("DataFrame finished --- %s seconds ---" % (time.time() - start_time))

    #Data Preprocessing
    #Timestamp (2 hour behind Timezone)

    #Cypher Queries
    NodeFolder = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Folder {id:row.id, title:row.title, created:row.created, last_updated:row.last_updated})
    """

    #Execute Import
    graph.execute_write_query_with_data(NodeFolder, dfFolder, database="neo4j")
   
    logging.info("Process Node Folder finished --- %s seconds ---" % (time.time() - start_time))

#Main Method
if __name__ == "__main__":
    importingNodeFolder()