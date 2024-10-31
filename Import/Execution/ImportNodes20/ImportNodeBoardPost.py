import pandas as pd
import pyodbc
import numpy
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO)

def importingNodeBoardPost(cnxn, graph) -> None:

    """
    graph as neo4j (Target DB) connector
    cnxn as dremio (Source DB) connector
    creation of BoardPost Nodes
    1 SQL query
    2 Load data into dataframe
    3 preprocess data
    4 cypher query
    5 execute cypher query with data from the dataframe
    """
    start_time = time.time()

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


    # Close the Neo4j driver
    logging.info(("Process Node BoardPost finished --- %s seconds ---" % (time.time() - start_time)))

#Main Method
if __name__ == "__main__":
   importingNodeBoardPost()