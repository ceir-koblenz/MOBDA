#Library für Neointerface für die Verbindung zu Neo4j
import neointerface
#Verbindung zu Neo4j 
neodb = neointerface.NeoInterface(host="neo4j://ma-lschloemer.bas.uni-koblenz.de:7687" , credentials=("neo4j", "neo4jneo4j"))

#Cypher Queries für Relations
queryRelationAccount_account_contained_in_system_System = """
//Relation Account <-> System
MATCH (acc:Account)
MATCH (sy:System)
MERGE (acc)-[racis:account_contained_in_system {cardinality: "exactly 1"}]->(sy)
MERGE (sy)-[rsca:system_contains_account]->(acc)
"""
queryRelationAccount_account_created_item_AttachmentAll = """
//1. Step Relation Account <-> Attachment
MATCH (acc:Account)
MATCH (att:Attachment)
WHERE acc.PROF_GUID = att.EXID 
//WHERE Clause for WikiPage missing
MERGE (acc)-[raci:account_created_item]->(att)
MERGE (att)-[ricba:item_created_by_account]->(acc)
"""

queryRelationAccount_account_created_item_AttachmentallWikipage = """
//2. Step Relation Account <-> Attachment (WikikPage)
MATCH (acc:Account)
MATCH (att:Attachment)
WHERE acc.PROF_GUID = att.DIRECTORY_ID
MERGE (acc)-[raci:account_created_item]->(att)
MERGE (att)-[ricba:item_created_by_account]->(acc)
"""

queryRelationAccount_account_created_item_BlogPost = """
//Relation Account <-> BlogPost
MATCH (acc:Account)
MATCH (bp:BlogPost)
WHERE acc.PROF_GUID = bp.EXTID
MERGE (acc)-[raci:account_created_item]->(bp)
MERGE (bp)-[ricba:item_created_by_account]->(acc)
"""

queryRelationAccount_account_created_item_BoardPost = """
MATCH (acc:Account)
MATCH (bop:BoardPost)
WHERE acc.PROF_GUID = bop.EXID
MERGE (acc)-[raci:account_created_item]->(bop)
MERGE (bop)-[ricba:item_created_by_account]->(acc)
"""
queryRelationAccount_account_created_item_CommentEXID = """
//1. Step Relation Account <-> Comment (EXID)
MATCH (acc:Account)
MATCH (comm:Comment)
WHERE acc.PROF_GUID = comm.EXID 
//OR acc.PROF_GUID = comm.EXTID 
//WHERE Clause for WikiPage and Files missing
MERGE (acc)-[raci:account_created_item]->(comm)
MERGE (comm)-[ricba:item_created_by_account]->(acc)
"""
queryRelationAccount_account_created_item_CommentEXTID = """
//2.Step Relation Account <-> Comment (extid/BlogPost)
MATCH (acc:Account)
MATCH (comm:Comment)
WHERE acc.PROF_GUID = comm.EXTID 
MERGE (acc)-[raci:account_created_item]->(comm)
MERGE (comm)-[ricba:item_created_by_account]->(acc)
"""
queryRelationAccount_account_created_item_CommentDIRECTORYID = """
//3.Step Relation Account <-> Comment (Directory_id: WikiPage, File)
MATCH (acc:Account)
MATCH (comm:Comment)
WHERE acc.PROF_GUID = comm.DIRECTORY_ID
MERGE (acc)-[raci:account_created_item]->(comm)
MERGE (comm)-[ricba:item_created_by_account]->(acc)
"""
queryRelationAccount_account_created_item_File = """
//Relation Account <-> File
MATCH (acc:Account)
MATCH (fi:File)
WHERE acc.PROF_GUID = fi.DIRECTORY_ID
MERGE (acc)-[raci:account_created_item]->(fi)
MERGE (fi)-[ricba:item_created_by_account]->(acc)
"""

queryRelationAccount_account_created_item_FollowEXID = """
//1. Step Relation Account <-> Follow (EXID)
MATCH (acc:Account)
MATCH (foll:Follow)
WHERE acc.PROF_GUID = foll.EXID  
MERGE (acc)-[raci:account_created_item]->(foll)
MERGE (foll)-[ricba:item_created_by_account]->(acc)
"""

