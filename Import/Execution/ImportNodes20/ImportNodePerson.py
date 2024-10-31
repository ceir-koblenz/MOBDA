import pandas as pd
import time
import logging 

logging.basicConfig(level=logging.INFO)

def importingNodePerson(cnxn, graph):

    """
    creation of Person Nodes
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
    sqlPerson= """
    SELECT PROF_GUID as id ,PROF_MAIL_LOWER as email, PROF_SURNAME as family_name, PROF_GIVEN_NAME as given_name, PROF_TELEPHONE_NUMBER as phone
    FROM "MOBDA_Datastore".Nodes."Uniconnect_Node_Person"
    """

    #Load Dataframes
    dfPerson = pd.read_sql(sqlPerson,cnxn)
    print (dfPerson)
    
    logging.info(("DataFrame finished --- %s seconds ---" % (time.time() - start_time)))

    #Data Preprocessing

    #Cypher Queries

    NodePerson = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Person {id:row.id, email:row.email, family_name:row.family_name, given_name:row.given_name, phone:row.phone})
    """

    #Execute Import

    graph.execute_write_query_with_data(NodePerson, dfPerson, "neo4j")
    ("ProcessEvent finished --- %s seconds ---" % (time.time() - start_time))


    # Close the Neo4j driver
    logging.info(("Process Node Person finished --- %s seconds ---" % (time.time() - start_time)))
#Main method
if __name__ == "__main__":
    importingNodePerson()