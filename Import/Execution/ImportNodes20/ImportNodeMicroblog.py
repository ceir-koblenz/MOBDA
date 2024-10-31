import pandas as pd
import pyodbc
import numpy
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
import logging

logging.basicConfig(level=logging.INFO)

def importingNodeMicroblog(cnxn, graph):

    """
    graph as neo4j (Target DB) connector
    cnxn as dremio (Source DB) connector
    creation of Microblog Nodes
    1 SQL query
    2 Load data into dataframe
    3 preprocess data
    4 cypher query
    5 execute cypher query with data from the dataframe
    """
    start_time = time.time()

    #SQL Queries
    sqlMicoblog= """
    SELECT BOARD_CONTAINER_ID as id FROM "MOBDA_Datastore".Nodes."Uniconnect_Node_Microblog"
    """

    #Load Dataframes
    dfMicroblog = pd.read_sql(sqlMicoblog,cnxn)
    # print (dfMicroblog)
    logging.info("DataFrame finished --- %s seconds ---" % (time.time() - start_time))

    #Data Preprocessing
    # not needed here

    #Cypher Query
    NodeMicroblog = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Microblog {id:row.id})
    """

    #Execute Import
    graph.execute_write_query_with_data(NodeMicroblog, dfMicroblog, database="neo4j")
   
    logging.info("Process Node Microblog finished --- %s seconds ---" % (time.time() - start_time))

#Main Method
if __name__ == "__main__":
    importingNodeMicroblog()