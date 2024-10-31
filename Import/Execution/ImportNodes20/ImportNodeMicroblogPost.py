import pandas as pd
import pyodbc
import numpy
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO)

def importingNodeMicroblogPost(cnxn, graph):
    """
    graph as neo4j (Target DB) connector
    cnxn as dremio (Source DB) connector
    creation of MicroblogPost Nodes
    1 SQL query
    2 Load data into dataframe
    3 preprocess data
    4 cypher query
    5 execute cypher query with data from the dataframe
    """

    start_time = time.time()

    #SQL Queries
    sqlMicroblogPost= """
    SELECT ENTRY_ID as id, CREATION_DATE as created, UPDATE_DATE as last_updated, CONTENT as content FROM "MOBDA_Datastore".Nodes."Uniconnect_Node_MicroblogPost"
    """

    #Load Dataframes
    dfMicroblogPost = pd.read_sql(sqlMicroblogPost,cnxn)
    # print (dfMicroblogPost)
    logging.info("DataFrame finished --- %s seconds ---" % (time.time() - start_time))

    #Data Preprocessing
    dfMicroblogPost['content'] = dfMicroblogPost['content'].fillna('NaN')
    dfMicroblogPost['content'] = dfMicroblogPost[['content']].applymap(lambda text: BeautifulSoup(text, 'html.parser').get_text())
    dfMicroblogPost['content'] = dfMicroblogPost['content'].str.replace('\n', '')
    dfMicroblogPost['content'] = dfMicroblogPost['content'].str.replace('\t', '')
    dfMicroblogPost['content'] = dfMicroblogPost['content'].str.replace('\r', '')
    dfMicroblogPost['content'] = dfMicroblogPost['content'].str.replace('\v', '')
    # print (dfMicroblogPost)

    #Cypher Queries
    NodeMicroblogPost = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:MicroblogPost {id:row.id, created:row.created, last_updated:row.last_updated, content:row.content})
    """

    #Execute Import
    graph.execute_write_query_with_data(NodeMicroblogPost, dfMicroblogPost, database="neo4j")
    
    logging.info("Process Node MicroblogPost finished --- %s seconds ---" % (time.time() - start_time))

#Main Method
if __name__ == "__main__":
    importingNodeMicroblogPost()