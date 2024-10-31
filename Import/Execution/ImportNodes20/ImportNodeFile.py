import pandas as pd
import time
import logging

logging.basicConfig(level=logging.INFO)

def importingNodeFile(cnxn, graph) -> None:
    """
    graph as neo4j (Target DB) connector
    cnxn as dremio (Source DB) connector
    creation of File Nodes
    1 SQL query
    2 Load data into dataframe
    3 preprocess data
    4 cypher query
    5 execute cypher query with data from the dataframe
    """
    start_time = time.time()

    #SQL Queries
    sqlFile= """
    SELECT ID as id, CREATE_DATE as created, LAST_UPDATE as last_updated, MEDIA_LABEL as title
    FROM "MOBDA_Datastore".Nodes."Uniconnect_Node_File" 
    """

    #Load Dataframes
    dfFile = pd.read_sql(sqlFile,cnxn)
    # print (dfFile)
    logging.info("DataFrame finished --- %s seconds ---" % (time.time() - start_time))

    #Data Preprocessing
    #Timestamp (2 hour behind Timezone)

    #Cypher Queries
    NodeFile = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:File {id:row.id, title:row.title, created:row.created, last_updated:row.last_updated})
    """

    #Execute Import
    graph.execute_write_query_with_data(NodeFile, dfFile, database="neo4j")

    logging.info("Process Node File finished --- %s seconds ---" % (time.time() - start_time))

#Main Method
if __name__ == "__main__":
    importingNodeFile()