import pandas as pd
import time
import logging

logging.basicConfig(level=logging.INFO)

def importingNodeAccount(cnxn, graph) -> None:

    """
    graph as neo4j (Target DB) connector
    cnxn as dremio (Source DB) connector
    creation of Account Nodes
    1 SQL query
    2 Load data into dataframe
    3 preprocess data
    4 cypher query
    5 execute cypher query with data from the dataframe
    """

    start_time = time.time()

    #SQL Queries
    sqlAccount= """
    SELECT PROF_GUID as id, PROF_MAIL_LOWER as email, PROF_UID as private_name, PROF_DISPLAY_NAME as public_name 
    FROM "MOBDA_Datastore".Nodes."Uniconnect_Node_Account" 
    """

    #Load Dataframes
    dfAccount = pd.read_sql(sqlAccount,cnxn)
    # print (dfAccount)
    logging.info("DataFrame finished --- %s seconds ---" % (time.time() - start_time))

    #Data Preprocessing
    # not needed

    #Cypher Queries
    NodeAccount = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Account {id:row.id, email:row.email, private_name:row.private_name, public_name:row.public_name})
    """

    #Execute Import
    graph.execute_write_query_with_data(NodeAccount, dfAccount, database="neo4j")


    # Close the Neo4j driver
    logging.info("Process Node Account finished --- %s seconds ---" % (time.time() - start_time))
    
if __name__ == "__main__":
   importingNodeAccount()