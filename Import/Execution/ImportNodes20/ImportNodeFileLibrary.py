import pandas as pd
import pyodbc
import numpy
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
import logging

logging.basicConfig(level=logging.INFO)

def importingNodeFileLibrary(cnxn, graph) -> None:

    """
    graph as neo4j (Target DB) connector
    cnxn as dremio (Source DB) connector
    creation of FileLibrary Nodes
    1 SQL query
    2 Load data into dataframe
    3 preprocess data
    4 cypher query
    5 execute cypher query with data from the dataframe
    """
    start_time = time.time()

    #SQL Queries
    sqlFileLibrary= """
    SELECT libid AS id, TITLE as title 
    FROM "MOBDA_Datastore".Nodes."Uniconnect_Node_FileLibrary"
    """

    #Load Dataframes
    dfFileLibrary = pd.read_sql(sqlFileLibrary,cnxn)
    # print (dfFileLibrary)

    logging.info("DataFrame finished --- %s seconds ---" % (time.time() - start_time))

    #Data Preprocessing
    #Timestamp (2 hour behind Timezone)
    #Cypher Queries

    NodeFileLibrary = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:FileLibrary {id:row.id, title:row.title})
    """

    #Execute Import
    graph.execute_write_query_with_data(NodeFileLibrary, dfFileLibrary, database="neo4j")

    logging.info("Process Node FileLibrary finished --- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    importingNodeFileLibrary()