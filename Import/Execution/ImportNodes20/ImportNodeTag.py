import pandas as pd
import time
import logging

logging.basicConfig(level=logging.INFO)

def importingNodeTag(cnxn, graph)-> None:

    """
    creation of Tag Nodes
    graph as neo4j (Target DB) connector
    cnxn as dremio (Source DB) connector
    1 SQL query
    2 Load data into dataframe
    3 preprocess data
    4 cypher query
    5 execute cypher query with data from the dataframe
    """

    start_time = time.time()


    #SQL Queries
    sqlTagBlogPost= """
    SELECT ID as id, NAME as label, "TIME" as created, 'BlogPostTag' as intellectualentity FROM "MOBDA_Datastore".Nodes.Tag."Uniconnect_Node_Tag_BlogPost" 
    """

    sqlTagBoardPost= """
    SELECT TAGUUID as id, NAME as label, CREATED as created, 'BoardPostTag' as intellectualentity FROM "MOBDA_Datastore".Nodes.Tag."Uniconnect_Node_Tag_BoardPost" 
    """

    sqlTagFile= """
    SELECT id as id, tag as label, create_date as created, 'FileTag' as intellectualentity
    FROM MOBDA_Datastore.Nodes.Tag.Uniconnect_Node_Tag_File 
    """

    sqlTagSocialProfile= """
    SELECT PROF_TAG_ID as id, PROF_TAG as label, 'SocialProfileTag' as intellectualentity FROM "MOBDA_Datastore".Nodes.Tag."Uniconnect_Node_Tag_SocialProfile" 
    """

    sqlTagTask= """
    SELECT TAGUUID as id, NAME as label, 'TaskTag' as intellectualentity FROM "MOBDA_Datastore".Nodes.Tag."Uniconnect_Node_Tag_Task" 
    """

    sqlTagWikiPage= """
    SELECT ID as id, TAG as label, CREATE_DATE as created, 'WikiPageTag' as intellectualentity FROM "MOBDA_Datastore".Nodes.Tag."Uniconnect_Node_Tag_WikiPage"
    """

    #Load Dataframes
    dfTagBlogPost = pd.read_sql(sqlTagBlogPost,cnxn)
    print (dfTagBlogPost)
    dfTagBoardPost = pd.read_sql(sqlTagBoardPost,cnxn)
    print (dfTagBoardPost)
    dfTagFile = pd.read_sql(sqlTagFile,cnxn)
    print (dfTagFile)
    dfTagSocialProfile = pd.read_sql(sqlTagSocialProfile,cnxn)
    print (dfTagSocialProfile)
    dfTagTask = pd.read_sql(sqlTagTask,cnxn)
    print (dfTagTask)
    dfTagWikiPage = pd.read_sql(sqlTagWikiPage,cnxn)
    print (dfTagWikiPage)
    
    logging.info(("DataFrame finished --- %s seconds ---" % (time.time() - start_time)))

    #Data Preprocessing
    
    #Cypher Queries

    NodeTagBlogPost = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Tag {id:row.id, label:row.label, created:row.created, intellectual_entity:row.intellectualentity})
    """

    NodeTagBoardPost = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Tag {id:row.id, label:row.label, created:row.created, intellectual_entity:row.intellectualentity})
    """

    NodeTagFile = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Tag {id:row.id, label:row.label, created:row.created, intellectual_entity:row.intellectualentity})
    """

    NodeTagSocialProfile = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Tag {id:row.id, label:row.label, intellectual_entity:row.intellectualentity})
    """

    NodeTagTask = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Tag {id:row.id, label:row.label, intellectual_entity:row.intellectualentity})
    """

    NodeTagWikiPage = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:Tag {id:row.id, label:row.label, created:row.created, intellectual_entity:row.intellectualentity})
    """

    #Execute Import

    graph.execute_write_query_with_data(NodeTagBlogPost, dfTagBlogPost, database="neo4j")

    graph.execute_write_query_with_data(NodeTagBoardPost, dfTagBoardPost, "neo4j")

    graph.execute_write_query_with_data(NodeTagFile, dfTagFile, "neo4j")

    graph.execute_write_query_with_data(NodeTagSocialProfile, dfTagSocialProfile, "neo4j")

    graph.execute_write_query_with_data(NodeTagTask, dfTagTask, "neo4j")

    graph.execute_write_query_with_data(NodeTagWikiPage, dfTagWikiPage, "neo4j")

    ("ProcessEvent finished --- %s seconds ---" % (time.time() - start_time))

    # Close the Neo4j driver
    logging.info(("Process Node Tag finished --- %s seconds ---" % (time.time() - start_time)))

#Main Method
if __name__ == "__main__":
    importingNodeTag()