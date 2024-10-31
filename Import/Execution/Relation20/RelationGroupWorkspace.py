import pandas as pd
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
import logging

logging.basicConfig(level=logging.INFO)

def createRelationGroupWorkspaces(cnxn, graph) -> None:
    start_time = time.time()

    
    """
    creating all relations related to Groupworkspace data
    graph as neo4j (Target DB) connector
    cnxn as dremio (Source DB) connector
    1. SQL queries
    2. read data from dremio in dataframe
    3. cypher queries
    4. execute cypher queries with data from dataframes using pyneoinstance
    """

    #SQL Queries
    sqlRelationGroupWorkspaceMessageBoard_space_contains_container= """ 
    SELECT workspaceid, mboardid
    FROM "MOBDA_Datastore".Relations.GroupWorkspaces."Uniconnect_Relation_GroupWorkspaces_MessageBoard_space_contains_container"
    """

    sqlRelationGroupWorkspaceMicroblog_space_contains_container= """
    SELECT workspaceid, mblogid
    FROM "MOBDA_Datastore".Relations.GroupWorkspaces."Uniconnect_Relation_GroupWorkspaces_Microblog_space_contains_container"
    """
    
    sqlRelationGroupWorkspaceWeblog_space_contains_container= """
    SELECT workspaceid, weblogid
    FROM MOBDA_Datastore.Relations.GroupWorkspaces.Uniconnect_Relations_GroupWorkspaces_Weblog_space_contains_container
     """

    sqlRelationGroupWorkspaceWiki_space_contains_container= """
    SELECT workspaceid, wikiid
    FROM MOBDA_Datastore.Relations.GroupWorkspaces.Uniconnect_Relation_GroupWorkspaces_Wiki_space_contains_container
    """

    sqlRelationGroupWorkspaceFileLibrary_space_contains_container= """
    SELECT workspaceid, libid
    FROM MOBDA_Datastore.Relations.GroupWorkspaces.Uniconnect_Relation_GroupWorkspace_Filelibrary_space_contains_container
    """

    sqlRelationGroupWorkspaceTaskContainer_space_contains_container= """
    SELECT workspaceid, tcontainerid
    FROM MOBDA_Datastore.Relations.GroupWorkspaces.Uniconnect_Relation_GroupWorkspaces_TaskContainer_space_contains_container
    """
    
    #Load Dataframes
    dfRelationGroupWorkspaceMessageboard_space_contains_container = pd.read_sql(sqlRelationGroupWorkspaceMessageBoard_space_contains_container,cnxn)
    print (dfRelationGroupWorkspaceMessageboard_space_contains_container)
    dfRelationGroupWorkspaceMicroblog_space_contains_container = pd.read_sql(sqlRelationGroupWorkspaceMicroblog_space_contains_container,cnxn)
    print (dfRelationGroupWorkspaceMicroblog_space_contains_container)
    dfRelationGroupWorkspaceWeblog_space_contains_container = pd.read_sql(sqlRelationGroupWorkspaceWeblog_space_contains_container,cnxn)
    print (dfRelationGroupWorkspaceWeblog_space_contains_container)
    dfRelationGroupWorkspaceWiki_space_contains_container = pd.read_sql(sqlRelationGroupWorkspaceWiki_space_contains_container,cnxn)
    print (dfRelationGroupWorkspaceWiki_space_contains_container)
    dfRelationGroupWorkspaceFileLibrary_space_contains_container = pd.read_sql(sqlRelationGroupWorkspaceFileLibrary_space_contains_container,cnxn)
    print (dfRelationGroupWorkspaceFileLibrary_space_contains_container)
    dfRelationGroupWorkspaceTaskContainer_space_contains_container = pd.read_sql(sqlRelationGroupWorkspaceTaskContainer_space_contains_container,cnxn)
    print (dfRelationGroupWorkspaceTaskContainer_space_contains_container)
    
    
    logging.info(("DataFrame finished --- %s seconds ---" % (time.time() - start_time)))

    #Cypher Queries

    RelationGroupWorkspaceMessageBoard_space_contains_container = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (gws:GroupWorkspace{id:row.workspaceid})
    MATCH (mb:MessageBoard{id:row.mboardid})
    CREATE (gws)-[riehc:space_contains_container]->(mb)
    CREATE (mb)-[rcoie:container_contained_in_space {cardinality: "exactly 1"}]->(gws)
    """

    RelationGroupWorkspaceMicroblog_space_contains_container = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (gws:GroupWorkspace{id:row.workspaceid})
    MATCH (mb:Microblog{id:row.mblogid})
    CREATE (gws)-[riehc:space_contains_container]->(mb)
    CREATE (mb)-[rcoie:container_contained_in_space {cardinality: "exactly 1"}]->(gws)
    """

    RelationGroupWorkspaceWeblog_space_contains_container = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (gws:GroupWorkspace{id:row.workspaceid})
    MATCH (wb:Weblog{id:row.weblogid})
    CREATE (gws)-[riehc:space_contains_container]->(wb)
    CREATE (wb)-[rcoie:container_contained_in_space {cardinality: "exactly 1"}]->(gws)
    """

    RelationGroupWorkspaceWiki_space_contains_container = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (gws:GroupWorkspace{id:row.workspaceid})
    MATCH (wi:Wiki{id:row.wikiid})
    CREATE (gws)-[riehc:space_contains_container]->(wi)
    CREATE (wi)-[rcoie:container_contained_in_space {cardinality: "exactly 1"}]->(gws)
    """

    RelationGroupWorkspaceFileLibrary_space_contains_container = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (gws:GroupWorkspace{id:row.workspaceid})
    MATCH (li:FileLibrary{id:row.libid})
    CREATE (gws)-[riehc:space_contains_container]->(li)
    CREATE (li)-[rcoie:container_contained_in_space {cardinality: "exactly 1"}]->(gws)
    """

    RelationGroupWorkspaceTaskContainer_space_contains_container = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (gws:GroupWorkspace{id:row.workspaceid})
    MATCH (tc:TaskContainer{id:row.tcontainerid})
    CREATE (gws)-[riehc:space_contains_container]->(tc)
    CREATE (tc)-[rcoie:container_contained_in_space {cardinality: "exactly 1"}]->(gws)
    """

    #Execute Import
    graph.execute_write_query_with_data(RelationGroupWorkspaceMessageBoard_space_contains_container, dfRelationGroupWorkspaceMessageboard_space_contains_container, "neo4j", partitions = 12, parallel=True, workers = 12)
    graph.execute_write_query_with_data(RelationGroupWorkspaceMicroblog_space_contains_container, dfRelationGroupWorkspaceMicroblog_space_contains_container, "neo4j", partitions = 12, parallel=True, workers = 12)
    graph.execute_write_query_with_data(RelationGroupWorkspaceWeblog_space_contains_container, dfRelationGroupWorkspaceWeblog_space_contains_container, "neo4j", partitions = 12, parallel=True, workers = 12)
    graph.execute_write_query_with_data(RelationGroupWorkspaceWiki_space_contains_container, dfRelationGroupWorkspaceWiki_space_contains_container, "neo4j", partitions = 12, parallel=True, workers = 12)
    graph.execute_write_query_with_data(RelationGroupWorkspaceFileLibrary_space_contains_container, dfRelationGroupWorkspaceFileLibrary_space_contains_container, "neo4j", partitions = 12, parallel=True, workers = 12)
    graph.execute_write_query_with_data(RelationGroupWorkspaceTaskContainer_space_contains_container, dfRelationGroupWorkspaceTaskContainer_space_contains_container, "neo4j", partitions = 12, parallel=True, workers = 12)

    ("ProcessEvent finished --- %s seconds ---" % (time.time() - start_time))

    # Close the Neo4j driver
    logging.info(("Process Relation GroupWorkspace finished --- %s seconds ---" % (time.time() - start_time)))

# Main method
if __name__ == "__main__":
    createRelationGroupWorkspaces()