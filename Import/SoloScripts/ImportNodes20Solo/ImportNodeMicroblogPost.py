import pandas as pd
import pyodbc
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO)

def importingNodeMicroblogPost()-> None:
    """
    creating all nodes related to MicroblogPost data
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
    sqlMicroblogPost= """
    SELECT ENTRY_ID as id, CREATION_DATE as created, UPDATE_DATE as last_updated, CONTENT as content FROM "MOBDA_Datastore".Nodes."Uniconnect_Node_MicroblogPost"
    """

    #Load Dataframes
    dfMicroblogPost = pd.read_sql(sqlMicroblogPost,cnxn)
    print (dfMicroblogPost)
   
    logging.info(("DataFrame finished --- %s seconds ---" % (time.time() - start_time)))

    #Data Preprocessing
    dfMicroblogPost['content'] = dfMicroblogPost['content'].fillna('NaN')
    dfMicroblogPost['content'] = dfMicroblogPost[['content']].applymap(lambda text: BeautifulSoup(text, 'html.parser').get_text())
    dfMicroblogPost['content'] = dfMicroblogPost['content'].str.replace('\n', '')
    dfMicroblogPost['content'] = dfMicroblogPost['content'].str.replace('\t', '')
    dfMicroblogPost['content'] = dfMicroblogPost['content'].str.replace('\r', '')
    dfMicroblogPost['content'] = dfMicroblogPost['content'].str.replace('\v', '')
    print (dfMicroblogPost)

    #Cypher Queries

    NodeMicroblogPost = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:MicroblogPost {id:row.id, created:row.created, last_updated:row.last_updated, content:row.content})
    """

    #Execute Import
    graph.execute_write_query_with_data(NodeMicroblogPost, dfMicroblogPost, database="neo4j")

    ("ProcessEvent finished --- %s seconds ---" % (time.time() - start_time))

    logging.info(("Process finished --- %s seconds ---" % (time.time() - start_time)))

#Main Method
if __name__ == "__main__":
    importingNodeMicroblogPost()