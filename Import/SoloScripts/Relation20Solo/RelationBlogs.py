import pandas as pd
import pyodbc
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
import logging

logging.basicConfig(level=logging.INFO)

def createRelationBlogs()-> None:
    """
    creating all relations related to Blogs data
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
    sqlRelationBlog_post_contained_in_weblog= """
    SELECT blogid, WEBSITEID as websiteid, weblogid 
    FROM "MOBDA_Datastore".Relations.Blogs."Uniconnect_Relation_Blogs_blog_post_contained_in_weblog"
    """

    sqlRelationBlogComment_intellectual_entity_has_component = """
    SELECT blogid, entryid, comid 
    FROM "MOBDA_Datastore".Relations.Blogs."Uniconnect_Relation_Blogs_Comment_intellectual_entity_has_component"
    """
    sqlRelationBlogLike_intellectual_entity_has_component = """
    SELECT blogid, likeid
    FROM MOBDA_Datastore.Relations.Blogs.Uniconnect_Relation_Blogs_Like_intellectual_entity_has_component
    """
    sqlRelationBlogTag_intellectual_entity_has_component = """
    SELECT tagid, blogid
    FROM MOBDA_Datastore.Relations.Blogs.Uniconnect_Relation_Blogs_Tag_intellectual_entity_has_component
    """
    sqlRelationBlogCommentLike_intellectual_component_has_simple_component = """
    SELECT likeid, commentid
    FROM MOBDA_Datastore.Relations.Blogs.Uniconnect_Relation_BlogPostsComment_Like_intellectual_component_has_simple_component
    """

    #Load Dataframes
    dfRelationBlog_post_contained_in_weblog = pd.read_sql(sqlRelationBlog_post_contained_in_weblog,cnxn)
    print (dfRelationBlog_post_contained_in_weblog)
    dfRelationBlogComment_intellectual_entity_has_component = pd.read_sql(sqlRelationBlogComment_intellectual_entity_has_component,cnxn)
    print (dfRelationBlogComment_intellectual_entity_has_component)
    dfRelationBlogLike_intellectual_entity_has_component = pd.read_sql(sqlRelationBlogLike_intellectual_entity_has_component,cnxn)
    print (dfRelationBlogLike_intellectual_entity_has_component)
    dfRelationBlogTag_intellectual_entity_has_component = pd.read_sql(sqlRelationBlogTag_intellectual_entity_has_component,cnxn)
    print (dfRelationBlogTag_intellectual_entity_has_component)
    dfRelationBlogCommentLike_intellectual_component_has_simple_component = pd.read_sql(sqlRelationBlogCommentLike_intellectual_component_has_simple_component,cnxn)
    print (dfRelationBlogCommentLike_intellectual_component_has_simple_component)

    logging.info(("DataFrame finished --- %s seconds ---" % (time.time() - start_time)))

    #Cypher Queries
    RelationBlog_post_contained_in_weblog= """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (b:BlogPost{id:row.blogid})
    MATCH (wb:Weblog{id:row.weblogid})
    CREATE (b)-[rbpciw:blog_post_contained_in_weblog {cardinality: "exactly 1"}]->(wb)
    CREATE (wb)-[rwcbp:weblog_contains_blog_post]->(b)
    """
    RelationIntellectual_entity_contained_in_container = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (b:BlogPost{id:row.blogid})
    MATCH (wb:Weblog{id:row.weblogid})
    CREATE (b)-[riecic:intellectual_entity_contained_in_container {cardinality: "exactly 1"}]->(wb)
    CREATE (wb)-[rccie:container_contains_intellectual_entity]->(b)
    """
    #WHERE row.websiteid = row.weblogid

    RelationBlogComment_intellectual_entity_has_component = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (b:BlogPost{id:row.blogid})
    MATCH (c:Comment{id:row.comid})
    CREATE (b)-[riehc:intellectual_entity_has_component]->(c)
    CREATE (c)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(b)
    """
    RelationBlogLike_intellectual_entity_has_component = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (b:BlogPost{id:row.blogid})
    MATCH (l:Like{id:row.likeid})
    CREATE (b)-[riehc:intellectual_entity_has_component]->(l)
    CREATE (l)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(b)
    """

    RelationBlogTag_intellectual_entity_has_component = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (b:BlogPost{id:row.blogid})
    MATCH (t:Tag{id:row.tagid})
    CREATE (b)-[riehc:intellectual_entity_has_component]->(t)
    CREATE (t)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(b)
    """
    RelationBlogCommentLike_intellectual_component_has_simple_component = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (co:Comment{id:row.commentid})
    MATCH (li:Like{id:row.likeid})
    CREATE (co)-[riehc:intellectual_component_has_simple_component]->(li)
    CREATE (li)-[rcoie:simple_component_of_intellecutal_component ]->(co)
    """


    #Execute Import

    graph.execute_write_query_with_data(RelationBlog_post_contained_in_weblog, dfRelationBlog_post_contained_in_weblog, "neo4j", partitions = 12, parallel=True, workers = 12)
    graph.execute_write_query_with_data(RelationIntellectual_entity_contained_in_container, dfRelationBlog_post_contained_in_weblog, "neo4j", partitions = 12, parallel=True, workers = 12)
    graph.execute_write_query_with_data(RelationBlogComment_intellectual_entity_has_component, dfRelationBlogComment_intellectual_entity_has_component, "neo4j", partitions = 12, parallel=True, workers = 12)
    graph.execute_write_query_with_data(RelationBlogLike_intellectual_entity_has_component, dfRelationBlogLike_intellectual_entity_has_component, "neo4j", partitions = 12, parallel=True, workers = 12)
    graph.execute_write_query_with_data(RelationBlogTag_intellectual_entity_has_component, dfRelationBlogTag_intellectual_entity_has_component, "neo4j", partitions = 12, parallel=True, workers = 12)
    graph.execute_write_query_with_data(RelationBlogCommentLike_intellectual_component_has_simple_component, dfRelationBlogCommentLike_intellectual_component_has_simple_component, "neo4j", partitions = 12, parallel=True, workers = 12)
    
    ("ProcessEvent finished --- %s seconds ---" % (time.time() - start_time))

    logging.info(("Process finished --- %s seconds ---" % (time.time() - start_time)))

#Main Method
if __name__ == "__main__":
    createRelationBlogs()