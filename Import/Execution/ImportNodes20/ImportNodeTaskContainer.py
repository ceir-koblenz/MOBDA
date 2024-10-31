import pandas as pd
import time
import logging

logging.basicConfig(level=logging.INFO)

def importingNodeTaskConatiner(cnxn, graph)-> None:
    """
    creation of TaskContainer Nodes
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
    sqlTaskContainer= """
    SELECT ACTIVITYUUID as id
    FROM "MOBDA_Datastore".Nodes."Uniconnect_Node_TaskContainer"
    """

    #Load Dataframes
    dfTaskContainer = pd.read_sql(sqlTaskContainer,cnxn)
    print (dfTaskContainer)
   
    logging.info(("DataFrame finished --- %s seconds ---" % (time.time() - start_time)))

    #Data Preprocessing

    #Cypher Queries

    NodeTaskContainer = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:TaskContainer {id:row.id})
    """

    #Execute Import

    graph.execute_write_query_with_data(NodeTaskContainer, dfTaskContainer, "neo4j")
    ("ProcessEvent finished --- %s seconds ---" % (time.time() - start_time))

    logging.info(("Process TaskContainer Node finished --- %s seconds ---" % (time.time() - start_time)))

#Main Method
if __name__ == "__main__":
    importingNodeTaskConatiner()