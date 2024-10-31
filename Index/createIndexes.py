import pyodbc
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file

# Set up connections

config = load_yaml_file('C:/Users/lschloemer/Nextcloud/MOBDA 2.0/VSCodeMOBDARepository/Python/a.yaml')
db_info = config['db_infoneo']
graph = Neo4jInstance(db_info['uri'],db_info['database'],db_info['password'])

DSN = "Arrow Flight SQL ODBC DSN"
cnxn = pyodbc.connect(DSN=DSN ,autocommit=True)


def creationIndexes():

    #Cypher Query creating Indexes
    creationIndexes = """
    CREATE INDEX IndexAccountId FOR (m:Account) ON (m.id)
    CREATE INDEX IndexAttachmentId FOR (m:Attachment) ON (m.id)
    CREATE INDEX IndexBlogPostId FOR (m:BlogPost) ON (m.id)
    CREATE INDEX IndexBoardPostId FOR (m:BoardPost) ON (m.id)
    CREATE INDEX IndexCommentId FOR (m:Comment) ON (m.id)
    CREATE INDEX IndexEventId FOR (m:Event) ON (m.id)
    CREATE INDEX IndexFileId FOR (m:File) ON (m.id)
    CREATE INDEX IndexFolderId FOR (m:Folder) ON (m.id)
    CREATE INDEX IndexFollowId FOR (m:Follow) ON (m.id)
    CREATE INDEX IndexGroupWorkspaceId FOR (m:GroupWorkspace) ON (m.id)
    CREATE INDEX IndexLikeId FOR (m:Like) ON (m.id)
    CREATE INDEX IndexMessageBoardId FOR (m:MessageBoard) ON (m.id)
    CREATE INDEX IndexMicroblogId FOR (m:Microblog) ON (m.id)
    CREATE INDEX IndexMicroblogPostId FOR (m:MicroblogPost) ON (m.id)
    CREATE INDEX IndexOrganisationId FOR (m:Organisation) ON (m.id)
    CREATE INDEX IndexPersonId FOR (m:Person) ON (m.id)
    CREATE INDEX IndexSocialProfileId FOR (m:SocialProfile) ON (m.id)
    CREATE INDEX IndexSystenId FOR (m:System) ON (m.id)
    CREATE INDEX IndexTagId FOR (m:Tag) ON (m.id)
    CREATE INDEX IndexTaskId FOR (m:Task) ON (m.id)
    CREATE INDEX IndexTaskContainerId FOR (m:TaskContainer) ON (m.id)
    CREATE INDEX IndexWeblogId FOR (m:Weblog) ON (m.id)
    CREATE INDEX IndexWikiId FOR (m:Wiki) ON (m.id)
    CREATE INDEX IndexWikiPageId FOR (m:Wiki) ON (m.id)
    """
    #Execute Cypher Query
    graph.execute_write_query(creationIndexes, "neo4j")

#Main Method
if __name__ == "__main__":
    creationIndexes()