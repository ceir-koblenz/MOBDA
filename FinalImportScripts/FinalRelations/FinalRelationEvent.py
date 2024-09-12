#Library für Neointerface für die Verbindung zu Neo4j
import neointerface
#Verbindung zu Neo4j 
neodb = neointerface.NeoInterface(host="neo4j://ma-lschloemer.bas.uni-koblenz.de:7687" , credentials=("neo4j", "neo4jneo4j"))

#Cypher Queries für Relations
queryRelationEvent_event_affects_item_AttachmentID = """
//Relation Attachment<-> Event (BoardPost, Task)
MATCH (att:Attachment)
MATCH (ev:Event)
WHERE att.ID = ev.ITEM_UUID 
MERGE (ev)-[repby:event_affects_item {cardinality: "exactly 1"}]->(att)
MERGE (att)-[raha:item_affected_by_event]->(ev)
"""
queryRelationEvent_event_affects_item_AttachmentMATCHID = """
//2. Step Relation Attachment<-> Event (WikiPage)
MATCH (att:Attachment)
MATCH (ev:Event)
WHERE att.MATCH_ID = ev.ITEM_UUID 
MERGE (ev)-[repby:event_affects_item {cardinality: "exactly 1"}]->(att)
MERGE (att)-[raha:item_affected_by_event]->(ev)
"""

queryRelationEvent_event_affects_item_BlogPost = """
//Relation BlogPost <-> Event
MATCH (b:BlogPost)
MATCH (ev:Event)
WHERE b.ID = ev.ITEM_UUID AND ev.SOURCE_ID = 2
MERGE (ev)-[repby:event_affects_item {cardinality: "exactly 1"}]->(b)
MERGE (b)-[raha:item_affected_by_event]->(ev)
"""

queryRelationEvent_event_affects_item_BoardPost = """
//Relation BoardPost <-> Event
MATCH (bp:BoardPost)
MATCH (ev:Event)
WHERE bp.ID = ev.ITEM_UUID AND ev.SOURCE_ID = 6
MERGE (ev)-[repby:event_affects_item {cardinality: "exactly 1"}]->(bp)
MERGE (bp)-[raha:item_affected_by_event]->(ev)
"""

queryRelationEvent_event_affects_item_CommentBBS = """
//1. Step Relation Comment<-> Event (BlogPost, BoardPost, SocialProfile)
MATCH (com:Comment)
MATCH (ev:Event)
WHERE com.ID = ev.ITEM_UUID AND (ev.SOURCE_ID = 2 OR ev.SOURCE_ID = 6 OR ev.SOURCE_ID = 10)
MERGE (ev)-[repby:event_affects_item {cardinality: "exactly 1"}]->(com)
MERGE (com)-[raha:item_affected_by_event]->(ev)
"""
queryRelationEvent_event_affects_item_CommentM = """
//2. StepRelation Comment<-> Event (MicroblogPost)
MATCH (com:Comment)
MATCH (ev:Event)
WHERE com.ITEM_ID = ev.ITEM_UUID 
MERGE (ev)-[repby:event_affects_item {cardinality: "exactly 1"}]->(com)
MERGE (com)-[raha:item_affected_by_event]->(ev)
"""
queryRelationEvent_event_affects_item_CommentT = """ 
//3. Step Relation Comment<-> Event  (Task)
MATCH (com:Comment)
MATCH (ev:Event)
WHERE com.ID = ev.ITEM_UUID AND ev.SOURCE_ID = 1 AND ev.TITLE <> 'activity.entry.*'
MERGE (ev)-[repby:event_affects_item {cardinality: "exactly 1"}]->(com)
MERGE (com)-[raha:item_affected_by_event]->(ev)
"""
queryRelationEvent_event_affects_item_CommentF = """
//4. StepRelation Comment<-> Event (File)
MATCH (com:Comment)
MATCH (ev:Event)
WHERE com.MATCH_COMMENT_ID = ev.ITEM_UUID AND ev.SOURCE_ID = 5
MERGE (ev)-[repby:event_affects_item {cardinality: "exactly 1"}]->(com)
MERGE (com)-[raha:item_affected_by_event]->(ev)
"""
queryRelationEvent_event_affects_item_CommentW = """
//5. StepRelation Comment<-> Event (WikiPage)
MATCH (com:Comment)
MATCH (ev:Event)
WHERE com.MATCH_COM_ID = ev.ITEM_UUID 
MERGE (ev)-[repby:event_affects_item {cardinality: "exactly 1"}]->(com)
MERGE (com)-[raha:item_affected_by_event]->(ev)
"""
queryRelationEvent_event_affects_item_File = """
//Relation File <-> Event
MATCH (fi:File)
MATCH (ev:Event)
WHERE fi.MATCH_MEDIA_ID = ev.ITEM_UUID AND ev.SOURCE_ID = 5
MERGE (ev)-[repby:event_affects_item {cardinality: "exactly 1"}]->(fi)
MERGE (fi)-[raha:item_affected_by_event]->(ev)
"""
queryRelationEvent_event_affects_item_Folder = """
//Relation Folder <-> Event
MATCH (fo:Folder)
MATCH (ev:Event)
WHERE fo.MATCH_FOLDER_ID = ev.ITEM_UUID AND ev.SOURCE_ID = 5
MERGE (ev)-[repby:event_affects_item {cardinality: "exactly 1"}]->(fo)
MERGE (fo)-[raha:item_affected_by_event]->(ev)
"""

