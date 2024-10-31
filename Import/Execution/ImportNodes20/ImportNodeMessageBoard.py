import pandas as pd
import pyodbc
import numpy
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
import logging

logging.basicConfig(level=logging.INFO)

def importingNodeMessageBoard(cnxn, graph):
    """
    graph as neo4j (Target DB) connector
    cnxn as dremio (Source DB) connector
    creation of MessageBoard Nodes
    1 SQL query
    2 Load data into dataframe
    3 preprocess data
    4 cypher query
    5 execute cypher query with data from the dataframe
    """
    start_time = time.time()

    #SQL Queries
    sqlMessageBoard= """
    SELECT FORUMUUID as id FROM "MOBDA_Datastore".Nodes."Uniconnect_Node_MessageBoard"
    """

    #Load Dataframes
    dfMessageBoard = pd.read_sql(sqlMessageBoard,cnxn)
    # print (dfMessageBoard)
    logging.info("DataFrame finished --- %s seconds ---" % (time.time() - start_time))

    #Data Preprocessing

    #Cypher Queries
    NodeMessageBoard = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:MessageBoard {id:row.id})
    """

    #Execute Import
    graph.execute_write_query_with_data(NodeMessageBoard, dfMessageBoard, database="neo4j")

    logging.info("Process Node MessageBoard finished --- %s seconds ---" % (time.time() - start_time))
#Main method 
if __name__ == "__main__":
    importingNodeMessageBoard()