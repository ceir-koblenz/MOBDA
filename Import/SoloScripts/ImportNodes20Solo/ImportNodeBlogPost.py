import pandas as pd
import pyodbc
import numpy
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
from bs4 import BeautifulSoup
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)

def importingNodeBlogPost()-> None: 
    """
    creating all nodes related to BlogPost data
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
    sqlBlogPost= """
    SELECT ID as id, PUBTIME as created, HITCOUNT as views, UPDATETIME as last_updated, TEXT as content 
    FROM "MOBDA_Datastore".Nodes."Uniconnect_Node_BlogPost" 
    """

    #Load Dataframes
    dfBlogPost = pd.read_sql(sqlBlogPost,cnxn)
    #print (dfBlogPost)
   

    print("DataFrame finished --- %s seconds ---" % (time.time() - start_time))

    #Data Preprocessing
    dfBlogPost['content'] = dfBlogPost['content'].fillna('NaN')
    dfBlogPost['content'] = dfBlogPost[['content']].applymap(lambda text: BeautifulSoup(text, 'html.parser').get_text())
    dfBlogPost['content'] = dfBlogPost['content'].str.replace('\n', '')
    dfBlogPost['content'] = dfBlogPost['content'].str.replace('\t', '')
    dfBlogPost['content'] = dfBlogPost['content'].str.replace('\r', '')
    dfBlogPost['content'] = dfBlogPost['content'].str.replace('\v', '')
    dfBlogPost['content'] = dfBlogPost['content'].str.replace(';', ',')
    #print (dfBlogPost)
    
    #Cypher Queries

    NodeBlogPost = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:BlogPost {id:row.id, created:row.created, last_updated:row.last_updated, content:row.content, views:row.views})
    """

    #Execute Import
    graph.execute_write_query_with_data(NodeBlogPost, dfBlogPost, database="neo4j")

    ("ProcessEvent finished --- %s seconds ---" % (time.time() - start_time))


    # Close the Neo4j driver
    logging.info(("Process finished --- %s seconds ---" % (time.time() - start_time)))
# Main Method
if __name__ == "__main__":
   importingNodeBlogPost()