queryRelationEvent_event_affects_item_FollowBP = """
//1. Step Relation Follow <-> Event BoardPost X
MATCH (fol:Follow)
MATCH (ev:Event)
WHERE fol.TOPICID= ev.ITEM_UUID AND ev.SOURCE_ID = 6 AND ev.TITLE =~ ".*follow.*"
MERGE (ev)-[repby:event_affects_item {cardinality: "exactly 1"}]->(fol)
MERGE (fol)-[raha:item_affected_by_event]->(ev)
"""
queryRelationEvent_event_affects_item_FollowSP = """
//2. Step Relation Follow <-> Event SocialProflie
MATCH (fol:Follow)
MATCH (ev:Event)
WHERE fol.EXID = ev.UUID AND ev.TITLE =~ ".*follow.*"
MERGE (ev)-[repby:event_affects_item {cardinality: "exactly 1"}]->(fol)
MERGE (fol)-[raha:item_affected_by_event]->(ev)
"""
queryRelationEvent_event_affects_item_FollowT = """
//3. Step Relation Follow <-> Event Task X
MATCH (fol:Follow)
MATCH (ev:Event)
WHERE  fol.NODEUUID = ev.ITEM_UUID AND ev.TITLE =~ ".*follow.*" AND ev.UUID = fol.EXID
MERGE (ev)-[repby:event_affects_item {cardinality: "exactly 1"}]->(fol)
MERGE (fol)-[raha:item_affected_by_event]->(ev)
"""
queryRelationEvent_event_affects_item_FollowFI = """
//4. Step Relation Follow <-> Event File X
MATCH (fol:Follow)
MATCH (ev:Event)
WHERE fol.MATCH_MEDIA_ID = ev.ITEM_UUID AND ev.TITLE =~ "files.file.notification.*" AND ev.UUID = fol.DIRECTORY_ID
MERGE (ev)-[repby:event_affects_item {cardinality: "exactly 1"}]->(fol)
MERGE (fol)-[raha:item_affected_by_event]->(ev)
"""
queryRelationEvent_event_affects_item_FollowFO = """
//5. Step Relation Follow <-> Event Folder X
MATCH (fol:Follow)
MATCH (ev:Event)
WHERE fol.MATCH_FOLDER_ID = ev.ITEM_UUID AND ev.TITLE =~ 'files.collection.notification.*' AND ev.UUID = fol.DIRECTORY_ID
MERGE (ev)-[repby:event_affects_item {cardinality: "exactly 1"}]->(fol)
MERGE (fol)-[raha:item_affected_by_event]->(ev)
"""
queryRelationEvent_event_affects_item_FollowW = """
//6. Step Relation Follow <-> Event Wiki X
MATCH (fol:Follow)
MATCH (ev:Event)
WHERE fol.MATCH_MEDIA_ID = ev.ITEM_UUID AND ev.TITLE =~ 'wiki.*.notification.*' AND ev.UUID = fol.DIRECTORY_ID
MERGE (ev)-[repby:event_affects_item {cardinality: "exactly 1"}]->(fol)
MERGE (fol)-[raha:item_affected_by_event]->(ev)
"""
queryRelationEvent_event_affects_item_LikeBL= """
//1. Step Relation Like<-> Event BlogPost X
MATCH (lik:Like)
MATCH (ev:Event)
WHERE ev.ITEM_UUID = lik.ENTRYID AND (ev.TITLE =~ '.*recommended' OR ev.TITLE =~ '.*voted') AND ev.UUID = lik.EXTID
MERGE (ev)-[repby:event_affects_item {cardinality: "exactly 1"}]->(lik)
MERGE (lik)-[raha:item_affected_by_event]->(ev) 
"""

queryRelationEvent_event_affects_item_LikeBO = """
//2. Step Relation Like<-> Event BoardPost
MATCH (lik:Like)
MATCH (ev:Event)
WHERE lik.NODEID = ev.ITEM_UUID AND (ev.TITLE = 'forum.topic.unrecommended' OR ev.TITLE = 'forum.topic.recommended') AND ev.UUID = lik.EXID
MERGE (ev)-[repby:event_affects_item {cardinality: "exactly 1"}]->(lik)
MERGE (lik)-[raha:item_affected_by_event]->(ev) 

"""

