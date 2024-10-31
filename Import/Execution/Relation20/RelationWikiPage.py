import pandas as pd
import time
import logging

logging.basicConfig(level=logging.INFO)

def createRelationWikiPage(cnxn, graph) -> None:

    """
    creating all relations related to Wiki database
    graph as neo4j (Target DB) connector
    cnxn as dremio (Source DB) connector
    1. SQL queries
    2. read data from dremio in dataframe
    3. cypher queries
    4. execute cypher queries with data from dataframes using pyneoinstance
    """
    start_time = time.time()

    #1. SQL Queries

    sqlRelationWikiPageWiki = """
    SELECT wikipageid, wikiid
    FROM MOBDA_Datastore.Relations.WikiPages.Uniconnect_Relation_WikiPages_Wiki
    """

    sqlRelationWikiPagesAttachment_intellectual_entity_has_component = """
    SELECT wikipageid, attachmentid
    FROM MOBDA_Datastore.Relations.WikiPages.Uniconnect_Relation_WikiPages_Attachment_intellectual_entity_has_component
    """
    sqlRelationWikiPagesComment_intellectual_entity_has_component = """
    SELECT wikipageid, commentid
    FROM MOBDA_Datastore.Relations.WikiPages.Uniconnect_Relation_WikiPages_Comment_intellectual_entity_has_component
    """

    sqlRelationWikiPagesFollow_intellectual_entity_has_component = """
    SELECT followid, wikipageid
    FROM MOBDA_Datastore.Relations.WikiPages.Uniconnect_Relation_WikiPages_Follow_intellectual_entity_has_component
    """

    sqlRelationWikiPagesLike_intellectual_entity_has_component = """
    SELECT likeid, wikipageid
    FROM MOBDA_Datastore.Relations.WikiPages.Uniconnect_Relation_WikiPages_Like_intellectual_entity_has_component
    """
    sqlRelationWikiPagesTag_intellectual_entity_has_component = """
    SELECT tagid, wikipageid
    FROM MOBDA_Datastore.Relations.WikiPages.Uniconnect_Relation_WikiPages_Tag_intellectuial_entity_has_component
    """

    sqlRelationWikiPages_intellectual_entity_has_previous_version = """
    SELECT wikiid, previousid
    FROM MOBDA_Datastore.Relations.WikiPages.Uniconnect_Relation_WikiPages_intellectual_entity_has_previous_version
    """
    sqlRelationWikiPages_intellectual_entity_has_recent_version = """
    SELECT wikiid, recentid
    FROM MOBDA_Datastore.Relations.WikiPages.Uniconnect_Relation_WikiPages_intellecutal_entity_has_recent_version
    """
    sqlRelationWikiPages_wiki_page_has_parent = """
    SELECT wikiid, parentid
    FROM MOBDA_Datastore.Relations.WikiPages.Uniconnect_Relation_WikiPages_wiki_page_has_parent
    """
    sqlRelationWikiPages_wiki_page_has_child = """
    SELECT wikiid, childid
    FROM MOBDA_Datastore.Relations.WikiPages.Uniconnect_Relation_WikiPages_wiki_page_has_child
    """

    #2.Load Dataframes
    dfRelationWikiPageWiki= pd.read_sql(sqlRelationWikiPageWiki,cnxn)
    print (dfRelationWikiPageWiki)
    dfRelationWikiPagesAttachment_intellectual_entity_has_component= pd.read_sql(sqlRelationWikiPagesAttachment_intellectual_entity_has_component,cnxn)
    print (dfRelationWikiPagesAttachment_intellectual_entity_has_component)
    dfRelationWikiPagesComment_intellectual_entity_has_component= pd.read_sql(sqlRelationWikiPagesComment_intellectual_entity_has_component,cnxn)
    print (dfRelationWikiPagesComment_intellectual_entity_has_component)
    dfRelationWikiPagesFollow_intellectual_entity_has_component= pd.read_sql(sqlRelationWikiPagesFollow_intellectual_entity_has_component,cnxn)
    print (dfRelationWikiPagesFollow_intellectual_entity_has_component)
    dfRelationWikiPagesLike_intellectual_entity_has_component= pd.read_sql(sqlRelationWikiPagesLike_intellectual_entity_has_component,cnxn)
    print (dfRelationWikiPagesLike_intellectual_entity_has_component)
    dfRelationWikiPagesTag_intellectual_entity_has_component= pd.read_sql(sqlRelationWikiPagesTag_intellectual_entity_has_component,cnxn)
    print (dfRelationWikiPagesTag_intellectual_entity_has_component)
    dfRelationWikiPages_intellectual_entity_has_previous_version= pd.read_sql(sqlRelationWikiPages_intellectual_entity_has_previous_version,cnxn)
    print (dfRelationWikiPages_intellectual_entity_has_previous_version)
    dfRelationWikiPages_intellectual_entity_has_recent_version= pd.read_sql(sqlRelationWikiPages_intellectual_entity_has_recent_version,cnxn)
    print (dfRelationWikiPages_intellectual_entity_has_recent_version)
    dfRelationWikiPages_wiki_page_has_parent= pd.read_sql(sqlRelationWikiPages_wiki_page_has_parent,cnxn)
    print (dfRelationWikiPages_wiki_page_has_parent)
    dfRelationWikiPages_wiki_page_has_child= pd.read_sql(sqlRelationWikiPages_wiki_page_has_child,cnxn)
    print (dfRelationWikiPages_wiki_page_has_child)
    

    logging.info(("DataFrame finished --- %s seconds ---" % (time.time() - start_time)))

    #3 Cypher Queries

    RelationWikiPagesWiki_intellecutal_entity_contained_in_container = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (wp:WikiPage{id:row.wikipageid})
    MATCH (w:Wiki{id:row.wikiid})
    CREATE (wp)-[riecic:intellectual_entity_contained_in_container {cardinality: "exactly 1"}]->(w)
    CREATE (w)-[rccie:container_contains_intellectual_entity]->(wp)
    """

    RelationWikiPagesWiki_wiki_page_contained_in_wiki= """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (wp:WikiPage{id:row.wikipageid})
    MATCH (w:Wiki{id:row.wikiid})
    CREATE (w)-[rflcf:wiki_contains_wiki_page]->(wp)
    CREATE (wp)-[rfcifl:wiki_page_contained_in_wiki {cardinality: "exactly 1"}]->(w)
    """
    
    RelationWikiPagesAttachment_intellectual_entity_has_component = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (wp:WikiPage{id:row.wikipageid})
    MATCH (at:Attachment{id:row.attachmentid})
    CREATE (at)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(wp)
    CREATE (wp)-[riehc:intellectual_entity_has_component]->(at)
    """

    RelationWikiPagesComment_intellectual_entity_has_component = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (wp:WikiPage{id:row.wikipageid})
    MATCH (c:Comment{id:row.commentid})
    CREATE (c)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(wp)
    CREATE (wp)-[riehc:intellectual_entity_has_component]->(c)
    """

    RelationWikiPagesFollow_intellectual_entity_has_component = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (wp:WikiPage{id:row.wikipageid})
    MATCH (fo:Follow{id:row.followid})
    CREATE (fo)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(wp)
    CREATE (wp)-[riehc:intellectual_entity_has_component]->(fo)
    """
    RelationWikiPagesLike_intellectual_entity_has_component = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (wp:WikiPage{id:row.wikipageid})
    MATCH (l:Like{id:row.likeid})
    CREATE (l)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(wp)
    CREATE (wp)-[riehc:intellectual_entity_has_component]->(l)
    """
    RelationWikiPagesTag_intellectual_entity_has_component = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (wp:WikiPage{id:row.wikipageid})
    MATCH (t:Tag{id:row.tagid})
    CREATE (t)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(wp)
    CREATE (wp)-[riehc:intellectual_entity_has_component]->(t)
    """
    RelationWikiPages_intellectual_entity_has_previous_version = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (w1:WikiPage{id:row.wikiid})
    MATCH (w2:WikiPage{id:row.previousid})
    CREATE (w1)-[rflcf:intellectual_entity_has_previous_version  {cardinality: "maximal 1"}]->(w2)
    CREATE (w2)-[rfcifl:intellectual_entity_has_next_version  {cardinality: "maximal 1"}]->(w1)
    """
    RelationWikiPages_intellectual_entity_has_recent_version = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (w1:WikiPage{id:row.wikiid})
    MATCH (w2:WikiPage{id:row.recentid})
    CREATE (w1)-[rflcf:intellectual_entity_has_recent_version {cardinality: "exactly 1"}]->(w2)
    CREATE (w2)-[rfcifl:intellectual_entity_has_old_version]->(w1)
    """
    RelationWikiPages_wiki_page_has_parent = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (w1:WikiPage{id:row.wikiid})
    MATCH (w2:WikiPage{id:row.parentid})
    CREATE (w1)-[rflcf:wiki_page_has_parent {cardinality: "maximal 1"}]->(w2)
    """
    RelationWikiPages_wiki_page_has_child = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (w1:WikiPage{id:row.wikiid})
    MATCH (w2:WikiPage{id:row.childid})
    CREATE (w2)-[rflcf:wiki_page_has_child]->(w1)
    """

    #4 Execute Import
    graph.execute_write_queries_with_data([RelationWikiPagesWiki_intellecutal_entity_contained_in_container, RelationWikiPagesWiki_wiki_page_contained_in_wiki] ,dfRelationWikiPageWiki, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationWikiPagesAttachment_intellectual_entity_has_component,dfRelationWikiPagesAttachment_intellectual_entity_has_component, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationWikiPagesComment_intellectual_entity_has_component,dfRelationWikiPagesComment_intellectual_entity_has_component, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationWikiPagesFollow_intellectual_entity_has_component,dfRelationWikiPagesFollow_intellectual_entity_has_component, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationWikiPagesLike_intellectual_entity_has_component,dfRelationWikiPagesLike_intellectual_entity_has_component, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationWikiPagesTag_intellectual_entity_has_component,dfRelationWikiPagesTag_intellectual_entity_has_component, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationWikiPages_intellectual_entity_has_previous_version,dfRelationWikiPages_intellectual_entity_has_previous_version, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationWikiPages_intellectual_entity_has_recent_version,dfRelationWikiPages_intellectual_entity_has_recent_version, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationWikiPages_wiki_page_has_parent,dfRelationWikiPages_wiki_page_has_parent, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationWikiPages_wiki_page_has_child,dfRelationWikiPages_wiki_page_has_child, database="neo4j", partitions= 12, parallel= True, workers= 12)

    #calculate and print time spend
    ("ProcessEvent finished --- %s seconds ---" % (time.time() - start_time))

    logging.info(("Process Relation WikiPage finished --- %s seconds ---" % (time.time() - start_time)))
    
#Main method
if __name__ == "__main__":
    createRelationWikiPage()