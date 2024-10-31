import pandas as pd
import pyodbc
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
import logging

logging.basicConfig(level=logging.INFO)

def importingNodeLike()->None:
    """
    creating all nodes related to Like data
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
    sqlLikeBlogPost= """
    SELECT LIKE_ID as id, RATETIME as created, 'BlogPostLike' as intellectualentity
    FROM "MOBDA_Datastore".Nodes."Like"."Uniconnect_Node_Like_BlogPost" 
    """

    sqlLikeBlogPostComment= """
    SELECT LIKE_ID as id, RATETIME as created, 'BlogPostCommentLike' as intellectualentity
    FROM "MOBDA_Datastore".Nodes."Like"."Uniconnect_Node_Like_BlogPost_Comment"
    """

    sqlLikeBoardPost= """
    SELECT UUID as id, CREATED as created,'BoardPostLike' as intellectualentity
    FROM "MOBDA_Datastore".Nodes."Like"."Uniconnect_Node_Like_BoardPost"
    """

    sqlLikeBoardPostComment= """
    SELECT UUID as id, CREATED as created ,'BoardPostCommentLike' as intellectualentity
    FROM "MOBDA_Datastore".Nodes."Like"."Uniconnect_Node_Like_BoardPost_Comment" 
    """

    sqlLikeFile= """
    SELECT LIKE_ID as id, CREATE_DATE as created,'FileLike' as intellectualentity
    FROM "MOBDA_Datastore".Nodes."Like"."Uniconnect_Node_Like_File"
    """

    sqlLikeMicroblogPost= """
    SELECT RECOMMENDATION_ID as id, CREATION_DATE as created,'MicroblogPostLike' as intellectualentity
    FROM "MOBDA_Datastore".Nodes."Like"."Uniconnect_Node_Like_MicroblogPost"
    """

    sqlLikeMicroblogPostComment= """
    SELECT RECOMMENDATION_ID as id, CREATION_DATE as created,'MicroblogPostCommentLike' as intellectualentity 
    FROM "MOBDA_Datastore".Nodes."Like"."Uniconnect_Node_Like_MicroblogPost_Comment"
    """

    sqlLikeSocialProfileComment= """
    SELECT recommendation_id as id, creation_date as created, 'SocialProfileCommentLike' as intellectualentity
    FROM "MOBDA_Datastore".Nodes."Like"."Uniconnect_Node_Like_SocialProfile_Comment"
    """

    sqlLikeWikiPage= """
    SELECT LIKE_ID as id, CREATE_DATE as created,'WikiPageLike' as intellectualentity
    FROM "MOBDA_Datastore".Nodes."Like"."Uniconnect_Node_Like_WikiPage"
    """

    #Timestamps

    #Load Dataframes
    dfLikeBlogPost = pd.read_sql(sqlLikeBlogPost,cnxn)
    print (dfLikeBlogPost)
    dfLikeBlogPostComment = pd.read_sql(sqlLikeBlogPostComment,cnxn)
    print (dfLikeBlogPostComment)
    dfLikeBoardPost = pd.read_sql(sqlLikeBoardPost,cnxn)
    print (dfLikeBoardPost)
    dfLikeBoardPostComment = pd.read_sql(sqlLikeBoardPostComment,cnxn)
    print (dfLikeBoardPostComment)
    dfLikeFile = pd.read_sql(sqlLikeFile,cnxn)
    print (dfLikeFile)
    dfLikeMicroblogPost = pd.read_sql(sqlLikeMicroblogPost,cnxn)
    print (dfLikeMicroblogPost)
    dfLikeMicroblogPostComment = pd.read_sql(sqlLikeMicroblogPostComment,cnxn)
    print (dfLikeMicroblogPostComment)
    dfLikeSocialProfileComment = pd.read_sql(sqlLikeSocialProfileComment,cnxn)
    print (dfLikeSocialProfileComment)
    dfLikeWikiPage = pd.read_sql(sqlLikeWikiPage,cnxn)
    print (dfLikeWikiPage)

    logging.info(("DataFrame finished --- %s seconds ---" % (time.time() - start_time)))

    #Data Preprocessing
    #Timestamp?!

    #Cypher Queries

    NodeLikeBlogPost = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Like {id:row.id, created:row.created, intellectual_entity:row.intellectualentity})
    """
    NodeLikeBlogPostComment = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Like {id:row.id, created:row.created, intellectual_entity:row.intellectualentity})
    """

    NodeLikeBoardPost = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Like {id:row.id, created:row.created, intellectual_entity:row.intellectualentity})
    """

    NodeLikeBoardPostComment = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Like {id:row.id, created:row.created, intellectual_entity:row.intellectualentity})
    """

    NodeLikeFile = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Like {id:row.id, created:row.created, intellectual_entity:row.intellectualentity})
    """
    NodeLikeMicroblogPost= """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Like {id:row.id, created:row.created, intellectual_entity:row.intellectualentity})
    """

    NodeLikeMicroblogPostComment= """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Like {id:row.id, created:row.created, intellectual_entity:row.intellectualentity})
    """
    NodeLikeSocialProfileComment = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Like {id:row.id, created:row.created, intellectual_entity:row.intellectualentity})
    """

    NodeLikeWikiPage = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Like {id:row.id,  created:row.created, intellectual_entity:row.intellectualentity})
    """

    #Execute Import

    graph.execute_write_query_with_data(NodeLikeBlogPost, dfLikeBlogPost, database="neo4j")

    graph.execute_write_query_with_data(NodeLikeBlogPostComment, dfLikeBlogPostComment, database="neo4j")

    graph.execute_write_query_with_data(NodeLikeBoardPost, dfLikeBoardPost, database="neo4j")

    graph.execute_write_query_with_data(NodeLikeBoardPostComment, dfLikeBoardPostComment, database="neo4j")

    graph.execute_write_query_with_data(NodeLikeFile, dfLikeFile, database="neo4j")

    graph.execute_write_query_with_data(NodeLikeMicroblogPost, dfLikeMicroblogPost, database="neo4j")

    graph.execute_write_query_with_data(NodeLikeMicroblogPostComment, dfLikeMicroblogPostComment, database="neo4j")

    graph.execute_write_query_with_data(NodeLikeSocialProfileComment, dfLikeSocialProfileComment, database="neo4j")

    graph.execute_write_query_with_data(NodeLikeWikiPage, dfLikeWikiPage, database="neo4j")

    ("ProcessEvent finished --- %s seconds ---" % (time.time() - start_time))

    # Close the Neo4j driver
    logging.info(("Process finished --- %s seconds ---" % (time.time() - start_time)))

#Main Method
if __name__ == "__main__":
    importingNodeLike()