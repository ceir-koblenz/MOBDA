import pandas as pd
import pyodbc
import numpy
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
import logging

logging.basicConfig(level=logging.INFO)

def importingNodeAttachment(cnxn, graph) -> None:

    """
    graph as neo4j (Target DB) connector
    cnxn as dremio (Source DB) connector
    creation of Attachment Nodes
    1 SQL query
    2 Load data into dataframe
    3 preprocess data
    4 cypher query
    5 execute cypher query with data from the dataframe
    """

    start_time = time.time()

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
    #print (dfAttachmentBoardPost)
    dfAttachmentSocialProfileComment= pd.read_sql(sqlAttachmentSocialProfileComment,cnxn)
    #print (dfAttachmentSocialProfileComment)
    dfAttachmentTask = pd.read_sql(sqlAttachmentTask,cnxn)
    # print (dfAttachmentTask)
    dfAttachmentWikiPage = pd.read_sql(sqlAttachmentWikiPage,cnxn)
    #print (dfAttachmentWikiPage)

    logging.info("DataFrame finished --- %s seconds ---" % (time.time() - start_time))


    #dfCommentMicroblogPost
    dfAttachmentTask['content'] = dfAttachmentTask['content'].fillna('NaN')
    #print (dfAttachmentTask)

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

    logging.info("Process Node Attachment finished --- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
   importingNodeAttachment()