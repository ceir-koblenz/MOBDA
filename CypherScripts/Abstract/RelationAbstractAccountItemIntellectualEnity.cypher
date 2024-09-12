//abstract Relation Account <-> Item & IntellectualEntity + Childs

//Concepts Abstract
MATCH (it:Item_Concept)
MATCH (cm:Component_Concept)
MATCH (scm:SimpleComponent_Concept)
MATCH (itcm:IntellectualComponent_Concept)
MATCH (ie:IntellectualEntity_Concept)

//Concepts IntellecutalEntity
MATCH (b:BlogPost_Concept)
MATCH (wip:WikiPage_Concept)
MATCH (ta:Task_Concept)
MATCH (sop:SocialProfile_Concept)
MATCH (mbp:MicroblogPost_Concept)
MATCH (bp:BoardPost_Concept)
MATCH (mame:MailMessage_Concept)
MATCH (fol:Folder_Concept)
MATCH (fil:File_Concept)
MATCH (chme:ChatMessage_Concept)
MATCH (met:Meeting_Concept)
MATCH (caen:CalendarEntry_Concept)

//Concepts SimpleComponent
MATCH  (foll:Follow_Concept)
MATCH  (like:Like_Concept)
MATCH  (rea:Reaction_Concept)
MATCH  (subs:Subscription_Concept)
MATCH  (tag:Tag_Concept)
MATCH  (vote:Vote_Concept)

//Concepts IntellcutalComponent
MATCH  (att:Attachment_Concept)
MATCH  (comm:Comment_Concept)
//Realtions 
WITH [cm, it, scm, itcm, ie, b, wip, ta, sop, mbp, bp, mame, fol, fil, chme, met, caen, foll, like, rea, subs, tag, vote, att, comm] AS ConAI
UNWIND ConAI AS conAI 
MATCH (acc:Account_Concept)
MATCH (ev:Event_Concept)
//Account <-> Item
MERGE (acc)-[raci:account_created_item]->(conAI)
MERGE (conAI)-[ricba:item_created_by_account]->(acc)

//Event <-> Item
MERGE (ev)-[reai:event_affects_item {cardinality: "maximal 1"}]->(conAI)
MERGE (conAI)-[riabe:item_affected_by_event]->(ev)
//Reset zwischen MATCH und MERGE
WITH [] AS GoOn

//Concepts IntellecutalEntity
MATCH (ie:IntellectualEntity_Concept)
MATCH (b:BlogPost_Concept)
MATCH (wip:WikiPage_Concept)
MATCH (ta:Task_Concept)
MATCH (sop:SocialProfile_Concept)
MATCH (mbp:MicroblogPost_Concept)
MATCH (bp:BoardPost_Concept)
MATCH (mame:MailMessage_Concept)
MATCH (fol:Folder_Concept)
MATCH (fil:File_Concept)
MATCH (chme:ChatMessage_Concept)
MATCH (met:Meeting_Concept)
MATCH (caen:CalendarEntry_Concept)

WITH [ie, b, wip, ta, sop, mbp, bp, mame, fol, fil, chme, met, caen] AS ConAIE
UNWIND ConAIE AS conAIE 
MATCH (acc:Account_Concept)
MERGE (acc)-[ractie:account_contributed_to_intellectual_entity]->(conAIE)
MERGE (conAIE)-[riecba:intellectual_entity_contributed_by_account]->(acc)
MERGE (acc)-[ramico:account_mentioned_intectual_entity]->(conAIE)
MERGE (conAIE)-[riemba:intellectual_entity_mentioned_by_account]->(acc)