queryRelationAccount_account_created_item_FollowDIRECTORYID = """
//2. Step Relation Account <-> Follow (DIRECTORY_ID)
MATCH (acc:Account)
MATCH (foll:Follow)
WHERE acc.PROF_GUID = foll.DIRECTORY_ID  
MERGE (acc)-[raci:account_created_item]->(foll)
MERGE (foll)-[ricba:item_created_by_account]->(acc)
"""
queryRelationAccount_account_created_item_LikeEXTID = """
//1. Step Relation Account <-> Like extid
MATCH (acc:Account)
MATCH (like:Like)
WHERE acc.PROF_GUID = like.EXTID 
MERGE (acc)-[raci:account_created_item]->(like)
MERGE (like)-[ricba:item_created_by_account]->(acc)
"""

queryRelationAccount_account_created_item_LikeEXID = """
//2. Step Relation Account <-> Like Exid 
MATCH (acc:Account)
MATCH (like:Like)
WHERE acc.PROF_GUID = like.EXID
MERGE (acc)-[raci:account_created_item]->(like)
MERGE (like)-[ricba:item_created_by_account]->(acc)
"""

queryRelationAccount_account_created_item_LikeDIRECTORYID = """
//3. Step Relation Account <-> Like Directory_id
MATCH (acc:Account)
MATCH (like:Like)
WHERE acc.PROF_GUID = like.DIRECTORY_ID 
MERGE (acc)-[raci:account_created_item]->(like)
MERGE (like)-[ricba:item_created_by_account]->(acc)
"""
queryRelationAccount_account_created_item_MicroblogPost = """
MATCH (acc:Account)
MATCH (mbp:MicroblogPost)
WHERE acc.PROF_GUID = mbp.EXID
MERGE (acc)-[raci:account_created_item]->(mbp)
MERGE (mbp)-[ricba:item_created_by_account]->(acc)
"""
queryRelationAccount_account_created_item_SocialProfile = """
//Realation Account <-> SocialProfile
MATCH (acc:Account)
MATCH (socp:SocialProfile)
WHERE acc.PROF_GUID = socp.EXID
MERGE (acc)-[raci:account_created_item]->(socp)
MERGE (socp)-[ricba:item_created_by_account]->(acc)
"""

queryRelationAccount_account_created_item_TagEXTID = """
//1. Step Relation Account <-> Tag extid -> BlogPostTag
MATCH (acc:Account)
MATCH (tag:Tag)
WHERE acc.PROF_GUID = tag.EXTID 
MERGE (acc)-[raci:account_created_item]->(tag)
MERGE (tag)-[ricba:item_created_by_account]->(acc) """

queryRelationAccount_account_created_item_TagEXID = """ 
//2. Step Relation Account <-> Tag exid-> BoardPost, Tag
MATCH (acc:Account)
MATCH (tag:Tag)
WHERE  acc.PROF_GUID = tag.EXID
MERGE (acc)-[raci:account_created_item]->(tag)
MERGE (tag)-[ricba:item_created_by_account]->(acc)
"""

queryRelationAccount_account_created_item_TagPROFGUID = """
//3. Step Relation Account <-> Tag prof_guid -> Task
MATCH (acc:Account)
MATCH (tag:Tag)
WHERE  acc.PROF_GUID = tag.PROF_GUID
MERGE (acc)-[raci:account_created_item]->(tag)
MERGE (tag)-[ricba:item_created_by_account]->(acc) """

queryRelationAccount_account_created_item_Task = """
//Realation Account <-> Task
MATCH (acc:Account)
MATCH (task:Task)
WHERE acc.PROF_GUID = task.EXID
MERGE (acc)-[raci:account_created_item]->(task)
MERGE (task)-[ricba:item_created_by_account]->(acc)
"""
queryRelationAccount_account_created_item_WikiPage = """
//Relation Account <-> WikiPage
MATCH (acc:Account)
MATCH (wipo:WikiPage)
WHERE acc.PROF_GUID = wipo.DIRECTORY_ID
MERGE (acc)-[raci:account_created_item]->(wipo)
MERGE (wipo)-[ricba:item_created_by_account]->(acc)
"""

