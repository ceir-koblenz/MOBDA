import pandas as pd
import pyodbc
import numpy
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
import logging

logging.basicConfig(level=logging.INFO)

def importingNodeGroupWorkspace(cnxn, graph) -> None:
    """
    graph as neo4j (Target DB) connector
    cnxn as dremio (Source DB) connector
    creation of GroupWorkspace Nodes
    1 SQL query
    2 Load data into dataframe
    3 preprocess data
    4 cypher query
    5 execute cypher query with data from the dataframe
    """
    start_time = time.time()

    #SQL Queries
    sqlGroupWorkspace= """
    SELECT COMMUNITY_UUID as id, NAME as title FROM "MOBDA_Datastore".Nodes."Uniconnect_Node_GroupWorkspace"
    """

    #Load Dataframes
    dfGroupWorkspace = pd.read_sql(sqlGroupWorkspace,cnxn)
    # print(dfGroupWorkspace)

    logging.info("DataFrame finished --- %s seconds ---" % (time.time() - start_time))

    #Data Preprocessing
    # not needed

    #Cypher Queries
    NodeGroupWorkspace = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:GroupWorkspace {id:row.id, title:row.title})
    """

    #Execute Import
    graph.execute_write_query_with_data(NodeGroupWorkspace, dfGroupWorkspace, database="neo4j")
    
    logging.info("Process Node GroupWorkspace finished --- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    importingNodeGroupWorkspace()