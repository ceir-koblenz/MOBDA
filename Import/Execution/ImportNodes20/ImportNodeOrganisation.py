import pandas as pd
import pyodbc
import numpy
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO)

def importingNodeOrganisation(graph):
    """
    graph as neo4j (Target DB) connector
    cnxn as dremio (Source DB) connector
    creation of Organisation Nodes
    1 SQL query
    2 Load data into dataframe
    3 preprocess data
    4 cypher query
    5 execute cypher query with data from the dataframe
    """
    start_time = time.time()


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
    logging.info(("Process Node Organisation finished --- %s seconds ---" % (time.time() - start_time)))

#Main Method
if __name__ == "__main__":
    importingNodeOrganisation()