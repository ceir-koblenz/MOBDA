import pandas as pd
import time
import logging

logging.basicConfig(level=logging.INFO)

def importingNodeSystem(cnxn, graph)->None:

    """
    creation of System Nodes
    exists only once for the complete database
    graph as neo4j (Target DB) connector
    cnxn as dremio (Source DB) connector
    1 cypher query
    2 execute cypher query with data from the dataframe
    """

    start_time = time.time()
    
    NodeSystem = """
    CREATE (s:System {instancetitle: 'UniConnect'})
        SET
        s.softwareproduct = 'HCL Connections',
        s.softwaretype = 'ECS',
        s.softwarevendor = 'HCL Technologies',
        s.softwareversion = '6.0.0.0'
    """

    #Execute Import

    graph.execute_write_query(NodeSystem, "neo4j")
    ("ProcessEvent finished --- %s seconds ---" % (time.time() - start_time))


    logging.info(("Process Node System finished --- %s seconds ---" % (time.time() - start_time)))

#Main Method
if __name__ == "__main__":
    importingNodeSystem()