import pandas as pd
import pyodbc
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
import logging

logging.basicConfig(level=logging.INFO)

def createRelationFiles()->None:
    """
    creating all relations related to File data
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
    sqlRelationFilesFolder_file_contained_in_folder= """
    SELECT fileid, folderid
    FROM MOBDA_Datastore.Relations."Files".Uniconnect_Relation_Files_Folder_file_contained_in_folder
    """

    sqlRelationFilesComment_intellectual_entity_has_component = """
    SELECT fileid, commentid
    FROM MOBDA_Datastore.Relations."Files".Uniconnect_Relation_Files_Comment_intellectual_entity_has_component
    """
    sqlRelationFilesFollow_intellectual_entity_has_component = """
    SELECT followid, fileid
    FROM MOBDA_Datastore.Relations."Files".Uniconnect_Relation_Files_Follow_intellectual_entity_has_component
    """

    sqlRelationFilesLike_intellectual_entity_has_component = """
    SELECT likeid, fileid
    FROM MOBDA_Datastore.Relations."Files".Uniconnect_Relation_Files_Like_intellectual_entity_has_component
    """
    sqlRelationFilesTag_intellectual_entity_has_component = """
    SELECT tagid, fileid
    FROM MOBDA_Datastore.Relations."Files".Uniconnect_Relation_Files_Tag_intellectual_entity_has_component
    """
    sqlRelationFilesFileLibrary = """
    SELECT fileid, libid
    FROM MOBDA_Datastore.Relations."Files".Uniconnect_Relation_Files_FileLibrary
    """

    sqlRelationFiles_intellectual_entity_has_previous_version = """
    SELECT fileid, previousid
    FROM MOBDA_Datastore.Relations."Files"."Uniconnect_Relation_Files_intellectual_entity_has_previous_version"
    """
    
    sqlRelationFiles_intellectual_entity_has_recent_version = """
    SELECT fileid, recentid
    FROM MOBDA_Datastore.Relations."Files".Uniconnect_Relation_Files_intellectual_entity_has_recent_version
    """
    sqlRelationFolder_folder_has_parent = """
    SELECT childid, parentid
    FROM MOBDA_Datastore.Relations."Files".Uniconnect_Relation_Folders_folder_has_parent
    """
    sqlRelationFileLibraryFolder_file_library_contains_folder ="""
    SELECT libid, folderid
    FROM MOBDA_Datastore.Relations."Files".Uniconnect_Relation_FileLibrary_Folder_file_library_conatins_folder
    """
    sqlRelationFolderFollow_intellectual_entity_has_component ="""
    SELECT followid, folderid
    FROM MOBDA_Datastore.Relations."Files".Uniconnect_Relation_Folder_Follow_intellectual_entity_has_component
    """

    #Load Dataframes
    dfRelationFilesFolder_file_contained_in_folder= pd.read_sql(sqlRelationFilesFolder_file_contained_in_folder,cnxn)
    print (dfRelationFilesFolder_file_contained_in_folder)
    dfRelationFilesComment_intellectual_entity_has_component= pd.read_sql(sqlRelationFilesComment_intellectual_entity_has_component,cnxn)
    print (dfRelationFilesComment_intellectual_entity_has_component)
    dfRelationFilesFollow_intellectual_entity_has_component= pd.read_sql(sqlRelationFilesFollow_intellectual_entity_has_component,cnxn)
    print (dfRelationFilesFollow_intellectual_entity_has_component)
    dfRelationFilesLike_intellectual_entity_has_component= pd.read_sql(sqlRelationFilesLike_intellectual_entity_has_component,cnxn)
    print (dfRelationFilesLike_intellectual_entity_has_component)
    dfRelationFilesTag_intellectual_entity_has_component= pd.read_sql(sqlRelationFilesTag_intellectual_entity_has_component,cnxn)
    print (dfRelationFilesTag_intellectual_entity_has_component)
    dfRelationFilesFileLibrary= pd.read_sql(sqlRelationFilesFileLibrary,cnxn)
    print (dfRelationFilesFileLibrary)
    dfRelationFiles_intellectual_entity_has_previous_version = pd.read_sql(sqlRelationFiles_intellectual_entity_has_previous_version,cnxn)
    print (dfRelationFiles_intellectual_entity_has_previous_version)
    dfRelationFiles_intellectual_entity_has_recent_version= pd.read_sql(sqlRelationFiles_intellectual_entity_has_recent_version,cnxn)
    print (dfRelationFiles_intellectual_entity_has_recent_version)
    dfRelationFolder_folder_has_parent= pd.read_sql(sqlRelationFolder_folder_has_parent,cnxn)
    print (dfRelationFolder_folder_has_parent)
    dfRelationFileLibraryFolder_file_library_contains_folder= pd.read_sql(sqlRelationFileLibraryFolder_file_library_contains_folder,cnxn)
    print (dfRelationFileLibraryFolder_file_library_contains_folder)
    dfRelationFolderFollow_intellectual_entity_has_component= pd.read_sql(sqlRelationFolderFollow_intellectual_entity_has_component,cnxn)
    print (dfRelationFolderFollow_intellectual_entity_has_component)

    logging.info(("DataFrame finished --- %s seconds ---" % (time.time() - start_time)))

    #Cypher Queries
    RelationFileFolder_file_contained_in_folder= """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (f:File{id:row.fileid})
    MATCH (fo:Folder{id:row.folderid})
    CREATE (f)-[rfcif:file_contained_in_folder {cardinality: "maximal 1"}]->(fo)
    CREATE (fo)-[rfcf:folder_contains_file]->(f)
    """
    RelationFilesComment_intellectual_entity_has_component = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (f:File{id:row.fileid})
    MATCH (c:Comment{id:row.commentid})
    CREATE (c)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(f)
    CREATE (f)-[riehc:intellectual_entity_has_component]->(c)
    """
    RelationFilesFollow_intellectual_entity_has_component = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (f:File{id:row.fileid})
    MATCH (fo:Follow{id:row.followid})
    CREATE (fo)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(f)
    CREATE (f)-[riehc:intellectual_entity_has_component]->(fo)
    """
    RelationFilesLike_intellectual_entity_has_component = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (f:File{id:row.fileid})
    MATCH (l:Like{id:row.likeid})
    CREATE (l)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(f)
    CREATE (f)-[riehc:intellectual_entity_has_component]->(l)
    """
    RelationFilesTag_intellectual_entity_has_component = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (f:File{id:row.fileid})
    MATCH (t:Tag{id:row.tagid})
    CREATE (t)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(f)
    CREATE (f)-[riehc:intellectual_entity_has_component]->(t)
    """

    RelationFilesFileLibrary_intellecutal_entity_contained_in_container = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (f:File{id:row.fileid})
    MATCH (fl:FileLibrary{id:row.libid})
    CREATE (f)-[riecic:intellectual_entity_contained_in_container {cardinality: "exactly 1"}]->(fl)
    CREATE (fl)-[rccie:container_contains_intellectual_entity]->(f)
    """

    RelationFilesFileLibrary_file_contained_in_file_library = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (f:File{id:row.fileid})
    MATCH (fl:FileLibrary{id:row.libid})
    CREATE (fl)-[rflcf:file_library_contains_file]->(f)
    CREATE (f)-[rfcifl:file_contained_in_file_library {cardinality: "exactly 1"}]->(fl)
    """

    RelationFiles_intellectual_entity_has_previous_version = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (f1:File{id:row.fileid})
    MATCH (f2:File{id:row.previousid})
    CREATE (f1)-[rflcf:intellectual_entity_has_previous_version  {cardinality: "maximal 1"}]->(f2)
    CREATE (f2)-[rfcifl:intellectual_entity_has_next_version  {cardinality: "maximal 1"}]->(f1)
    """
    RelationFiles_intellectual_entity_has_recent_version = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (f1:File{id:row.fileid})
    MATCH (f2:File{id:row.recentid})
    CREATE (f1)-[rflcf:intellectual_entity_has_recent_version {cardinality: "exactly 1"}]->(f2)
    CREATE (f2)-[rfcifl:intellectual_entity_has_old_version]->(f1)
    """
    RelationFolder_folder_has_parent = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (fp:Folder{id:row.parentid})
    MATCH (fc:Folder{id:row.childid})
    CREATE (fc)-[rthp:task_has_parent {cardinality: "maximal 1"}]->(fp)
    CREATE (fp)-[rthc:task_has_child]->(fc)
    """
    RelationFileLibraryFolder_file_library_contains_folder = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (fl:FileLibrary{id:row.libid})
    MATCH (fo:Folder{id:row.folderid})
    CREATE (fl)-[rflcf:file_library_contains_folder]->(fo)
    CREATE (fo)-[rfcifl:folder_contained_in_file_library {cardinality: "exactly 1"}]->(fl)
    """
    RelationFileLibraryFolder_intellectual_entity_contained_in_container = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (fl:FileLibrary{id:row.libid})
    MATCH (fo:Folder{id:row.folderid})
    CREATE (fl)-[rflcf:container_contains_intellectual_entity]->(fo)
    CREATE (fo)-[rfcifl:intellectual_entity_contained_in_container {cardinality: "exactly 1"}]->(fl)
    """
    RelationFolderFollow_intellectual_entity_has_component = """
    WITH $rows AS rows 
    UNWIND rows AS row
    MATCH (fo:Folder{id:row.folderid})
    MATCH (foll:Follow{id:row.followid})
    CREATE (foll)-[rcoie:component_of_intellectual_entity {cardinality: "exactly 1"}]->(fo)
    CREATE (fo)-[riehc:intellectual_entity_has_component]->(foll)
    """

    #Execute Import
    graph.execute_write_query_with_data(RelationFileFolder_file_contained_in_folder,dfRelationFilesFolder_file_contained_in_folder, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationFilesComment_intellectual_entity_has_component,dfRelationFilesComment_intellectual_entity_has_component, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationFilesFollow_intellectual_entity_has_component,dfRelationFilesFollow_intellectual_entity_has_component, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationFilesLike_intellectual_entity_has_component,dfRelationFilesLike_intellectual_entity_has_component, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationFilesTag_intellectual_entity_has_component,dfRelationFilesTag_intellectual_entity_has_component, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_queries_with_data([RelationFilesFileLibrary_intellecutal_entity_contained_in_container, RelationFilesFileLibrary_file_contained_in_file_library] ,dfRelationFilesFileLibrary, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationFiles_intellectual_entity_has_previous_version,dfRelationFiles_intellectual_entity_has_previous_version, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationFiles_intellectual_entity_has_recent_version, dfRelationFiles_intellectual_entity_has_recent_version, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationFolder_folder_has_parent, dfRelationFolder_folder_has_parent, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_queries_with_data([RelationFileLibraryFolder_file_library_contains_folder, RelationFileLibraryFolder_intellectual_entity_contained_in_container], dfRelationFileLibraryFolder_file_library_contains_folder, database="neo4j", partitions= 12, parallel= True, workers= 12)
    graph.execute_write_query_with_data(RelationFolderFollow_intellectual_entity_has_component, dfRelationFolderFollow_intellectual_entity_has_component, database="neo4j", partitions= 12, parallel= True, workers= 12)
   
    ("ProcessEvent finished --- %s seconds ---" % (time.time() - start_time))

    logging.info(("Process finished --- %s seconds ---" % (time.time() - start_time)))

#Main Method
if __name__ == "__main__":
    createRelationFiles()