import pandas as pd
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
import logging

logging.basicConfig(level=logging.INFO)

def createRelationBoardPosts(cnxn, graph) -> None:
    start_time = time.time()

    
    """
    creating all relations related to BoardPost data
    graph as neo4j (Target DB) connector
    cnxn as dremio (Source DB) connector
    1. SQL queries
    2. read data from dremio in dataframe
    3. cypher queries
    4. execute cypher queries with data from dataframes using pyneoinstance
    """
    
    #SQL Queries
    sqlRelationBoardPostsMessageBoard_board_post_contained_in_message_board= """
    SELECT forumid, mboardid
    FROM MOBDA_Datastore.Relations.BoardPosts.Uniconnect_Relation_BoardPosts_MessageBoard_board_post_contained_in_message_board
     """

    sqlRelationBoardPostsComment_intellectual_entity_has_component = """
    SELECT commentid, forumid
    FROM MOBDA_Datastore.Relations.BoardPosts.Uniconnect_Relation_BoardPosts_Comment_intellectual_entity_has_component
    
    """
    sqlRelationBoardPostsAttachment_intellectual_entity_has_component = """
    SELECT attachmentid, forumid
    FROM MOBDA_Datastore.Relations.BoardPosts.Uniconnect_Relation_BoardPosts_Attachment_intellectual_entity_has_component
    
    """
    sqlRelationBoardPostsFollow_intellectual_entity_has_component = """
    SELECT followid, forumid
    FROM MOBDA_Datastore.Relations.BoardPosts.Uniconnect_Relation_BoardPosts_Follow_intellectual_entity_has_component
    
    """
    sqlRelationBoardPostsLike_intellectual_entity_has_component = """
    SELECT likeid, forumid
    FROM MOBDA_Datastore.Relations.BoardPosts.Uniconnect_Relation_BoardPosts_Like_intellectual_entity_has_component
    
    """
    sqlRelationBoardPostsTag_intellectual_entity_has_component = """
    SELECT tagid, forumid
    FROM MOBDA_Datastore.Relations.BoardPosts.Uniconnect_Relation_BoardPosts_Tag_intellectual_entity_has_component
     
    """
    sqlRelationBoardPostsCommentLike_intellectual_component_has_simple_component = """
    SELECT commentid, likeid
    FROM MOBDA_Datastore.Relations.BoardPosts.Uniconnect_Relation_BoardPostsComment_Like_intellectual_component_has_simple_component
    
    """
    #Load Dataframes
    dfRelationBoardPostsMessageBoard_board_post_contained_in_message_board = pd.read_sql(sqlRelationBoardPostsMessageBoard_board_post_contained_in_message_board,cnxn)
    print (dfRelationBoardPostsMessageBoard_board_post_contained_in_message_board)
    dfRelationBoardPostsComment_intellectual_entity_has_component= pd.read_sql(sqlRelationBoardPostsComment_intellectual_entity_has_component,cnxn)
    print (dfRelationBoardPostsComment_intellectual_entity_has_component)
    dfRelationBoardPostsAttachment_intellectual_entity_has_component= pd.read_sql(sqlRelationBoardPostsAttachment_intellectual_entity_has_component,cnxn)
    print (dfRelationBoardPostsAttachment_intellectual_entity_has_component)
    dfRelationBoardPostsFollow_intellectual_entity_has_component= pd.read_sql(sqlRelationBoardPostsFollow_intellectual_entity_has_component,cnxn)
    print (dfRelationBoardPostsFollow_intellectual_entity_has_component)
    dfRelationBoardPostsLike_intellectual_entity_has_component= pd.read_sql(sqlRelationBoardPostsLike_intellectual_entity_has_component,cnxn)
    print (dfRelationBoardPostsLike_intellectual_entity_has_component)
    dfRelationBoardPostsTag_intellectual_entity_has_component= pd.read_sql(sqlRelationBoardPostsTag_intellectual_entity_has_component,cnxn)
    print (dfRelationBoardPostsTag_intellectual_entity_has_component)
    dfRelationBoardPostsCommentLike_intellectual_component_has_simple_component= pd.read_sql(sqlRelationBoardPostsCommentLike_intellectual_component_has_simple_component,cnxn)
    print (dfRelationBoardPostsCommentLike_intellectual_component_has_simple_component)

    logging.info(("DataFrame finished --- %s seconds ---" % (time.time() - start_time)))

    #Cypher Queries
    RelationBoardPostsMessageBoard_board_post_contained_in_message_board= """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (b:BoardPost{id:row.forumid})
    MATCH (mb:MessageBoard{id:row.mboardid})
    CREATE (b)-[rbpcimb:board_post_contained_in_message_board {cardinality: "exactly 1"}]->(mb)
    CREATE (mb)-[rmbcbp:message_board_contains_board_post]->(b)
    """
    RelationBoardPostsMessageboard_intellecutal_entity_contained_in_container = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (b:BoardPost{id:row.forumid})
    MATCH (mb:MessageBoard{id:row.mboardid})
    CREATE (b)-[riecic:intellectual_entity_contained_in_container {cardinality: "exactly 1"}]->(mb)
    CREATE (mb)-[rccie:container_contains_intellectual_entity]->(b)
    """

    RelationBoardPostsComment_intellectual_entity_has_component = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (b:BoardPost{id:row.forumid})
    MATCH (c:Comment{id:row.commentid})
    CREATE (c)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(b)
    CREATE (b)-[riehc:intellectual_entity_has_component]->(c)
    """
    RelationBoardPostsAttachment_intellectual_entity_has_component = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (b:BoardPost{id:row.forumid})
    MATCH (at:Attachment{id:row.attachmentid})
    CREATE (at)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(b)
    CREATE (b)-[riehc:intellectual_entity_has_component]->(at)
    """

    RelationBoardPostsFollow_intellectual_entity_has_component = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (b:BoardPost{id:row.forumid})
    MATCH (f:Follow{id:row.followid})
    CREATE (f)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(b)
    CREATE (b)-[riehc:intellectual_entity_has_component]->(f)
    """
    RelationBoardPostsLike_intellectual_entity_has_component = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (b:BoardPost{id:row.forumid})
    MATCH (l:Like{id:row.likeid})
    CREATE (l)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(b)
    CREATE (b)-[riehc:intellectual_entity_has_component]->(l)
    """
    RelationBoardPostsTag_intellectual_entity_has_component = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (b:BoardPost{id:row.forumid})
    MATCH (ta:Tag{id:row.tagid})
    CREATE (ta)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(b)
    CREATE (b)-[riehc:intellectual_entity_has_component]->(ta)
    """
    RelationBoardPostsCommentLike_intellectual_component_has_simple_component = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (co:Comment{id:row.commentid})
    MATCH (li:Like{id:row.likeid})
    CREATE (co)-[riehc:intellectual_component_has_simple_component]->(li)
    CREATE (li)-[rcoie:simple_component_of_intellecutal_component]->(co)
    """

    #Execute Import

    graph.execute_write_queries_with_data([RelationBoardPostsMessageboard_intellecutal_entity_contained_in_container, RelationBoardPostsMessageBoard_board_post_contained_in_message_board], data=dfRelationBoardPostsMessageBoard_board_post_contained_in_message_board, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationBoardPostsComment_intellectual_entity_has_component,dfRelationBoardPostsComment_intellectual_entity_has_component, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationBoardPostsAttachment_intellectual_entity_has_component,dfRelationBoardPostsAttachment_intellectual_entity_has_component, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationBoardPostsFollow_intellectual_entity_has_component,dfRelationBoardPostsFollow_intellectual_entity_has_component, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationBoardPostsLike_intellectual_entity_has_component,dfRelationBoardPostsLike_intellectual_entity_has_component, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationBoardPostsTag_intellectual_entity_has_component,dfRelationBoardPostsTag_intellectual_entity_has_component, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationBoardPostsCommentLike_intellectual_component_has_simple_component,dfRelationBoardPostsCommentLike_intellectual_component_has_simple_component, database="neo4j", partitions= 12, parallel= True, workers= 12)

    ("ProcessEvent finished --- %s seconds ---" % (time.time() - start_time))


    # Close the Neo4j driver
    logging.info(("Process Relation BoardPost finished --- %s seconds ---" % (time.time() - start_time)))

#Main method
if __name__ == "__main__":
    createRelationBoardPosts()