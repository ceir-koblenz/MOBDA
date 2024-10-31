import pandas as pd
import time
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO)

def importingNodeTask(cnxn, graph)->None:
    """
    creation of Task Nodes
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
    logging.info(("Process Node Task finished --- %s seconds ---" % (time.time() - start_time)))

#Main Method
if __name__ == "__main__":
    importingNodeTask()