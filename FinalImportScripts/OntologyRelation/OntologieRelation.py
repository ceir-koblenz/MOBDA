#Library für Neointerface für die Verbindung zu Neo4j
import neointerface
#Verbindung zu Neo4j 
neodb = neointerface.NeoInterface(host="neo4j://ma-lschloemer.bas.uni-koblenz.de:7687" , credentials=("neo4j", "neo4jneo4j"))

#Cypher Queries für Relations

queryRelationInheritanceAccount = """
MATCH (acc:Account_Concept)
MATCH (ac:Account)
MERGE (ac)-[rac:is_a]->(acc)
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
MERGE (at)-[rat:is_a]->(conATIN)
"""
queryRelationInheritanceBlogPost = """
//Relations is_a zwischen child Nodes und Parent Nodes_Concepts
MATCH (bc:BlogPost_Concept)
MATCH (iec:IntellectualEntity_Concept)
MATCH (itc:Item_Concept)
WITH [bc, itc, iec] AS ConBGIN 
UNWIND ConBGIN as conBGIN
MATCH (b:BlogPost)
MERGE (b)-[rba:is_a]->(conBGIN)
"""

queryRelationInheritanceBoardPost = """
//Inheritance of BoadPOst
MATCH (bpc:BoardPost_Concept)
MATCH (itc:Item_Concept)
MATCH (iec:IntellectualEntity_Concept)
WITH [bpc, itc, iec] AS ConBPIN
UNWIND ConBPIN as conBPIN
MATCH (bp:BoardPost)
MERGE (bp)-[rbp:is_a]->(conBPIN)
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
MERGE (com)-[rcom:is_a]->(conCOIN)
"""

queryRelationInheritanceEvent = """
MATCH (evc:Event_Concept)
MATCH (ev:Event)
MERGE (ev)-[re:is_a]->(evc)
"""

queryRelationInheritanceFile = """
//Inheritance of File 
MATCH (fic:File_Concept)
MATCH (itc:Item_Concept)
MATCH (iec:IntellectualEntity_Concept)
WITH [fic, itc, iec] AS ConFIIN
UNWIND ConFIIN as conFIIN
MATCH (fil:File)
MERGE (fil)-[rfil:is_a]->(conFIIN)
"""

queryRelationInheritanceFileLibrary = """
MATCH (coc:Container_Concept)
MATCH (filic:FileLibrary_Concept)
WITH [coc, filic] AS ConFILIC
UNWIND ConFILIC as conFILIC
MATCH (fili:FileLibrary)
MERGE (fili)-[rfili:is_a]->(conFILIC)
"""

queryRelationInheritanceFolder = """
//Inheritance of Folder
MATCH (foc:Folder_Concept)
MATCH (itc:Item_Concept)
MATCH (iec:IntellectualEntity_Concept)
WITH [foc, itc, iec] AS ConFOCIN
UNWIND ConFOCIN as conFOCIN
MATCH (fo:Folder)
MERGE (fo)-[rfoc:is_a]->(conFOCIN)
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
MERGE (fol)-[rfol:is_a]->(conFOLIN)
"""

queryRelationInheritanceGroupWorkspace = """
MATCH (spa:Space_Concept)
MATCH (gwsc:GroupWorkspace_Concept)
WITH [gwsc, spa] AS ConGWSIN 
UNWIND ConGWSIN as conGWSIN
MATCH (gws:GroupWorkspace)
MERGE (gws)-[rgws:is_a]->(conGWSIN)
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
MERGE (like)-[rlike:is_a]->(conLIKIN)
"""

queryRelationInheritanceMessageBoard = """
//Inheritance of MessageBoard
MATCH (coc:Container_Concept)
MATCH (mbc:MessageBoard_Concept)
WITH [coc, mbc] AS ConMBCIN
UNWIND ConMBCIN as conMBCIN
MATCH (mb:MessageBoard)
MERGE (mb)-[rmb:is_a]->(conMBCIN)
"""

queryRelationInheritanceMicroblog = """
MATCH (coc:Container_Concept)
MATCH (mbc:Microblog_Concept)
WITH [coc, mbc] AS ConMBC
UNWIND ConMBC as conMBC
MATCH (mb:Microblog)
MERGE (mb)-[rmb:is_a]->(conMBC)
"""

queryRelationInheritanceMicroblogPost = """
MATCH (mbpc:MicroblogPost_Concept)
MATCH (itc:Item_Concept)
MATCH (iec:IntellectualEntity_Concept)
WITH [mbpc, itc, iec] AS ConMBPIN
UNWIND ConMBPIN as conMBPIN
MATCH (mbp:MicroblogPost)
MERGE (mbp)-[rfil:is_a]->(conMBPIN)
"""

queryRelationInheritanceOrganisation = """
MATCH (agc:Agent_Concept)
MATCH (ogc:Organisation_Concept)
WITH [ogc, agc] AS ConORCIN
UNWIND ConORCIN as conORCIN
MATCH (og:Organisation)
MERGE (og)-[rog:is_a]->(conORCIN)
"""

