import pandas as pd
import pyodbc
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
import logging

logging.basicConfig(level=logging.INFO)

def createRelationMicroblogPost()-> None:
    """
    creating all relations related to MicroblogPost data
    graph as neo4j (Target DB) connector
    cnxn as dremio (Source DB) connector
    1. Set up Connection
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
    sqlRelationMicroblogPostsComment_intellectual_entity_has_component= """
    SELECT comid, mblogid
    FROM "MOBDA_Datastore".Relations.MicroblogPosts."Uniconnect_Relation_MicroblogPosts_Comment_intellectual_entity_has_component"
    """

    sqlRelationMicroblogPostsLike_intellectual_entity_has_component= """
    SELECT mblogid, likeid
    FROM MOBDA_Datastore.Relations.MicroblogPosts.Uniconnect_Relation_MicroblogPosts_Like_intellectual_entity_has_component
    """

    sqlRelationMicroblogPostsMicroblog= """
    SELECT mblogid, mblogpostid
    FROM MOBDA_Datastore.Relations.MicroblogPosts.Uniconnect_Relation_MicroblogPosts_Microblog
    """
    sqlRelationMicroblogPostsCommentLike_intellectual_component_has_simple_component= """
    SELECT commentid, likeid
    FROM MOBDA_Datastore.Relations.MicroblogPosts.Uniconnect_Relation_MicroblogPostsComment_Like_intellectual_component_has_simple_component
    """

    #Load Dataframes
    dfRelationMicroblogPostsComment_intellectual_entity_has_component = pd.read_sql(sqlRelationMicroblogPostsComment_intellectual_entity_has_component,cnxn)
    print (dfRelationMicroblogPostsComment_intellectual_entity_has_component)
    dfRelationMicroblogPostsLike_intellectual_entity_has_component = pd.read_sql(sqlRelationMicroblogPostsLike_intellectual_entity_has_component,cnxn)
    print (dfRelationMicroblogPostsLike_intellectual_entity_has_component)
    dfRelationMicroblogPostsMicroblog = pd.read_sql(sqlRelationMicroblogPostsMicroblog,cnxn)
    print (dfRelationMicroblogPostsMicroblog)
    dfRelationMicroblogPostsCommentLike_intellctual_component_has_simple_component = pd.read_sql(sqlRelationMicroblogPostsCommentLike_intellectual_component_has_simple_component,cnxn)
    print (dfRelationMicroblogPostsCommentLike_intellctual_component_has_simple_component)
    
    logging.info(("DataFrame finished --- %s seconds ---" % (time.time() - start_time)))

    #Cypher Queries

    RelationMicroblogPostsComment_intellectual_entity_has_component = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (b:MicroblogPost{id:row.mblogid})
    MATCH (c:Comment{id:row.comid})
    CREATE (b)-[riehc:intellectual_entity_has_component]->(c)
    CREATE (c)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(b)
    """
    RelationMicroblogPostsLike_intellectual_entity_has_component = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (b:MicroblogPost{id:row.mblogid})
    MATCH (l:Like{id:row.likeid})
    CREATE (b)-[riehc:intellectual_entity_has_component]->(l)
    CREATE (l)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(b)
    """

    RelationMicroblogPostMicroblog_micrblog_post_contained_in_microblog = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (mbp:MicroblogPost{id:row.mblogpostid})
    MATCH (mb:Microblog{id:row.mblogid})
    CREATE (mb)-[riehc:microblog_contains_microblog_post]->(mbp)
    CREATE (mbp)-[rmpcim:microblog_post_contained_in_microblog {cardinality: "exactly 1"}]->(mb)
    """
    RelationMicroblogPostMicroblog_intellectual_entity_contained_in_container = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (mbp:MicroblogPost{id:row.mblogpostid})
    MATCH (mb:Microblog{id:row.mblogid})
    CREATE (mb)-[rccie:container_contains_intellectual_entity]->(mbp)
    CREATE (mbp)-[riecic:intellectual_entity_contained_in_container {cardinality: "exactly 1"}]->(mb)
    """

    RelationMicroblogPostsCommentLike_intellectual_component_has_simple_component = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (co:Comment{id:row.commentid})
    MATCH (li:Like{id:row.likeid})
    CREATE (co)-[riehc:intellectual_component_has_simple_component]->(li)
    CREATE (li)-[rcoie:simple_component_of_intellecutal_component]->(co)
    """

    #Execute Import
    graph.execute_write_query_with_data(RelationMicroblogPostsComment_intellectual_entity_has_component, dfRelationMicroblogPostsComment_intellectual_entity_has_component, "neo4j", partitions = 12, parallel=True, workers = 12)
    graph.execute_write_query_with_data(RelationMicroblogPostsLike_intellectual_entity_has_component, dfRelationMicroblogPostsLike_intellectual_entity_has_component, "neo4j", partitions = 12, parallel=True, workers = 12)
    graph.execute_write_queries_with_data([RelationMicroblogPostMicroblog_micrblog_post_contained_in_microblog, RelationMicroblogPostMicroblog_intellectual_entity_contained_in_container], dfRelationMicroblogPostsMicroblog, "neo4j", partitions = 12, parallel=True, workers = 12)
    graph.execute_write_query_with_data(RelationMicroblogPostsCommentLike_intellectual_component_has_simple_component, dfRelationMicroblogPostsCommentLike_intellctual_component_has_simple_component, "neo4j", partitions = 12, parallel=True, workers = 12)
    

    ("ProcessEvent finished --- %s seconds ---" % (time.time() - start_time))
    logging.info(("Process finished --- %s seconds ---" % (time.time() - start_time)))

#Main Method
if __name__ == "__main__":
    createRelationMicroblogPost()