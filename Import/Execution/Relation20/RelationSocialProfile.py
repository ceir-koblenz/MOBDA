import pandas as pd
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
import logging

logging.basicConfig(level=logging.INFO)

def createRelationSocialProfile(cnxn, graph) -> None:

    """
    creating all relations related to SocialProfile data
    graph as neo4j (Target DB) connector
    cnxn as dremio (Source DB) connector
    1. SQL queries
    2. read data from dremio in dataframe
    3. cypher queries
    4. execute cypher queries with data from dataframes using pyneoinstance
    """
    start_time = time.time()


    #SQL Queries
    sqlRelationSocialProfilesComment_intellectual_entity_has_component= """
    SELECT socprofileid, commentid
    FROM MOBDA_Datastore.Relations.SocialProfiles.Uniconnect_Relation_SocialProfile_Comment_intellectual_entity_has_component
    """

    sqlRelationSocialProfilesFollow_intellectual_entity_has_component= """
    SELECT followid, socprofileid 
    FROM "MOBDA_Datastore".Relations.SocialProfiles."Uniconnect_Relation_SocialProfiles_Follow_intellectul_entity_has_component"
    """

    sqlRelationSocialProfilesTag_intellectual_entity_has_component= """
    SELECT tagid, socprofileid
    FROM MOBDA_Datastore.Relations.SocialProfiles.Uniconnect_Relation_SocialProfiles_Tag_intellectuall_entity_has_component
    """
    
    sqlRelationSocialProfilesCommentLike_intellectual_component_has_simple_component= """
    SELECT likeid, commentid
    FROM MOBDA_Datastore.Relations.SocialProfiles.Uniconnect_Relation_SocialProfilesComment_Like_intellectual_component_has_simple_component
    """

    #Load Dataframes
    dfRelationSocialProfilesComment_intellectual_entity_has_component = pd.read_sql(sqlRelationSocialProfilesComment_intellectual_entity_has_component,cnxn)
    print (dfRelationSocialProfilesComment_intellectual_entity_has_component)
    dfRelationSocialProfilesFollow_intellectual_entity_has_component = pd.read_sql(sqlRelationSocialProfilesFollow_intellectual_entity_has_component,cnxn)
    print (dfRelationSocialProfilesFollow_intellectual_entity_has_component)
    dfRelationSocialProfilesTag_intellectual_entity_has_component = pd.read_sql(sqlRelationSocialProfilesTag_intellectual_entity_has_component,cnxn)
    print (dfRelationSocialProfilesTag_intellectual_entity_has_component)
    dfRelationSocialProfilesCommentLike_intellecutal_component_has_simple_component = pd.read_sql(sqlRelationSocialProfilesCommentLike_intellectual_component_has_simple_component,cnxn)
    print (dfRelationSocialProfilesCommentLike_intellecutal_component_has_simple_component)
    
    logging.info(("DataFrame finished --- %s seconds ---" % (time.time() - start_time)))

    #Cypher Queries

    RelationSocialProfilesComment_intellectual_entity_has_component = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (sp:SocialProfile{id:row.socprofileid})
    MATCH (c:Comment{id:row.commentid})
    CREATE (sp)-[riehc:intellectual_entity_has_component]->(c)
    CREATE (c)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(sp)
    """
    RelationSocialProfilesFollow_intellectual_entity_has_component = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (sp:SocialProfile{id:row.socprofileid})
    MATCH (fo:Follow{id:row.followid})
    CREATE (sp)-[riehc:intellectual_entity_has_component]->(fo)
    CREATE (fo)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(sp)
    """
    RelationSocialProfilesTag_intellectual_entity_has_component = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (sp:SocialProfile{id:row.socprofileid})
    MATCH (ta:Tag{id:row.tagid})
    CREATE (sp)-[riehc:intellectual_entity_has_component]->(ta)
    CREATE (ta)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(sp)
    """
    RelationSocialProfilesCommentLike_intellectual_component_has_simple_component = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (com:Comment{id:row.commentid})
    MATCH (li:Like{id:row.likeid})
    CREATE (com)-[riehc:intellectual_component_has_simple_component]->(li)
    CREATE (li)-[rcoie:simple_component_of_intellecutal_component ]->(com)
    """

    #Execute Import
    graph.execute_write_query_with_data(RelationSocialProfilesComment_intellectual_entity_has_component, dfRelationSocialProfilesComment_intellectual_entity_has_component, "neo4j", partitions = 12, parallel=True, workers = 12)
    graph.execute_write_query_with_data(RelationSocialProfilesFollow_intellectual_entity_has_component, dfRelationSocialProfilesFollow_intellectual_entity_has_component, "neo4j", partitions = 12, parallel=True, workers = 12)
    graph.execute_write_query_with_data(RelationSocialProfilesTag_intellectual_entity_has_component, dfRelationSocialProfilesTag_intellectual_entity_has_component, "neo4j", partitions = 12, parallel=True, workers = 12)
    graph.execute_write_query_with_data(RelationSocialProfilesCommentLike_intellectual_component_has_simple_component, dfRelationSocialProfilesCommentLike_intellecutal_component_has_simple_component, "neo4j", partitions = 12, parallel=True, workers = 12)
    

    ("ProcessEvent finished --- %s seconds ---" % (time.time() - start_time))


    # Close the Neo4j driver
    logging.info(("Process Relation SocialProfile finished --- %s seconds ---" % (time.time() - start_time)))

#Main method
if __name__ == "__main__":
    createRelationSocialProfile()