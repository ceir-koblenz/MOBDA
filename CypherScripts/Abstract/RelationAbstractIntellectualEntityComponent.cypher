//Relation Component <-> IntellecutalEntity

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
//Collect Concepts IntellctualEntity
WITH [ie, b, wip, ta, sop, mbp, bp, mame, fol, fil, chme, met, caen] AS ConIEC
UNWIND ConIEC AS conIEC
//Concepts Components
MATCH (foll:Follow_Concept)
MATCH (scm:SimpleComponent_Concept)
MATCH (like:Like_Concept)
MATCH (rea:Reaction_Concept)
MATCH (subs:Subscription_Concept)
MATCH (tag:Tag_Concept)
MATCH (vote:Vote_Concept)
MATCH (itcm:IntellectualComponent_Concept)
MATCH (att:Attachment_Concept)
MATCH (comm:Comment_Concept)

//Relation Concepts SimpleComponent
MERGE (scm)-[rcoiescm:component_of_intellectual_entity]->(conIEC)
MERGE (conIEC)-[riehcscm:intellectual_entity_has_component]->(scm)
MERGE (foll)-[rcoiefoll:component_of_intellectual_entity]->(conIEC)
MERGE (conIEC)-[riehcfoll:intellectual_entity_has_component]->(foll)
MERGE (like)-[rcoielike:component_of_intellectual_entity]->(conIEC)
MERGE (conIEC)-[riehclike:intellectual_entity_has_component]->(like)
MERGE (rea)-[rcoierea:component_of_intellectual_entity]->(conIEC)
MERGE (conIEC)-[riehcrea:intellectual_entity_has_component]->(rea)
MERGE (subs)-[rcoiesubs:component_of_intellectual_entity]->(conIEC)
MERGE (conIEC)-[riehcsubs:intellectual_entity_has_component]->(subs)
MERGE (tag)-[rcoietag:component_of_intellectual_entity]->(conIEC)
MERGE (conIEC)-[riehctag:intellectual_entity_has_component]->(tag)
MERGE (vote)-[rcoievote:component_of_intellectual_entity]->(conIEC)
MERGE (conIEC)-[riehcvote:intellectual_entity_has_component]->(vote)

//Relation Concepts IntellecutalComponent
MERGE (itcm)-[rcoieitcm:component_of_intellectual_entity]->(conIEC)
MERGE (conIEC)-[riehcitcm:intellectual_entity_has_component]->(itcm)
MERGE (att)-[rcoieatt:component_of_intellectual_entity]->(conIEC)
MERGE (conIEC)-[riehcatt:intellectual_entity_has_component]->(att)
MERGE (comm)-[rcoiecomm:component_of_intellectual_entity]->(conIEC)
MERGE (conIEC)-[riehccomm:intellectual_entity_has_component]->(comm)