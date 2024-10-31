import pyodbc
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
import logging

logging.basicConfig(level=logging.INFO)

def importingNodeOrganisation() -> None:
    """
    creating all nodes related to Organisation data
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

    #Cypher Query
    NodeOrganisation = """
    MERGE (o:Organisation {ID: 1})
    SET
        o.title = 'Universität Koblenz-Landau',
        o.phone = '0261 2871667',
        o.email =  'asta.uni-koblenz.de'
    """

    #Execute Import
    graph.execute_write_query(NodeOrganisation, "neo4j")
    ("ProcessEvent finished --- %s seconds ---" % (time.time() - start_time))

    # Close the Neo4j driver
    logging.info(("Process finished --- %s seconds ---" % (time.time() - start_time)))

#Main Method
if __name__ == "__main__":
    importingNodeOrganisation()