queryRelationInheritancePerson = """
MATCH (agc:Agent_Concept)
MATCH (pec:Person_Concept)
WITH [agc, pec] AS ConPERIN
UNWIND ConPERIN as conPERIN
MATCH (pe:Person)
MERGE (pe)-[rpe:is_a]->(conPERIN)
"""

queryRelationInheritanceSocialProfile = """
//Inheritance of SocialProfile
MATCH (sopc:SocialProfile_Concept)
MATCH (itc:Item_Concept)
MATCH (iec:IntellectualEntity_Concept)
WITH [sopc, itc, iec] AS ConSOPIN
UNWIND ConSOPIN as conSOPIN
MATCH (sop:SocialProfile)
MERGE (sop)-[rsop:is_a]->(conSOPIN)
"""

queryRelationInheritanceSystem = """
MATCH (syc:System_Concept)
MATCH (sy:System)
MERGE (sy)-[rsy:is_a]->(syc)
"""
queryRelationInheritanceTag = """
MATCH (tagc:Tag_Concept)
MATCH (itc:Item_Concept)
MATCH (scc:SimpleComponent_Concept)
MATCH (comc:Component_Concept)
WITH [tagc, itc, scc, comc] AS ConTAGIN
UNWIND ConTAGIN as conTAGIN
MATCH (tag:Tag)
MERGE (tag)-[rtag:is_a]->(conTAGIN)
"""

queryRelationInheritanceTask = """
MATCH (tasc:Task_Concept)
MATCH (itc:Item_Concept)
MATCH (iec:IntellectualEntity_Concept)
WITH [tasc, itc, iec] AS ConTASKIN
UNWIND ConTASKIN as conTASKIN
MATCH (tas:Task)
MERGE (tas)-[rtask:is_a]->(conTASKIN)
"""

queryRelationInheritanceTaskContainer = """
MATCH (coc:Container_Concept)
MATCH (taskcc:TaskContainer_Concept)
WITH [coc, taskcc] AS ConTASKCIN
UNWIND ConTASKCIN as conTASKCIN
MATCH (taskc:TaskContainer)
MERGE (taskc)-[rtaskc:is_a]->(conTASKCIN)
"""

queryRelationInheritanceWeblog = """
MATCH (coc:Container_Concept)
MATCH (wbc:Weblog_Concept)
WITH [coc, wbc] AS ConWBC
UNWIND ConWBC as conWBC
MATCH (wb:Weblog)
MERGE (wb)-[rwb:is_a]->(conWBC)
"""

queryRelationInheritanceWiki = """
MATCH (coc:Container_Concept)
MATCH (wikic:Wiki_Concept)
WITH [coc, wikic] AS ConWIKIIN
UNWIND ConWIKIIN as conWIKIIN
MATCH (wiki:Wiki)
MERGE (wiki)-[rwiki:is_a]->(conWIKIIN)
"""

queryRelationInheritanceWikiPage = """
MATCH (wikipc:WikiPage_Concept)
MATCH (itc:Item_Concept)
MATCH (iec:IntellectualEntity_Concept)
WITH [wikipc, itc, iec] AS ConWIKIPIN
UNWIND ConWIKIPIN as conWIKIPIN
MATCH (wikip:WikiPage)
MERGE (wikip)-[rwikip:is_a]->(conWIKIPIN)
"""

#Ausführen der Cypher Queries
neodb.query(queryRelationInheritanceAccount)
neodb.query(queryRelationInheritanceAttachment)
neodb.query(queryRelationInheritanceBlogPost)
neodb.query(queryRelationInheritanceBoardPost)
neodb.query(queryRelationInheritanceComment)
neodb.query(queryRelationInheritanceEvent)
neodb.query(queryRelationInheritanceFile)
neodb.query(queryRelationInheritanceFileLibrary)
neodb.query(queryRelationInheritanceFolder)
neodb.query(queryRelationInheritanceFollow)
neodb.query(queryRelationInheritanceGroupWorkspace)
neodb.query(queryRelationInheritanceLike)
neodb.query(queryRelationInheritanceMessageBoard)
neodb.query(queryRelationInheritanceMicroblog)
neodb.query(queryRelationInheritanceMicroblogPost)
neodb.query(queryRelationInheritanceOrganisation)
neodb.query(queryRelationInheritancePerson)
neodb.query(queryRelationInheritanceSocialProfile)
neodb.query(queryRelationInheritanceSystem)
neodb.query(queryRelationInheritanceTag)
neodb.query(queryRelationInheritanceTask)
neodb.query(queryRelationInheritanceTaskContainer)
neodb.query(queryRelationInheritanceWeblog)
neodb.query(queryRelationInheritanceWiki)
neodb.query(queryRelationInheritanceWikiPage)