queryRelationAccount_account_has_social_profile_SocialProfile = """
//Realation Account <-> SocialProfile has SocialProflie
MATCH (acc:Account)
MATCH (socp:SocialProfile)
WHERE acc.PROF_GUID = socp.EXID
MERGE (acc)-[rahsp:account_has_social_profile {cardinality: "maximal 1" }]->(socp)
MERGE (socp)-[rspoa:social_profile_of_account]->(acc)
"""
queryRelationAccount_account_is_member_of_space_GroupWorkspace = """
//Realation Account <-> GroupWorkspace Has Member
MATCH (acc:Account)
MATCH (gws:GroupWorkspace)
WHERE acc.PROF_GUID = gws.DIRECTORY_UUID
MERGE (acc)-[raimos:account_is_member_of_space]->(gws)
MERGE (gws)-[rshma:space_has_member_account]->(acc)
"""
queryRelationAccount_account_of_agent_Organisation = """
//Relation Account <-> Organisation
MATCH (acc:Account)
MATCH (org:Organisation)
MERGE (acc)-[raoa:account_of_agent {cardinality: "exactly 1"}]->(org)
MERGE (org)-[raha:agent_has_account]->(acc)
"""
queryRelationAccount_account_of_agent_Person = """
//Relation Account <-> Person
MATCH (acc:Account)
MATCH (per:Person)
WHERE acc.PROF_GUID = per.PROF_GUID
MERGE (acc)-[raoa:account_of_agent {cardinality: "exactly 1"}]->(per)
MERGE (org)-[raha:agent_has_account]->(per)
"""
queryRelationAccount_account_performed_event_Event25 = """
//1. StepRelation Account <-> Event
MATCH (acc:Account)
MATCH (ev:Event)
WHERE acc.PROF_GUID = ev.UUID AND ev.ID <=2500000
MERGE (ev)-[repby:event_performed_by_account {cardinality: "exactly 1"}]->(acc)
MERGE (acc)-[raha:account_performed_event]->(ev)
"""
queryRelationAccount_account_performed_event_Event2560= """
//2.Step Relation Account <-> Event
MATCH (acc:Account)
MATCH (ev:Event)
WHERE acc.PROF_GUID = ev.UUID AND ev.ID >2500000 AND ev.ID <6000000
MERGE (ev)-[repby:event_performed_by_account {cardinality: "exactly 1"}]->(acc)
MERGE (acc)-[raha:account_performed_event]->(ev)"""

queryRelationAccount_account_performed_event_Event60= """
//3. Step Relation Account <-> Event
MATCH (acc:Account)
MATCH (ev:Event)
WHERE acc.PROF_GUID = ev.UUID AND ev.ID >= 6000000
MERGE (ev)-[repby:event_performed_by_account {cardinality: "exactly 1"}]->(acc)
MERGE (acc)-[raha:account_performed_event]->(ev)
"""

neodb.query(queryRelationAccount_account_contained_in_system_System)
neodb.query(queryRelationAccount_account_created_item_AttachmentAll)
neodb.query(queryRelationAccount_account_created_item_AttachmentallWikipage)
neodb.query(queryRelationAccount_account_created_item_BlogPost)
neodb.query(queryRelationAccount_account_created_item_BoardPost)
neodb.query(queryRelationAccount_account_created_item_CommentEXID)
neodb.query(queryRelationAccount_account_created_item_CommentEXTID)
neodb.query(queryRelationAccount_account_created_item_CommentDIRECTORYID)
neodb.query(queryRelationAccount_account_created_item_File)
neodb.query(queryRelationAccount_account_created_item_FollowEXID)
neodb.query(queryRelationAccount_account_created_item_FollowDIRECTORYID)
neodb.query(queryRelationAccount_account_created_item_LikeEXTID)
neodb.query(queryRelationAccount_account_created_item_LikeEXID)
neodb.query(queryRelationAccount_account_created_item_LikeDIRECTORYID)
neodb.query(queryRelationAccount_account_created_item_MicroblogPost)
neodb.query(queryRelationAccount_account_created_item_SocialProfile)
neodb.query(queryRelationAccount_account_created_item_TagEXTID)
neodb.query(queryRelationAccount_account_created_item_TagEXID)
neodb.query(queryRelationAccount_account_created_item_TagPROFGUID)
neodb.query(queryRelationAccount_account_created_item_Task)
neodb.query(queryRelationAccount_account_created_item_WikiPage)
neodb.query(queryRelationAccount_account_has_social_profile_SocialProfile)
neodb.query(queryRelationAccount_account_is_member_of_space_GroupWorkspace)
neodb.query(queryRelationAccount_account_of_agent_Organisation)
neodb.query(queryRelationAccount_account_of_agent_Person)
neodb.query(queryRelationAccount_account_performed_event_Event25)
neodb.query(queryRelationAccount_account_performed_event_Event2560)
neodb.query(queryRelationAccount_account_performed_event_Event60)