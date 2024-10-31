import pandas as pd
import pyodbc
import numpy
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO)

def importingNodeComment()-> None:

    """
    creating all nodes related to Comment data
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
    sqlCommentBlogPost= """
    SELECT ID as id, NAME as title, POSTTIME as created, LASTUPDATED as last_updated, CONTENT as content, 'BlogPostComment' as intellectualentity FROM "MOBDA_Datastore".Nodes.Comment."Uniconnect_Node_Comment_BlogPost" 
    """

    sqlCommentBoardPost= """
    SELECT NODEUUID as id, CREATED as created, LASTMOD as last_updated, NAME as title, DESCRIPTION as content, 'BoardPostComment' as intellectualentity FROM "MOBDA_Datastore".Nodes.Comment."Uniconnect_Node_Comment_BoardPost" 
    """

    sqlCommentFile= """
    SELECT ID as id, COMMENT as content, CREATE_DATE as created, LAST_UPDATE last_updated, TITLE as title, 'FileComment' as intellectualentity FROM "MOBDA_Datastore".Nodes.Comment."Uniconnect_Node_Comment_File" 
    """

    sqlCommentMicroblogPost= """
    SELECT COMMENT_ID as id, CONTENT as content, CREATION_DATE as created, UPDATE_DATE as last_updated, 'MicroblogPostComment' as intellectualentity
    FROM "MOBDA_Datastore".Nodes.Comment."Uniconnect_Node_Comment_MicroblogPost" 
    """

    sqlCommentSocialProfile= """
    SELECT ENTRY_ID as id, CREATION_DATE as created, UPDATE_DATE as last_updated, CONTENT as content, 'SocialProfileComment' as intellectualentity
    FROM "MOBDA_Datastore".Nodes.Comment."Uniconnect_Node_Comment_SocialProfile" 
    """

    sqlCommentTask= """
    SELECT NODEUUID as id, NAME as title, CREATED as created, LASTMOD as last_updated, DESCRIPTION as content, 'TaskComment' as intellectualentity
    FROM "MOBDA_Datastore".Nodes.Comment."Uniconnect_Node_Comment_Task" 
    """

    sqlCommentWikiPage= """
    SELECT ID as id, COMMENT as content, CREATE_DATE as created, LAST_UPDATE as last_updated, TITLE as title, 'WikiPageComment' as intellectualentity
    FROM MOBDA_Datastore.Nodes.Comment.Uniconnect_Node_Comment_WikiPage
    """

    #Load Dataframes
    dfCommentBlogPost = pd.read_sql(sqlCommentBlogPost,cnxn)
    print (dfCommentBlogPost)
    dfCommentBoardPost = pd.read_sql(sqlCommentBoardPost,cnxn)
    print (dfCommentBoardPost)
    dfCommentFile = pd.read_sql(sqlCommentFile,cnxn)
    print (dfCommentFile)
    dfCommentMicroblogPost = pd.read_sql(sqlCommentMicroblogPost,cnxn)
    print (dfCommentMicroblogPost)
    dfCommentSocialProfile = pd.read_sql(sqlCommentSocialProfile,cnxn)
    print (dfCommentSocialProfile)
    dfCommentTask = pd.read_sql(sqlCommentTask,cnxn)
    print (dfCommentTask)
    dfCommentWikiPage = pd.read_sql(sqlCommentWikiPage,cnxn)
    print (dfCommentWikiPage)
    
    logging.info(("DataFrame finished --- %s seconds ---" % (time.time() - start_time)))

    #Data Preprocessing

    #CommentBlogPost
    dfCommentBlogPost['content'] = dfCommentBlogPost['content'].fillna('NaN')
    dfCommentBlogPost['content'] = dfCommentBlogPost[['content']].applymap(lambda text: BeautifulSoup(text, 'html.parser').get_text())
    dfCommentBlogPost['content'] = dfCommentBlogPost['content'].str.replace('\n', '')
    dfCommentBlogPost['content'] = dfCommentBlogPost['content'].str.replace('\t', '')
    dfCommentBlogPost['content'] = dfCommentBlogPost['content'].str.replace('\r', '')
    dfCommentBlogPost['content'] = dfCommentBlogPost['content'].str.replace('\v', '')
    print (dfCommentBlogPost)

    #CommmentBoardPost
    dfCommentBoardPost['content'] = dfCommentBoardPost['content'].fillna('NaN')
    dfCommentBoardPost['content'] = dfCommentBoardPost[['content']].applymap(lambda text: BeautifulSoup(text, 'html.parser').get_text())
    dfCommentBoardPost['content'] = dfCommentBoardPost['content'].str.replace('\n', '')
    dfCommentBoardPost['content'] = dfCommentBoardPost['content'].str.replace('\t', '')
    dfCommentBoardPost['content'] = dfCommentBoardPost['content'].str.replace('\r', '')
    dfCommentBoardPost['content'] = dfCommentBoardPost['content'].str.replace('\v', '')
    print (dfCommentBoardPost)

    #CommentFile
    dfCommentFile['content'] = dfCommentFile['content'].fillna('NaN')
    dfCommentFile['content'] = dfCommentFile[['content']].applymap(lambda text: BeautifulSoup(text, 'html.parser').get_text())
    dfCommentFile['content'] = dfCommentFile['content'].str.replace('\n', '')
    dfCommentFile['content'] = dfCommentFile['content'].str.replace('\t', '')
    dfCommentFile['content'] = dfCommentFile['content'].str.replace('\r', '')
    dfCommentFile['content'] = dfCommentFile['content'].str.replace('\v', '')
    print (dfCommentFile)

    #dfCommentMicroblogPost
    dfCommentMicroblogPost['content'] = dfCommentMicroblogPost['content'].fillna('NaN')
    dfCommentMicroblogPost['content'] = dfCommentMicroblogPost[['content']].applymap(lambda text: BeautifulSoup(text, 'html.parser').get_text())
    dfCommentMicroblogPost['content'] = dfCommentMicroblogPost['content'].str.replace('\n', '')
    dfCommentMicroblogPost['content'] = dfCommentMicroblogPost['content'].str.replace('\t', '')
    dfCommentMicroblogPost['content'] = dfCommentMicroblogPost['content'].str.replace('\r', '')
    dfCommentMicroblogPost['content'] = dfCommentMicroblogPost['content'].str.replace('\v', '')
    print (dfCommentMicroblogPost)

    #dfCommentSocialProfile
    dfCommentSocialProfile['content'] = dfCommentSocialProfile['content'].fillna('NaN')
    dfCommentSocialProfile['content'] = dfCommentSocialProfile[['content']].applymap(lambda text: BeautifulSoup(text, 'html.parser').get_text())
    dfCommentSocialProfile['content'] = dfCommentSocialProfile['content'].str.replace('\n', '')
    dfCommentSocialProfile['content'] = dfCommentSocialProfile['content'].str.replace('\t', '')
    dfCommentSocialProfile['content'] = dfCommentSocialProfile['content'].str.replace('\r', '')
    dfCommentSocialProfile['content'] = dfCommentSocialProfile['content'].str.replace('\v', '')
    print (dfCommentSocialProfile)

    #dfCommentTask
    dfCommentTask['content'] = dfCommentTask['content'].fillna('NaN')
    dfCommentTask['content'] = dfCommentTask[['content']].applymap(lambda text: BeautifulSoup(text, 'html.parser').get_text())
    dfCommentTask['content'] = dfCommentTask['content'].str.replace('\n', '')
    dfCommentTask['content'] = dfCommentTask['content'].str.replace('\t', '')
    dfCommentTask['content'] = dfCommentTask['content'].str.replace('\r', '')
    dfCommentTask['content'] = dfCommentTask['content'].str.replace('\v', '')
    print (dfCommentTask)

    #dfCommentWikiPage
    dfCommentWikiPage['content'] = dfCommentWikiPage['content'].fillna('NaN')
    dfCommentWikiPage['content'] = dfCommentWikiPage[['content']].applymap(lambda text: BeautifulSoup(text, 'html.parser').get_text())
    dfCommentWikiPage['content'] = dfCommentWikiPage['content'].str.replace('\n', '')
    dfCommentWikiPage['content'] = dfCommentWikiPage['content'].str.replace('\t', '')
    dfCommentWikiPage['content'] = dfCommentWikiPage['content'].str.replace('\r', '')
    dfCommentWikiPage['content'] = dfCommentWikiPage['content'].str.replace('\v', '')
    print (dfCommentWikiPage)

    #Cypher Queries

    NodeCommentBlogPost = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Comment {id:row.id, title:row.title, created:row.created, last_updated:row.last_updated, content:row.content, intellectual_entity:row.intellectualentity})
    """

    NodeCommentBoardPost = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Comment {id:row.id, title:row.title, created:row.created, last_updated:row.last_updated, content:row.content, intellectual_entity:row.intellectualentity})
    """

    NodeCommentFile = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Comment {id:row.id, title:row.title, created:row.created, last_updated:row.last_updated, content:row.content, intellectual_entity:row.intellectualentity})
    """

    NodeCommentMicroblogPost = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Comment {id:row.id, created:row.created, last_updated:row.last_updated, content:row.content, intellectual_entity:row.intellectualentity})
    """

    NodeCommentSocialProfile = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Comment {id:row.id, created:row.created, last_updated:row.last_updated, content:row.content, intellectual_entity:row.intellectualentity})
    """

    NodeCommentTask = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Comment {id:row.id, title:row.title, created:row.created, last_updated:row.last_updated, content:row.content, intellectual_entity:row.intellectualentity})
    """

    NodeCommentWikiPage = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Comment {id:row.id, title:row.title, created:row.created, last_updated:row.last_updated, content:row.content, intellectual_entity:row.intellectualentity})
    """

    #Execute Import

    graph.execute_write_query_with_data(NodeCommentBlogPost, dfCommentBlogPost, database="neo4j")

    graph.execute_write_query_with_data(NodeCommentBoardPost, dfCommentBoardPost, database="neo4j")

    graph.execute_write_query_with_data(NodeCommentFile, dfCommentFile, database="neo4j")

    graph.execute_write_query_with_data(NodeCommentMicroblogPost, dfCommentMicroblogPost, database="neo4j")

    graph.execute_write_query_with_data(NodeCommentSocialProfile, dfCommentSocialProfile, database="neo4j")

    graph.execute_write_query_with_data(NodeCommentTask, dfCommentTask, database="neo4j")

    graph.execute_write_query_with_data(NodeCommentWikiPage, dfCommentWikiPage, database="neo4j")

    ("ProcessEvent finished --- %s seconds ---" % (time.time() - start_time))

    logging.info(("Process finished --- %s seconds ---" % (time.time() - start_time)))

#Main Method
if __name__ == "__main__":
   importingNodeComment()