queryRelationEvent_event_affects_item_LikeBOC = """
//3. Step Relation Like<-> Event BoardPostComment, MicroblogPost
MATCH (lik:Like)
MATCH (ev:Event)
WHERE lik.ENTRY_ID = ev.ITEM_UUID AND ev.TITLE =~ '.*recommend.*' AND ev.UUID = lik.EXID
MERGE (ev)-[repby:event_affects_item {cardinality: "exactly 1"}]->(lik)
MERGE (lik)-[raha:item_affected_by_event]->(ev)
"""

queryRelationEvent_event_affects_item_LikeF = """
//4. Step Relation Like<-> Event Files
MATCH (lik:Like)
MATCH (ev:Event)
WHERE  lik.MATCH_MEDIA_ID = ev.ITEM_UUID AND ev.TITLE =~ '.*recommend.*' AND ev.UUID = lik.DIRECTORY_ID
MERGE (ev)-[repby:event_affects_item {cardinality: "exactly 1"}]->(lik)
MERGE (lik)-[raha:item_affected_by_event]->(ev) 
"""

queryRelationEvent_event_affects_item_MicroblogPost = """
//Relation MicroblogPost <-> Event
MATCH (mbp:MicroblogPost)
MATCH (ev:Event)
WHERE mbp.ID = ev.ITEM_UUID AND ev.TITLE = 'community.wallpost.created'
MERGE (ev)-[repby:event_affects_item {cardinality: "exactly 1"}]->(mbp)
MERGE (mbp)-[raha:item_affected_by_event]->(ev)
"""

queryRelationEvent_event_affects_item_SocialProfile = """
//Relation SocialProfile <-> Event
MATCH (sop:SocialProfile)
MATCH (ev:Event)
WHERE sop.EXID = ev.ITEM_UUID AND ev.SOURCE_ID = 10 
MERGE (ev)-[repby:event_affects_item {cardinality: "exactly 1"}]->(sop)
MERGE (sop)-[raha:item_affected_by_event]->(ev)
"""
queryRelationEvent_event_affects_item_Task = """
//Relation Task <-> Event
MATCH (ta:Task)
MATCH (ev:Event)
WHERE ta.ID = ev.ITEM_UUID AND ev.SOURCE_ID = 1 
MERGE (ev)-[repby:event_affects_item {cardinality: "exactly 1"}]->(ta)
MERGE (ta)-[raha:item_affected_by_event]->(ev)
"""

queryRelationEvent_event_affects_item_WikiPage = """
//Relation WikiPage <-> Event
MATCH (wipa:WikiPage)
MATCH (ev:Event)
WHERE wipa.MATCH_MEDIA_ID = ev.ITEM_UUID 
MERGE (ev)-[repby:event_affects_item {cardinality: "exactly 1"}]->(wipa)
MERGE (wipa)-[raha:item_affected_by_event]->(ev)
"""

#Ausführung der Cypher Skripte mit NeoInterface
neodb.query(queryRelationEvent_event_affects_item_AttachmentID)
neodb.query(queryRelationEvent_event_affects_item_AttachmentMATCHID)
neodb.query(queryRelationEvent_event_affects_item_BlogPost)
neodb.query(queryRelationEvent_event_affects_item_BoardPost)
neodb.query(queryRelationEvent_event_affects_item_CommentBBS)
neodb.query(queryRelationEvent_event_affects_item_CommentM)
neodb.query(queryRelationEvent_event_affects_item_CommentT)
neodb.query(queryRelationEvent_event_affects_item_CommentF)
neodb.query(queryRelationEvent_event_affects_item_CommentW)
neodb.query(queryRelationEvent_event_affects_item_File)
neodb.query(queryRelationEvent_event_affects_item_Folder)
neodb.query(queryRelationEvent_event_affects_item_FollowBP)
neodb.query(queryRelationEvent_event_affects_item_FollowSP)
neodb.query(queryRelationEvent_event_affects_item_FollowT)
neodb.query(queryRelationEvent_event_affects_item_FollowFI)
neodb.query(queryRelationEvent_event_affects_item_FollowFO)
neodb.query(queryRelationEvent_event_affects_item_FollowW)
neodb.query(queryRelationEvent_event_affects_item_LikeBO)
neodb.query(queryRelationEvent_event_affects_item_LikeBL)
neodb.query(queryRelationEvent_event_affects_item_LikeBOC)
neodb.query(queryRelationEvent_event_affects_item_LikeF)
neodb.query(queryRelationEvent_event_affects_item_MicroblogPost)
neodb.query(queryRelationEvent_event_affects_item_SocialProfile)
neodb.query(queryRelationEvent_event_affects_item_Task)
neodb.query(queryRelationEvent_event_affects_item_WikiPage)