import time
from pyneoinstance import Neo4jInstance
from pyneoinstance import load_yaml_file
import logging

logging.basicConfig(level=logging.INFO)

def creatingAbstractRelation(graph) -> None:
    """
    creation of relations between data and ontology layer
    1 cypher queries
    2 executoion of cypher queries
    """
    start_time = time.time()

    #Cypher Queries für Relations

    queryRelationInheritanceAccount = """
    MATCH (acc:Account_Concept)
    MATCH (ac:Account)
    CREATE (ac)-[rac:is_a]->(acc)
    """

    queryRelationInheritanceAttachment = """
    //Inheritance of Attachment 
    MATCH (atc:Attachement_Concept)
    MATCH (itc:Item_Concept)
    MATCH (coc:Component_Concept)
    MATCH (icc:IntellectualComponent_Concept)
    WITH [atc, itc, coc, icc] AS ConATIN 
    UNWIND ConATIN as conATIN
    MATCH (at:Attachment)
    CREATE (at)-[rat:is_a]->(conATIN)
    """
    queryRelationInheritanceBlogPost = """
    //Relations is_a zwischen child Nodes und Parent Nodes_Concepts
    MATCH (bc:BlogPost_Concept)
    MATCH (iec:IntellectualEntity_Concept)
    MATCH (itc:Item_Concept)
    WITH [bc, itc, iec] AS ConBGIN 
    UNWIND ConBGIN as conBGIN
    MATCH (b:BlogPost)
    CREATE (b)-[rba:is_a]->(conBGIN)
    """

    queryRelationInheritanceBoardPost = """
    //Inheritance of BoadPOst
    MATCH (bpc:BoardPost_Concept)
    MATCH (itc:Item_Concept)
    MATCH (iec:IntellectualEntity_Concept)
    WITH [bpc, itc, iec] AS ConBPIN
    UNWIND ConBPIN as conBPIN
    MATCH (bp:BoardPost)
    CREATE (bp)-[rbp:is_a]->(conBPIN)
    """

    queryRelationInheritanceComment = """
    //Inheritance of Comment
    MATCH (comc:Comment_Concept)
    MATCH (itc:Item_Concept)
    MATCH (coc:Component_Concept)
    MATCH (icc:IntellectualComponent_Concept)
    WITH [comc, itc, coc, icc] AS ConCOIN 
    UNWIND ConCOIN as conCOIN
    MATCH (com:Comment)
    CREATE (com)-[rcom:is_a]->(conCOIN)
    """

    queryRelationInheritanceEvent = """
    MATCH (evc:Event_Concept)
    MATCH (ev:Event)
    CREATE (ev)-[re:is_a]->(evc)
    """

    queryRelationInheritanceFile = """
    //Inheritance of File 
    MATCH (fic:File_Concept)
    MATCH (itc:Item_Concept)
    MATCH (iec:IntellectualEntity_Concept)
    WITH [fic, itc, iec] AS ConFIIN
    UNWIND ConFIIN as conFIIN
    MATCH (fil:File)
    CREATE (fil)-[rfil:is_a]->(conFIIN)
    """

    queryRelationInheritanceFileLibrary = """
    MATCH (coc:Container_Concept)
    MATCH (filic:FileLibrary_Concept)
    WITH [coc, filic] AS ConFILIC
    UNWIND ConFILIC as conFILIC
    MATCH (fili:FileLibrary)
    CREATE (fili)-[rfili:is_a]->(conFILIC)
    """

    queryRelationInheritanceFolder = """
    //Inheritance of Folder
    MATCH (foc:Folder_Concept)
    MATCH (itc:Item_Concept)
    MATCH (iec:IntellectualEntity_Concept)
    WITH [foc, itc, iec] AS ConFOCIN
    UNWIND ConFOCIN as conFOCIN
    MATCH (fo:Folder)
    CREATE (fo)-[rfoc:is_a]->(conFOCIN)
    """

    queryRelationInheritanceFollow = """
    //Inheritance of Follow 
    MATCH (folc:Follow_Concept)
    MATCH (itc:Item_Concept)
    MATCH (coc:Component_Concept)
    MATCH (scc:SimpleComponent_Concept)
    WITH [folc, itc, coc, scc] AS ConFOLIN 
    UNWIND ConFOLIN as conFOLIN
    MATCH (fol:Follow)
    CREATE (fol)-[rfol:is_a]->(conFOLIN)
    """

    queryRelationInheritanceGroupWorkspace = """
    MATCH (spa:Space_Concept)
    MATCH (gwsc:GroupWorkspace_Concept)
    WITH [gwsc, spa] AS ConGWSIN 
    UNWIND ConGWSIN as conGWSIN
    MATCH (gws:GroupWorkspace)
    CREATE (gws)-[rgws:is_a]->(conGWSIN)
    """

    queryRelationInheritanceLike = """
    //Inheritance of Like
    MATCH (likec:Like_Concept)
    MATCH (itc:Item_Concept)
    MATCH (coc:Component_Concept)
    MATCH (scc:SimpleComponent_Concept)
    WITH [likec, itc, coc, scc] AS ConLIKIN 
    UNWIND ConLIKIN as conLIKIN
    MATCH (like:Like)
    CREATE (like)-[rlike:is_a]->(conLIKIN)
    """

    queryRelationInheritanceMessageBoard = """
    //Inheritance of MessageBoard
    MATCH (coc:Container_Concept)
    MATCH (mbc:MessageBoard_Concept)
    WITH [coc, mbc] AS ConMBCIN
    UNWIND ConMBCIN as conMBCIN
    MATCH (mb:MessageBoard)
    CREATE (mb)-[rmb:is_a]->(conMBCIN)
    """

    queryRelationInheritanceMicroblog = """
    MATCH (coc:Container_Concept)
    MATCH (mbc:Microblog_Concept)
    WITH [coc, mbc] AS ConMBC
    UNWIND ConMBC as conMBC
    MATCH (mb:Microblog)
    CREATE (mb)-[rmb:is_a]->(conMBC)
    """

    queryRelationInheritanceMicroblogPost = """
    MATCH (mbpc:MicroblogPost_Concept)
    MATCH (itc:Item_Concept)
    MATCH (iec:IntellectualEntity_Concept)
    WITH [mbpc, itc, iec] AS ConMBPIN
    UNWIND ConMBPIN as conMBPIN
    MATCH (mbp:MicroblogPost)
    CREATE (mbp)-[rfil:is_a]->(conMBPIN)
    """

    queryRelationInheritanceOrganisation = """
    MATCH (agc:Agent_Concept)
    MATCH (ogc:Organisation_Concept)
    WITH [ogc, agc] AS ConORCIN
    UNWIND ConORCIN as conORCIN
    MATCH (og:Organisation)
    CREATE (og)-[rog:is_a]->(conORCIN)
    """

    queryRelationInheritancePerson = """
    MATCH (agc:Agent_Concept)
    MATCH (pec:Person_Concept)
    WITH [agc, pec] AS ConPERIN
    UNWIND ConPERIN as conPERIN
    MATCH (pe:Person)
    CREATE (pe)-[rpe:is_a]->(conPERIN)
    """

    queryRelationInheritanceSocialProfile = """
    //Inheritance of SocialProfile
    MATCH (sopc:SocialProfile_Concept)
    MATCH (itc:Item_Concept)
    MATCH (iec:IntellectualEntity_Concept)
    WITH [sopc, itc, iec] AS ConSOPIN
    UNWIND ConSOPIN as conSOPIN
    MATCH (sop:SocialProfile)
    CREATE (sop)-[rsop:is_a]->(conSOPIN)
    """

    queryRelationInheritanceSystem = """
    MATCH (syc:System_Concept)
    MATCH (sy:System)
    CREATE (sy)-[rsy:is_a]->(syc)
    """
    queryRelationInheritanceTag = """
    MATCH (tagc:Tag_Concept)
    MATCH (itc:Item_Concept)
    MATCH (scc:SimpleComponent_Concept)
    MATCH (comc:Component_Concept)
    WITH [tagc, itc, scc, comc] AS ConTAGIN
    UNWIND ConTAGIN as conTAGIN
    MATCH (tag:Tag)
    CREATE (tag)-[rtag:is_a]->(conTAGIN)
    """

    queryRelationInheritanceTask = """
    MATCH (tasc:Task_Concept)
    MATCH (itc:Item_Concept)
    MATCH (iec:IntellectualEntity_Concept)
    WITH [tasc, itc, iec] AS ConTASKIN
    UNWIND ConTASKIN as conTASKIN
    MATCH (tas:Task)
    CREATE (tas)-[rtask:is_a]->(conTASKIN)
    """

    queryRelationInheritanceTaskContainer = """
    MATCH (coc:Container_Concept)
    MATCH (taskcc:TaskContainer_Concept)
    WITH [coc, taskcc] AS ConTASKCIN
    UNWIND ConTASKCIN as conTASKCIN
    MATCH (taskc:TaskContainer)
    CREATE (taskc)-[rtaskc:is_a]->(conTASKCIN)
    """

    queryRelationInheritanceWeblog = """
    MATCH (coc:Container_Concept)
    MATCH (wbc:Weblog_Concept)
    WITH [coc, wbc] AS ConWBC
    UNWIND ConWBC as conWBC
    MATCH (wb:Weblog)
    CREATE (wb)-[rwb:is_a]->(conWBC)
    """

    queryRelationInheritanceWiki = """
    MATCH (coc:Container_Concept)
    MATCH (wikic:Wiki_Concept)
    WITH [coc, wikic] AS ConWIKIIN
    UNWIND ConWIKIIN as conWIKIIN
    MATCH (wiki:Wiki)
    CREATE (wiki)-[rwiki:is_a]->(conWIKIIN)
    """

    queryRelationInheritanceWikiPage = """
    MATCH (wikipc:WikiPage_Concept)
    MATCH (itc:Item_Concept)
    MATCH (iec:IntellectualEntity_Concept)
    WITH [wikipc, itc, iec] AS ConWIKIPIN
    UNWIND ConWIKIPIN as conWIKIPIN
    MATCH (wikip:WikiPage)
    CREATE (wikip)-[rwikip:is_a]->(conWIKIPIN)
    """

    #Execution Cypher Queries
    graph.execute_write_query(queryRelationInheritanceAccount, "neo4j")
    graph.execute_write_query(queryRelationInheritanceAttachment, "neo4j")
    graph.execute_write_query(queryRelationInheritanceBlogPost, "neo4j")
    graph.execute_write_query(queryRelationInheritanceBoardPost, "neo4j")
    graph.execute_write_query(queryRelationInheritanceComment, "neo4j")
    graph.execute_write_query(queryRelationInheritanceEvent, "neo4j")
    graph.execute_write_query(queryRelationInheritanceFile, "neo4j")
    graph.execute_write_query(queryRelationInheritanceFileLibrary, "neo4j")
    graph.execute_write_query(queryRelationInheritanceFolder, "neo4j")
    graph.execute_write_query(queryRelationInheritanceFollow, "neo4j")
    graph.execute_write_query(queryRelationInheritanceGroupWorkspace, "neo4j")
    graph.execute_write_query(queryRelationInheritanceLike, "neo4j")
    graph.execute_write_query(queryRelationInheritanceMessageBoard, "neo4j")
    graph.execute_write_query(queryRelationInheritanceMicroblog, "neo4j")
    graph.execute_write_query(queryRelationInheritanceMicroblogPost, "neo4j")
    graph.execute_write_query(queryRelationInheritanceOrganisation, "neo4j")
    graph.execute_write_query(queryRelationInheritancePerson, "neo4j")
    graph.execute_write_query(queryRelationInheritanceSocialProfile, "neo4j")
    graph.execute_write_query(queryRelationInheritanceSystem, "neo4j")
    graph.execute_write_query(queryRelationInheritanceTag, "neo4j")
    graph.execute_write_query(queryRelationInheritanceTask, "neo4j")
    graph.execute_write_query(queryRelationInheritanceTaskContainer, "neo4j")
    graph.execute_write_query(queryRelationInheritanceWeblog, "neo4j")
    graph.execute_write_query(queryRelationInheritanceWiki, "neo4j")
    graph.execute_write_query(queryRelationInheritanceWikiPage, "neo4j")

    ("ProcessEvent finished --- %s seconds ---" % (time.time() - start_time))
    logging.info(("Process finished --- %s seconds ---" % (time.time() - start_time)))

#Main Method
if __name__ == "__main__":
    creatingAbstractRelation()
