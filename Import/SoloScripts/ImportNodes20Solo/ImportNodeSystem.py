import pyodbc
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
import logging

logging.basicConfig(level=logging.INFO)

def importingNodeSystem()-> None:

    """
    creating all nodes related to System data
    1. Initiate connection to Neo4j and Dremio
    2. cypher queries
    3. execute cypher queries with data from dataframes using pyneoinstance
    """

    start_time = time.time()

    # Set up connections

    config = load_yaml_file('C:/Users/lschloemer/Nextcloud/MOBDA 2.0/VSCodeMOBDARepository/Python/a.yaml')
    db_info = config['db_infoneo']
    graph = Neo4jInstance(db_info['uri'],db_info['database'],db_info['password'])

    DSN = "Arrow Flight SQL ODBC DSN"
    cnxn = pyodbc.connect(DSN=DSN ,autocommit=True)


    NodeSystem = """
    MERGE (s:System {instancetitle: 'UniConnect'})
        SET
        s.softwareproduct = 'HCL Connections',
        s.softwaretype = 'ECS',
        s.softwarevendor = 'HCL Technologies',
        s.softwareversion = '6.0.0.0'
    """

    #Execute Import

    graph.execute_write_query(NodeSystem, "neo4j")
    ("ProcessEvent finished --- %s seconds ---" % (time.time() - start_time))


    # Close the Neo4j driver
    logging.info(("Process finished --- %s seconds ---" % (time.time() - start_time)))

#Main Method
if __name__ == "__main__":
    importingNodeSystem()