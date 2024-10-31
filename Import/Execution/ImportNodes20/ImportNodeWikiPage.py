import pandas as pd
import time
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO)

def importingNodeWikiPage(cnxn, graph)-> None:
    """
    creation of WikiPage Nodes
    graph as neo4j (Target DB) connector
    cnxn as dremio (Source DB) connector
    1 SQL query
    2 Load data into dataframe
    3 preprocess data
    4 cypher query
    5 execute cypher query with data from the dataframe
    """
        
    start_time = time.time()

    #SQL Queries
    sqlWikiPage= """
    SELECT ID as id, CREATE_DATE as created, LAST_UPDATE as last_updated, MEDIA_LABEL as title, SUMMARY as content, DOWNLOAD_CNT as views
    FROM "MOBDA_Datastore".Nodes."Uniconnect_Node_WikiPage" 
    """

    #Load Dataframes
    dfWikiPage = pd.read_sql(sqlWikiPage,cnxn)
    # print (dfWikiPage)

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
    logging.info(("Process Node WikiPage finished --- %s seconds ---" % (time.time() - start_time)))

#Main method
if __name__ == "__main__":
    importingNodeWikiPage()