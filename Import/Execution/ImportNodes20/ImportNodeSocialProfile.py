import pandas as pd
import time
import logging

logging.basicConfig(level=logging.INFO)

def importingNodeSocialProfile(cnxn, graph):
    """
    creation of SocialProfile Nodes
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
    sqlSocialProfile= """
    SELECT PERSON_ID as id, CREATION_DATE as created, LAST_UPDATE as last_updated, DISPLAYNAME as title FROM "MOBDA_Datastore".Nodes."Uniconnect_Node_SocialProfile"
    """

    #Load Dataframes
    dfSocialProfile = pd.read_sql(sqlSocialProfile,cnxn)
    #print (dfSocialProfile)

    logging.info(("DataFrame finished --- %s seconds ---" % (time.time() - start_time)))

    #Data Preprocessing
    

    #Cypher Queries

    NodeSocialProfile = """
    WITH $rows AS rows 
    UNWIND rows AS row
    CREATE (e:SocialProfile {id:row.id, created:row.created, last_updated:row.last_updated, title:row.title})
    """

    #Execute Import

    graph.execute_write_query_with_data(NodeSocialProfile, dfSocialProfile, database="neo4j")

    ("ProcessEvent finished --- %s seconds ---" % (time.time() - start_time))

    logging.info(("Process Node SocialProfile finished --- %s seconds ---" % (time.time() - start_time)))

#Main Method
if __name__ == "__main__":
    importingNodeSocialProfile()