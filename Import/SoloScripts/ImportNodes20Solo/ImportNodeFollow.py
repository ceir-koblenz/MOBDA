import pandas as pd
import pyodbc
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
import logging

logging.basicConfig(level=logging.INFO)

def importingNodeFollow()-> None:
    """
    creating all nodes related to Follow data
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
    sqlFollowBoardPost= """
    SELECT UUID as id, CREATED as created, 'BoardPostFollow' as intellectualentity FROM "MOBDA_Datastore".Nodes.Follow."Uniconnect_Node_Follow_BoardPost" 
    """

    sqlFollowFile= """
    SELECT FOLLOW_ID as id, CREATE_DATE as created, 'FileFollow' as intellectualentity
    FROM "MOBDA_Datastore".Nodes.Follow."Uniconnect_Node_Follow_File" 
    """

    sqlFollowFolder= """
    SELECT FOLLOW_ID as id, CREATE_DATE as created, 'FolderFollow' as intellectualentity FROM "MOBDA_Datastore".Nodes.Follow."Uniconnect_Node_Follow_Folder"
    """

    sqlFollowSocialProfile= """
    SELECT COMM_FOLLOW_ID as id, 'SocialProfileFollow' as intellectualentity FROM "MOBDA_Datastore".Nodes.Follow."Uniconnect_Node_Follow_SocialProfile" 
    """

    sqlFollowTask= """
    SELECT NMEMBERUUID as id, CREATED as created, 'TaskFollow' as intellectualentity
    FROM "MOBDA_Datastore".Nodes.Follow."Uniconnect_Node_Follow_Task"
    """

    sqlFollowWikiPage= """
    SELECT FOLLOW_ID as id, CREATE_DATE as created, 'WikiPageFollow' as intellectualentity
    FROM "MOBDA_Datastore".Nodes.Follow."Uniconnect_Node_Follow_WikiPage"
    """

    #Load Dataframes
    dfFollowBoardPost = pd.read_sql(sqlFollowBoardPost,cnxn)
    print (dfFollowBoardPost)
    dfFollowFile = pd.read_sql(sqlFollowFile,cnxn)
    print (dfFollowFile)
    dfFollowFolder = pd.read_sql(sqlFollowFolder,cnxn)
    print (dfFollowFolder)
    dfFollowSocialProfile = pd.read_sql(sqlFollowSocialProfile,cnxn)
    print (dfFollowSocialProfile)
    dfFollowTask = pd.read_sql(sqlFollowTask,cnxn)
    print (dfFollowTask)
    dfFollowWikiPage = pd.read_sql(sqlFollowWikiPage,cnxn)
    print (dfFollowWikiPage)
    
    logging.info(("DataFrame finished --- %s seconds ---" % (time.time() - start_time)))

    #Data Preprocessing

    #Cypher Queries

    NodeFollowBoardPost = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Follow {id:row.id, created:row.created, intellectual_entity:row.intellectualentity})
    """

    NodeFollowFile = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Follow {id:row.id, created:row.created, intellectual_entity:row.intellectualentity})
    """

    NodeFollowFolder = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Follow {id:row.id, created:row.created, intellectual_entity:row.intellectualentity})
    """

    NodeFollowSocialProfile = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Follow {id:row.id, intellectual_entity:row.intellectualentity})
    """

    NodeFollowTask = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Follow {id:row.id, created:row.created, intellectual_entity:row.intellectualentity})
    """

    NodeFollowWikiPage = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Follow {id:row.id, created:row.created, intellectual_entity:row.intellectualentity})
    """

    #Execute Import

    graph.execute_write_query_with_data(NodeFollowBoardPost, dfFollowBoardPost, database="neo4j")

    graph.execute_write_query_with_data(NodeFollowFile, dfFollowFile, database="neo4j")

    graph.execute_write_query_with_data(NodeFollowFolder, dfFollowFolder, database="neo4j")

    graph.execute_write_query_with_data(NodeFollowSocialProfile, dfFollowSocialProfile, database="neo4j")

    graph.execute_write_query_with_data(NodeFollowTask, dfFollowTask, database="neo4j")

    graph.execute_write_query_with_data(NodeFollowWikiPage, dfFollowWikiPage, database="neo4j")

    ("ProcessEvent finished --- %s seconds ---" % (time.time() - start_time))

    logging.info(("Process finished --- %s seconds ---" % (time.time() - start_time)))

#Main method
if __name__ == "__main__":
    importingNodeFollow()