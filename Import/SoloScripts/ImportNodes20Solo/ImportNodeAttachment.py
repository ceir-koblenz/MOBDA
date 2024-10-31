import pandas as pd
import pyodbc
import numpy
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO)

def importingNodeAttachment()-> None:

    """
    creating all nodes related to Attachment data
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
    logging.info((db_info['uri']))
    graph = Neo4jInstance(db_info['uri'],db_info['database'],db_info['password'])

    DSN = "Arrow Flight SQL ODBC DSN"
    cnxn = pyodbc.connect(DSN=DSN ,autocommit=True)

    #SQL Queries
    sqlAttachmentBoardPost= """
    SELECT NODEUUID as id, FIELDNAME as title, CREATED as created, LASTMOD as last_updated, 'BoardPostAttachment' as intellectualentity
    FROM "MOBDA_Datastore".Nodes.Attachment."Uniconnect_Node_Attachment_BoardPost"
    """

    sqlAttachmentSocialProfileComment= """
    SELECT OBJECT_ID as id, CREATION_DATE as created, DISPLAY_NAME as title, 'SocialProfileCommentAttachment' as intellectualentity
    FROM "MOBDA_Datastore".Nodes.Attachment."Uniconnect_Node_Attachment_SocialProfile_Comment"
    """

    sqlAttachmentTask= """
    SELECT NODEUUID as id, NAME as title, DESCRIPTION as content, LASTMOD as last_updated, CREATED as created, 'TaskAttachment' as intellectualentity
    FROM "MOBDA_Datastore".Nodes.Attachment."Uniconnect_Node_Attachment_Task"
    """

    sqlAttachmentWikiPage= """
    SELECT ID as id, TITLE as title, CREATE_DATE as created, LAST_UPDATE as last_updated, 'WikiPageAttachment' as intellectualentity 
    FROM "MOBDA_Datastore".Nodes.Attachment."Uniconnect_Node_Attachment_WikiPage" 
    """

    #Load Dataframes
    dfAttachmentBoardPost = pd.read_sql(sqlAttachmentBoardPost,cnxn)
    print (dfAttachmentBoardPost)
    dfAttachmentSocialProfileComment= pd.read_sql(sqlAttachmentSocialProfileComment,cnxn)
    print (dfAttachmentSocialProfileComment)
    dfAttachmentTask = pd.read_sql(sqlAttachmentTask,cnxn)
    print (dfAttachmentTask)
    dfAttachmentWikiPage = pd.read_sql(sqlAttachmentWikiPage,cnxn)
    print (dfAttachmentWikiPage)

    logging.info(("DataFrame finished --- %s seconds ---" % (time.time() - start_time)))

    #Data Preprocessing

    #Cypher Queries

    NodeAttachmentBoardPost = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Attachment {id:row.id, title:row.title, created:row.created, last_updated:row.last_updated, intellectual_entity:row.intellectualentity})
    """

    NodeAttachmentSocialProfileComment = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Attachment {id:row.id, title:row.title, created:row.created, intellectual_entity:row.intellectualentity})
    """

    NodeAttachmentTask = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Attachment {id:row.id, title:row.title, created:row.created, last_updated:row.last_updated, content:row.content, intellectual_entity:row.intellectualentity})
    """

    NodeAttachmentWikiPage = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Attachment {id:row.id, title:row.title, created:row.created, last_updated:row.last_updated, intellectual_entity:row.intellectualentity})
    """


    #Execute Import

    graph.execute_write_query_with_data(NodeAttachmentBoardPost, dfAttachmentBoardPost, database="neo4j")

    graph.execute_write_query_with_data(NodeAttachmentSocialProfileComment, dfAttachmentSocialProfileComment, database="neo4j")

    graph.execute_write_query_with_data(NodeAttachmentTask, dfAttachmentTask, database="neo4j")

    graph.execute_write_query_with_data(NodeAttachmentWikiPage, dfAttachmentWikiPage, database="neo4j")

    ("ProcessEvent finished --- %s seconds ---" % (time.time() - start_time))


    # Close the Neo4j driver
    logging.info(("Process finished --- %s seconds ---" % (time.time() - start_time)))
    
#Main method
if __name__ == "__main__":
   importingNodeAttachment()