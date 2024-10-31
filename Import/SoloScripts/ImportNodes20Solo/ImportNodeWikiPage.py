import pandas as pd
import pyodbc
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO)

def importingNodeWikiPage()->None:
    """
    creating all nodes related to WikiPage data
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
    sqlWikiPage= """
    SELECT ID as id, CREATE_DATE as created, LAST_UPDATE as last_updated, MEDIA_LABEL as title, SUMMARY as content, DOWNLOAD_CNT as views
    FROM "MOBDA_Datastore".Nodes."Uniconnect_Node_WikiPage" 
    """

    #Load Dataframes
    dfWikiPage = pd.read_sql(sqlWikiPage,cnxn)
    print (dfWikiPage)
    
    logging.info(("DataFrame finished --- %s seconds ---" % (time.time() - start_time)))

    #Data Preprocessing
    #Timestamp (2 hour behind Timezone)
    dfWikiPage['content'] = dfWikiPage['content'].fillna('NaN')
    dfWikiPage['content'] = dfWikiPage[['content']].applymap(lambda text: BeautifulSoup(text, 'html.parser').get_text())
    dfWikiPage['content'] = dfWikiPage['content'].str.replace('\n', '')
    dfWikiPage['content'] = dfWikiPage['content'].str.replace('\t', '')
    dfWikiPage['content'] = dfWikiPage['content'].str.replace('\r', '')
    dfWikiPage['content'] = dfWikiPage['content'].str.replace('\v', '')
    print (dfWikiPage)

    #Cypher Queries
    NodeWikiPage = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:WikiPage {id:row.id, title:row.title, created:row.created, last_updated:row.last_updated, content:row.content, views:row.views})
    """

    #Execute Import
    graph.execute_write_query_with_data(NodeWikiPage, dfWikiPage, "neo4j")
    ("ProcessEvent finished --- %s seconds ---" % (time.time() - start_time))

    # Close the Neo4j driver
    logging.info(("Process finished --- %s seconds ---" % (time.time() - start_time)))

#Main Method
if __name__ == "__main__":
    importingNodeWikiPage()