import pandas as pd
import pyodbc
import numpy
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO)

def importingNodeMicroblog()-> None:
    """
    creating all nodes related to Microblog data
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
    sqlMicoblog= """
    SELECT BOARD_CONTAINER_ID as id FROM "MOBDA_Datastore".Nodes."Uniconnect_Node_Microblog"
    """

    #Load Dataframes
    dfMicroblog = pd.read_sql(sqlMicoblog,cnxn)
    print (dfMicroblog)

    logging.info(("DataFrame finished --- %s seconds ---" % (time.time() - start_time)))

    #Data Preprocessing

    #Cypher Queries

    NodeMicroblog = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Microblog {id:row.id})
    """

    #Execute Import

    graph.execute_write_query_with_data(NodeMicroblog, dfMicroblog, database="neo4j")
    ("ProcessEvent finished --- %s seconds ---" % (time.time() - start_time))

    logging.info(("Process finished --- %s seconds ---" % (time.time() - start_time)))

#Main Method
if __name__ == "__main__":
    importingNodeMicroblog()