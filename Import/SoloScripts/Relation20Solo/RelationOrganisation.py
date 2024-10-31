import pyodbc
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
import logging

logging.basicConfig(level=logging.INFO)

def createRelationOrganisation()-> None:
    """
    creating all relations related to Organisation data
    graph as neo4j (Target DB) connector
    cnxn as dremio (Source DB) connector
    1. Set up Connection
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

    #Cypher Queries
    RelationOrganisationPerson_organisation_related_to_agent = """
    MATCH (org:Organisation)
    MATCH (per:Person)
    CREATE (org)-[rorta:organisation_related_to_agent]->(per)
    CREATE (per)-[raha:agent_related_to_organisation]->(org)
    """
    RelationAccountOrganisation_account_of_agent = """
    MATCH (acc:Account)
    MATCH (org:Organisation)
    CREATE (acc)-[racis:account_of_agent {cardinality: "exactly 1"}]->(org)
    CREATE (org)-[rsca:agent_has_account]->(acc)
    """


    #Execute Import
    graph.execute_write_query(RelationAccountOrganisation_account_of_agent, "neo4j")
    graph.execute_write_query(RelationOrganisationPerson_organisation_related_to_agent, "neo4j")

    ("ProcessEvent finished --- %s seconds ---" % (time.time() - start_time))
    logging.info(("Process finished --- %s seconds ---" % (time.time() - start_time)))

#Main Method
if __name__ == "__main__":
    createRelationOrganisation()