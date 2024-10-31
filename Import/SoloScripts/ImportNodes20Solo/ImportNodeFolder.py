import pandas as pd
import pyodbc
import numpy
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO)

def importingNodeFolder()-> None:

    """
    creating all nodes related to Folder data
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
    sqlFolder= """
    SELECT ID as id, CREATE_DATE as created, LAST_UPDATE as last_updated, TITLE as title FROM "MOBDA_Datastore".Nodes."Uniconnect_Node_Folder" 
    """

    #Load Dataframes
    dfFolder = pd.read_sql(sqlFolder,cnxn)
    print (dfFolder)

    logging.info(("DataFrame finished --- %s seconds ---" % (time.time() - start_time)))

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
    ("ProcessEvent finished --- %s seconds ---" % (time.time() - start_time))

    logging.info(("Process finished --- %s seconds ---" % (time.time() - start_time)))

#Main Method
if __name__ == "__main__":
    importingNodeFolder()