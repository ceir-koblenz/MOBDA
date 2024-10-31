import pandas as pd
import pyodbc
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
import logging

# Set up connections
logging.basicConfig(level=logging.INFO)

def importingNodeAccount()-> None:

    """
    creating all nodes related to Account data
    1. Initiate connection to Neo4j and Dremio
    2. SQL queries
    3. read data from dremio in dataframe
    4. cypher queries
    5. execute cypher queries with data from dataframes using pyneoinstance
    """
    
    config = load_yaml_file('C:/Users/lschloemer/Nextcloud/MOBDA 2.0/VSCodeMOBDARepository/Python/a.yaml')
    db_info = config['db_infoneo']
    logging.info(db_info['uri'])
    graph = Neo4jInstance(db_info['uri'],db_info['database'],db_info['password'])
    DSN = "Arrow Flight SQL ODBC DSN"

    cnxn = pyodbc.connect(DSN=DSN ,autocommit=True)

    start_time = time.time()

    #SQL Queries
    sqlAccount= """
    SELECT PROF_GUID as id, PROF_MAIL_LOWER as email, PROF_UID as private_name, PROF_DISPLAY_NAME as public_name 
    FROM "MOBDA_Datastore".Nodes."Uniconnect_Node_Account" 
    """

    #Load Dataframes
    dfAccount = pd.read_sql(sqlAccount,cnxn)

    logging.info((dfAccount))

    logging.info("DataFrame finished --- %s seconds ---" % (time.time() - start_time))

    #Data Preprocessing

    #Cypher Queries

    NodeAccount = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Account {id:row.id, email:row.email, private_name:row.private_name, public_name:row.public_name})
    """

    #Execute Import
    graph.execute_write_query_with_data(NodeAccount, dfAccount, database="neo4j")

    logging.info("Process finished --- %s seconds ---" % (time.time() - start_time))

#Main Method
if __name__ == "__main__":
   importingNodeAccount()