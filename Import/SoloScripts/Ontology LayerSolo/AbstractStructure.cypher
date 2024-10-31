//Abstract Strucutre
//Abstract Concepts
MERGE (c:Collection_Concept {name: "Collection_Concept"})
MERGE (sd:SocialDocument_Concept {name: "SocialDocument_Concept"})
MERGE (it:Item_Concept {name: "Item_Concept"})
MERGE (ie:IntellectualEntity_Concept {name: "IntellectualEntity_Concept"})
MERGE (cm:Component_Concept {name: "Component_Concept"})
MERGE (sc:SimpleComponent_Concept {name: "SimpleComponent_Concept"})
MERGE (ic:IntellectualComponent_Concept {name: "IntellectualComponent_Concept"})
MERGE (co:Container_Concept {name: "Container_Concept"})
MERGE (sp:Space_Concept {name: "Space_Concept"})
MERGE (sy:System_Concept {name: "System_Concept"})
MERGE (dw:DigitalWorkspace_Concept {name: "DigitalWorkspace_Concept"})

//Concepts IntellectualEntity
MERGE (b:BlogPost_Concept {name: "BlogPost_Concept"})
MERGE (wip:WikiPage_Concept {name: "WikiPage_Concept"})
MERGE (ta:Task_Concept {name: "Task_Concept"})
MERGE (sop:SocialProfile_Concept {name: "SocialProfile_Concept"})
MERGE (mbp:MicroblogPost_Concept {name: "MicroblogPost_Concept"})
MERGE (bp:BoardPost_Concept {name: "BoardPost_Concept"})
MERGE (mame:MailMessage_Concept {name: "MailMessage_Concept"}) 
MERGE (fol:Folder_Concept {name: "Folder_Concept "})
MERGE (fil:File_Concept {name: "File_Concept"})
MERGE (chme:ChatMessage_Concept {name: "ChatMessage_Concept"})
MERGE (met:Meeting_Concept {name: "Meeting_Concept"})
MERGE (caen:CalendarEntry_Concept {name: "CalendarEntry_Concept"})

//Subclass Relations
//Major Entities
MERGE (ic)-[riccm:sub_class_of]->(cm)
MERGE (sc)-[rsccm:sub_class_of]->(cm)
MERGE (cm)-[rcmit:sub_class_of]->(it)
MERGE (ie)-[rieit:sub_class_of]->(it)

// Subclass IE Concept to IE
WITH [b, wip, ta, sop, mbp, bp, mame, fol, fil, chme, met, caen] AS ConIEIT //Concept InterlectualEntity to InterlectualEntity
UNWIND ConIEIT as conIEIT
MATCH (ie:IntellectualEntity_Concept)
MATCH (it:Item_Concept) //?
MERGE (conIEIT)-[rcie:sub_class_of]->(ie)

//Subclass IE Concept to IT (UNWIND from Subclass IE)
MERGE (conIEIT)-[rcit:sub_class_of]->(it)

//Concepts Container
MERGE (w:Weblog_Concept {name: "Weblog_Concept"})
MERGE (wi:Wiki_Concept {name: "Wiki_Concept"})
MERGE (taco:TaskContainer_Concept {name: "TaskContainer_Concept"})
MERGE (spc:SocialProfileContainer_Concept {name: "SocialProfileContainer_Concept"})
MERGE (mibl:Microblog_Concept {name: "Microblog_Concept"})
MERGE (mebo:MessageBoard_Concept {name: "MessageBoard_Concept"})
MERGE (maco:MailContainer_Concept {name: "MailContainer_Concept"})
MERGE (fili:FileLibrary_Concept {name: "FileLibrary_Concept"})
MERGE (chach:ChatChannel_Concept {name: "ChatChannel_Concept"})
MERGE (meco:MeetingContainer_Concept {name: "MeetingContainer_Concept"})
MERGE (cal:Calendar_Concept {name: "Calendar_Concept"})

//Subclass CO Concept to Container
WITH [w, wi, taco, spc, mibl, mebo, maco, fili, chach, meco, cal] AS ConCOCO
UNWIND ConCOCO as conCOCO
MATCH (co:Container_Concept)
MERGE (conCOCO)-[rcco:sub_class_of]->(co)

//Concepts SimpleComponent
MERGE (foll:Follow_Concept {name: "Follow_Concept"})
MERGE (like:Like_Concept {name: "Like_Concept"})
MERGE (rea:Reaction_Concept {name: "Reaction_Concept"})
MERGE (subs:Subscription_Concept {name: "Subscription_Concept"})
MERGE (tag:Tag_Concept {name: "Tag_Concept"})
MERGE (vote:Vote_Concept {name: "Vote_Concept"})

//Subclass SC Concept to SimpleComponents 
WITH[foll, like, rea, subs, tag, vote] AS ConSC
UNWIND ConSC as conSC
MATCH (sc:SimpleComponent_Concept)
MATCH (cm:Component_Concept) //?
MATCH (it:Item_Concept) //?
MERGE (conSC)-[rcsc:sub_class_of]->(sc)

//Subclass SimpleComponent Concept to Component
MERGE (conSC)-[rcsccm:sub_class_of]->(cm)

//Subclass SimpleComponent Concept to Item
MERGE (conSC)-[rcscit:sub_class_of]->(it)

//Concepts IntellectualComponent
MERGE (att:Attachment_Concept {name: "Attachment_Concept"})
MERGE (comm:Comment_Concept {name: "Comment_Concept"})

//Subclass IntellectualComponent Concept to IntellecutalComponent
WITH [att, comm] AS ConIC 
UNWIND ConIC as conIC
MATCH (ic:IntellectualComponent_Concept)
MATCH (cm:Component_Concept) //?
MATCH (it:Item_Concept) //?
MERGE (conIC)-[rcicic:sub_class_of]->(ic)

//Subclass IntellctualComponent Concept to Component
MERGE (conIC)-[rcicc:sub_class_of]->(cm)

//Subclass IntellctualComponent Concept to item
MERGE (conIC)-[rcicit:sub_class_of]->(it)

//Concept Space
MERGE (gws:GroupWorkspace_Concept {name: "GroupWorkspace_Concept"})
MERGE (op:OrganisationalPlatform_Concept {name: "OrganisationalPlatform_Concept"})
MERGE (us:UserWorkspace_Concept {name: "UserWorkspace_Concept"})

//Sublass Space Concept to Space
WITH [gws, op, us] AS ConSP 
UNWIND ConSP as conSP
MATCH (sp:Space_Concept)
MERGE (conSP)-[rcspsp:sub_class_of]->(sp)

//Concepts Event (rot)
MERGE (ev:Event_Concept {name: "Event_Concept"})

//Concepts Account (gelb)
MERGE (acc:Account_Concept {name: "Account_Concept"})
MERGE (role:Role_Concept {name: "Role_Concept"})
MERGE (gro:Group_Concept {name: "Group_Concept"})
MERGE (ogro:OrganisationalGroup_Concept {name: "OrganisationalGroup_Concept"})
MERGE (ag:Agent_Concept {name: "Agent_Concept"})
MERGE (arag:ArtifcialAgent_Concept {name: "ArtifcialAgent_Concept"})
MERGE (org:Organisation_Concept {name: "Organisation_Concept"})
MERGE (per:Person_Concept {name: "Person_Concept"})

//Sublass  Agent 
WITH [arag, org, per] AS ConAG
UNWIND ConAG AS conAG 
MATCH (ag:Agent_Concept)
MERGE (conAG)-[rcag:sub_class_of]->(ag)