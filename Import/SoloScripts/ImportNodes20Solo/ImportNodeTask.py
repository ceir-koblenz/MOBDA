import pandas as pd
import pyodbc
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO)

def importingNodeTask()-> None:

    """
    creating all nodes related to Task data
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
    sqlTask= """
    SELECT NODEUUID as id, CREATED as created, LASTMOD as last_updated, DESCRIPTION as content, NAME as title
    FROM "MOBDA_Datastore".Nodes."Uniconnect_Node_Task"
    """

    #Load Dataframes
    dfTask = pd.read_sql(sqlTask,cnxn)
    print (dfTask)

    logging.info(("DataFrame finished --- %s seconds ---" % (time.time() - start_time)))

    #Data Preprocessing
    dfTask['content'] = dfTask['content'].fillna('NaN')
    dfTask['content'] = dfTask[['content']].applymap(lambda text: BeautifulSoup(text, 'html.parser').get_text())
    dfTask['content'] = dfTask['content'].str.replace('\n', '')
    dfTask['content'] = dfTask['content'].str.replace('\t', '')
    dfTask['content'] = dfTask['content'].str.replace('\r', '')
    dfTask['content'] = dfTask['content'].str.replace('\v', '')
    print (dfTask)

    #Cypher Queries
    NodeTask = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Task {id:row.id, created:row.created, last_updated:row.last_updated, content:row.content, title:row.title})
    """

    #Execute Import
    graph.execute_write_query_with_data(NodeTask, dfTask, "neo4j")
    ("ProcessEvent finished --- %s seconds ---" % (time.time() - start_time))

    # Close the Neo4j driver
    logging.info(("Process finished --- %s seconds ---" % (time.time() - start_time)))

#Main Method
if __name__ == "__main__":
    importingNodeTask()