//Abstract Relations with itself
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
WITH [ie, b, wip, ta, sop, mbp, bp, mame, fol, fil, chme, met, caen] AS ConIES
UNWIND ConIES AS conIES

MERGE (conIES)-[riesrv:intellecutal_entity_has_recent_version {cardinality: "exactly 1"}]->(conIES)
MERGE (conIES)-[riesnv:intellecutal_entity_has_next_version {cardinality: "maximal 1"}]->(conIES)
MERGE (conIES)-[riespv:intellecutal_entity_has_previous_version {cardinality: "maximal 1"}]->(conIES)
MERGE (conIES)-[riesov:intellecutal_entity_has_old_version]->(conIES)

