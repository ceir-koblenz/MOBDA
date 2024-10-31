import pandas as pd
import pyodbc
import numpy
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO)

def importingNodeBoardPost() -> None:

    """
    creating all nodes related to BoardPost data
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
    logging.info((db_info['uri']))
    graph = Neo4jInstance(db_info['uri'],db_info['database'],db_info['password'])

    DSN = "Arrow Flight SQL ODBC DSN"
    
    cnxn = pyodbc.connect(DSN=DSN ,autocommit=True)

    #SQL Queries
    sqlBoardPost= """
    SELECT NODEUUID as id, CREATED as created, NAME as title, DESCRIPTION as content, LASTMOD as last_updated 
    FROM "MOBDA_Datastore".Nodes."Uniconnect_Node_BoardPost" 
    """

    #Load Dataframes
    dfBoardPost = pd.read_sql(sqlBoardPost,cnxn)
    print (dfBoardPost)

    logging.info(("DataFrame finished --- %s seconds ---" % (time.time() - start_time)))

    #Data Preprocessing
    dfBoardPost['content'] = dfBoardPost['content'].fillna('NaN')
    dfBoardPost['content'] = dfBoardPost[['content']].applymap(lambda text: BeautifulSoup(text, 'html.parser').get_text())
    dfBoardPost['content'] = dfBoardPost['content'].str.replace('\n', '')
    dfBoardPost['content'] = dfBoardPost['content'].str.replace('\t', '')
    dfBoardPost['content'] = dfBoardPost['content'].str.replace('\r', '')
    dfBoardPost['content'] = dfBoardPost['content'].str.replace('\v', '')
    print(dfBoardPost)

    #Cypher Queries

    NodeBoardPost = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:BoardPost {id:row.id, title:row.title, created:row.created, last_updated:row.last_updated, content:row.content})
    """

    #Execute Import

    graph.execute_write_query_with_data(NodeBoardPost, dfBoardPost, database="neo4j")
    ("ProcessEvent finished --- %s seconds ---" % (time.time() - start_time))

    logging.info(("Process finished --- %s seconds ---" % (time.time() - start_time)))
    
#Main Method
if __name__ == "__main__":
   importingNodeBoardPost()