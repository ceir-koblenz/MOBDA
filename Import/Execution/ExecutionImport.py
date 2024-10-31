import pyodbc
import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
import logging

logging.basicConfig(level=logging.INFO)

# Nodes Data Layer
from ImportNodes20.ImportNodeAccount import importingNodeAccount
from ImportNodes20.ImportNodeAttachment import importingNodeAttachment
from ImportNodes20.ImportNodeBlogPost import importingNodeBlogPost
from ImportNodes20.ImportNodeBoardPost import importingNodeBoardPost
from ImportNodes20.ImportNodeComment import importingNodeComment
from ImportNodes20.ImportNodeEvent import importingNodeEvent
from ImportNodes20.ImportNodeFile import importingNodeFile
from ImportNodes20.ImportNodeFileLibrary import importingNodeFileLibrary
from ImportNodes20.ImportNodeFolder import importingNodeFolder
from ImportNodes20.ImportNodeFollow import importingNodeFollow
from ImportNodes20.ImportNodeGroupWorkspace import importingNodeGroupWorkspace
from ImportNodes20.ImportNodeLike import importingNodeLike
from ImportNodes20.ImportNodeMessageBoard import importingNodeMessageBoard
from ImportNodes20.ImportNodeMicroblog import importingNodeMicroblog
from ImportNodes20.ImportNodeMicroblogPost import importingNodeMicroblogPost
from ImportNodes20.ImportNodeOrganisation import importingNodeOrganisation
from ImportNodes20.ImportNodePerson import importingNodePerson
from ImportNodes20.ImportNodeSocialProfile import importingNodeSocialProfile
from ImportNodes20.ImportNodeSystem import importingNodeSystem
from ImportNodes20.ImportNodeTag import importingNodeTag
from ImportNodes20.ImportNodeTask import importingNodeTask
from ImportNodes20.ImportNodeTaskContainer import importingNodeTaskConatiner
from ImportNodes20.ImportNodeWeblog import importingNodeWeblog
from ImportNodes20.ImportNodeWiki import importingNodeWiki
from ImportNodes20.ImportNodeWikiPage import importingNodeWikiPage

# Nodes Ontology Layer
from OntologyLayer20.AbstractImport20 import importingAbstractNodes

#Relations Onotology Layer <-> Data Layer
from OntologyLayer20.OntologyRelation import creatingAbstractRelation

#Relations Data Layer
from Relation20.RelationAccount import createRelationAccounts
from Relation20.RelationBlogs import createRelationBlogs
from Relation20.RelationBoardPost import createRelationBoardPosts
from Relation20.RelationEvent import createRelationEvents
from Relation20.RelationFile import createRelationFiles
from Relation20.RelationGroupWorkspace import createRelationGroupWorkspaces
from Relation20.RelationMicroblogPost import createRelationMicroblogPost
from Relation20.RelationOrganisation import createRelationOrganisation
from Relation20.RelationSocialProfile import createRelationSocialProfile
from Relation20.RelationTask import createRelationTask
from Relation20.RelationWikiPage import createRelationWikiPage

logging.basicConfig(level=logging.INFO)

def main() -> None:
    """
    Executing all import scripts
    """
    start_time = time.time()
    

    # Creating connection to neo4j, reading from a yaml config file
    config = load_yaml_file('C:/Users/lschloemer/Nextcloud/MOBDA 2.0/VSCodeMOBDARepository/Python/a.yaml')
    db_info = config['db_infoneo']
    graph = Neo4jInstance(db_info['uri'],db_info['database'],db_info['password'])

    #create connection to Dremio
    DSN = "Arrow Flight SQL ODBC DSN"
    cnxn = pyodbc.connect(DSN=DSN ,autocommit=True)

    #Executing all import scripts
    #Parameter: cnxn for connection to Dremio, graph for connection to neo4j

    #Function for Nodes Data Layer
    importingNodeAccount(cnxn, graph)
    importingNodeAttachment(cnxn, graph)
    importingNodeBlogPost(cnxn, graph)
    importingNodeBoardPost(cnxn, graph)
    importingNodeComment(cnxn, graph)
    importingNodeEvent(cnxn, graph)
    importingNodeFile(cnxn, graph)
    importingNodeFileLibrary(cnxn, graph)
    importingNodeFolder(cnxn, graph)
    importingNodeFollow(cnxn, graph)
    importingNodeGroupWorkspace(cnxn, graph)
    importingNodeLike(cnxn, graph)
    importingNodeMessageBoard(cnxn, graph)
    importingNodeMicroblog(cnxn, graph)
    importingNodeMicroblogPost(cnxn, graph)
    importingNodeOrganisation(graph)
    importingNodePerson(cnxn, graph)
    importingNodeSocialProfile(cnxn, graph)
    importingNodeSystem(cnxn, graph)
    importingNodeTag(cnxn, graph)
    importingNodeTask(cnxn, graph)
    importingNodeTaskConatiner(cnxn, graph)
    importingNodeWeblog(cnxn, graph)
    importingNodeWiki(cnxn, graph)
    importingNodeWikiPage(cnxn, graph)

    # Functions for Ontology Layer
    importingAbstractNodes(graph)
    creatingAbstractRelation(graph)

    # Functions for Relations Data Layer
    createRelationAccounts(cnxn, graph)
    createRelationBlogs(cnxn, graph)
    createRelationBoardPosts(cnxn, graph)
    createRelationEvents(cnxn, graph)
    createRelationFiles(cnxn, graph)
    createRelationGroupWorkspaces(cnxn, graph)
    createRelationMicroblogPost(cnxn, graph)
    createRelationOrganisation(cnxn, graph)
    createRelationSocialProfile(cnxn, graph)
    createRelationTask(cnxn, graph)
    createRelationWikiPage(cnxn, graph)

    #Measuring time and print result
    ("ProcessEvent finished --- %s seconds ---" % (time.time() - start_time))
    logging.info("Process Complete finished --- %s seconds ---" % (time.time() - start_time))

#Main method to execute
if __name__ == "__main__":
    main()