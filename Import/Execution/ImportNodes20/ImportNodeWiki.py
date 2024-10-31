import pandas as pd
import time
import logging

logging.basicConfig(level=logging.INFO)

def importingNodeWiki(cnxn, graph)-> None:

    """
    creation of Wiki Nodes
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
    sqlWiki= """
    SELECT ID as id, TITLE as title FROM "MOBDA_Datastore".Nodes."Unniconnect_Node_Wiki"
    """

    #Load Dataframes
    dfWiki = pd.read_sql(sqlWiki,cnxn)
    print (dfWiki)
    
    logging.info(("DataFrame finished --- %s seconds ---" % (time.time() - start_time)))

    #Data Preprocessing
    #Timestamp (2 hour behind Timezone)
    #Cypher Queries

    NodeWiki = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Wiki {id:row.id, title:row.title})
    """

    #Execute Import

    graph.execute_write_query_with_data(NodeWiki, dfWiki, "neo4j")
    ("ProcessEvent finished --- %s seconds ---" % (time.time() - start_time))


    logging.info("Process Node Wiki finished --- %s seconds ---" % (time.time() - start_time))

#Main Method
if __name__ == "__main__":
    importingNodeWiki