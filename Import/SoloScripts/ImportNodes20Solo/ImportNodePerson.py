import pandas as pd
import pyodbc
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
import logging 

logging.basicConfig(level=logging.INFO)

def importingNodePerson()-> None:
    """
    creating all nodes related to Person data
    1. Initiate connection to Neo4j and Dremio
    2. SQL queries
    3. read data from dremio in dataframe
    4. cypher queries
    5. execute cypher queries with data from dataframes using pyneoinstance
    """

    start_time = time.time()

    # Set up connections

    config = load_yaml_file('C:/Users/lschloemer/Nextcloud/MOBDA 2.0/VSCodeMOBDARepository/Python/a.yaml')
    db_info = config['db_infoneo']
    graph = Neo4jInstance(db_info['uri'],db_info['database'],db_info['password'])
    DSN = "Arrow Flight SQL ODBC DSN"
    cnxn = pyodbc.connect(DSN=DSN ,autocommit=True)

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

    logging.info(("Process finished --- %s seconds ---" % (time.time() - start_time)))

#Main Method
if __name__ == "__main__":
    importingNodePerson()