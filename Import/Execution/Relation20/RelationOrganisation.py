import pandas as pd
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
import logging

logging.basicConfig(level=logging.INFO)

def createRelationOrganisation(cnxn, graph) -> None:

    """
    creating all relations related to Organisation
    Organisation has no database and is the same for CNX instance UniConnect
    graph as neo4j (Target DB) connector
    cnxn as dremio (Source DB) connector
    1. cypher queries
    2. execute cypher queries with pyneoinstance
    """
    start_time = time.time()


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


    # Close the Neo4j driver
    logging.info(("Process Relation Organisation finished --- %s seconds ---" % (time.time() - start_time)))

#Main method
if __name__ == "__main__":
    createRelationOrganisation()