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
WITH [it, cm, scm, itcm, ie, b, wip, ta, sop, mbp, bp, mame, fol, fil, chme, met, caen, foll, like, rea, subs, tag, vote, att, comm] AS ConSDCI
UNWIND ConSDCI AS conSDCI 
MATCH (sd:SocialDocument_Concept)
MERGE (sd)-[rsdci:social_document_contains_item]->(conSDCI)
MERGE (conSDCI)-[ricisd:item_contained_in_social_document]->(sd)
