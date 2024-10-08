//MATCH (sd:SocialDocument_Concept)
MATCH (con:Container_Concept)
MATCH (cal:Calendar_Concept)
MATCH (meco:MeetingContainer_Concept)
MATCH (chach:ChatChannel_Concept)
MATCH (fili:FileLibrary_Concept)
MATCH (maco:MailContainer_Concept)
MATCH (mebo:MessageBoard_Concept)
MATCH (miblo:Microblog_Concept)
MATCH (spc:SocialProfileContainer_Concept)
MATCH (taco:TaskContainer_Concept)
MATCH (web:Weblog_Concept)
MATCH (wi:Wiki_Concept)
WITH [con, cal, meco, chach,  fili, maco, mebo, miblo,spc, taco, web, wi] AS Consdcic
UNWIND Consdcic AS consdcic
MATCH (sd:SocialDocument_Concept)
MERGE (sd)-[rsdcic:social_document_contained_in_container]->(consdcic)
MERGE (consdcic)-[rccsd:container_contains_social_document]->(sd)