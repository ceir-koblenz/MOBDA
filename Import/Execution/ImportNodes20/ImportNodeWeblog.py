import pandas as pd
import time
import logging

logging.basicConfig(level=logging.INFO)

def importingNodeWeblog(cnxn, graph)->None:
    
    """
    creation of Weblog Nodes
    graph as neo4j (Target DB) connector
    cnxn as dremio (Source DB) connector
    1 SQL query
    2 Load data into dataframe
    3 preprocess data
    4 cypher query
    5 execute cypher query with data from the dataframe
    """

    start_time = time.time()

    #Cypher Queries

    #SQL Queries
    sqlWeblog = """
    SELECT ID as id, NAME as title FROM "MOBDA_Datastore".Nodes."Uniconnect_Node_Weblog" 
    """

    #Load Dataframes
    dfWeblog= pd.read_sql(sqlWeblog,cnxn)
    print (dfWeblog)


    logging.info(("DataFrame finished --- %s seconds ---" % (time.time() - start_time)))

    #Data Preprocessing

    #Cypher Queries

    NodeWeblog = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Weblog {id:row.id, title:row.title})
    """
    #Execute Import
    graph.execute_write_query_with_data(NodeWeblog, dfWeblog, "neo4j")
    ("ProcessEvent finished --- %s seconds ---" % (time.time() - start_time))

    logging.info(("Process Node Weblog finished --- %s seconds ---" % (time.time() - start_time)))

#Main method
if __name__ =="__main__":
    importingNodeWeblog()