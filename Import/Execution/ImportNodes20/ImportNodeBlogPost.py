import pandas as pd
import time
from pyneoinstance import Neo4jInstance
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO)

def importingNodeBlogPost(cnxn, graph) -> None: 

    """
    graph as neo4j (Target DB) connector
    cnxn as dremio (Source DB) connector
    creation of BlogPost Nodes
    1 SQL query
    2 Load data into dataframe
    3 preprocess data
    4 cypher query
    5 execute cypher query with data from the dataframe
    """
    start_time = time.time()

    #SQL Queries
    sqlBlogPost= """
    SELECT ID as id, PUBTIME as created, HITCOUNT as views, UPDATETIME as last_updated, TEXT as content 
    FROM "MOBDA_Datastore".Nodes."Uniconnect_Node_BlogPost" 
    """

    #Load Dataframes
    dfBlogPost = pd.read_sql(sqlBlogPost,cnxn)
    #print (dfBlogPost)

    logging.info("DataFrame finished --- %s seconds ---" % (time.time() - start_time))

    #Data Preprocessing
    dfBlogPost['content'] = dfBlogPost['content'].fillna('NaN')
    dfBlogPost['content'] = dfBlogPost[['content']].applymap(lambda text: BeautifulSoup(text, 'html.parser').get_text())
    dfBlogPost['content'] = dfBlogPost['content'].str.replace('\n', '')
    dfBlogPost['content'] = dfBlogPost['content'].str.replace('\t', '')
    dfBlogPost['content'] = dfBlogPost['content'].str.replace('\r', '')
    dfBlogPost['content'] = dfBlogPost['content'].str.replace('\v', '')
    dfBlogPost['content'] = dfBlogPost['content'].str.replace(';', ',')
    #print (dfBlogPost)
   
    #Cypher Query
    NodeBlogPost = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:BlogPost {id:row.id, created:row.created, last_updated:row.last_updated, content:row.content, views:row.views})
    """

    #Execute Import
    graph.execute_write_query_with_data(NodeBlogPost, dfBlogPost, database="neo4j")

    logging.info("Process Node BlogPost finished --- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
   importingNodeBlogPost()