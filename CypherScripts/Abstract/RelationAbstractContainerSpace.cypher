//Space_Concept <-> Container_Concept with Childs
//Container_Concept with Childs
MATCH (co:Container_Concept)
MATCH (w:Weblog_Concept)
MATCH (wi:Wiki_Concept)
MATCH (taco:TaskContainer_Concept)
MATCH (spc:SocialProfileContainer_Concept)
MATCH (mibl:Microblog_Concept)
MATCH (mebo:MessageBoard_Concept)
MATCH (maco:MailContainer_Concept)
MATCH (fili:FileLibrary_Concept)
MATCH (chach:ChatChannel_Concept)
MATCH (meco:MeetingContainer_Concept)
MATCH (cal:Calendar_Concept)

WITH [co, w, wi, taco, spc, mibl, mebo, maco, fili, chach, meco, cal] AS ConCOCO
UNWIND ConCOCO as conCOCO
//Space_Concept with Childs
MATCH (spc:Space_Concept)
MATCH (gws:GroupWorkspace_Concept)
MATCH (op:OrganisationalPlatform_Concept)
MATCH (us:UserWorkspace_Concept)

//Erstellung Relations Space <-> Container und Childs
MERGE (conCOCO)-[rccisspc:container_contained_in_space {cardinality: "exactly 1"}]->(spc)
MERGE (spc)-[rsccspc:space_contains_container]->(conCOCO)
MERGE (conCOCO)-[rccisgws:container_contained_in_space {cardinality: "exactly 1"}]->(gws)
MERGE (gws)-[rsccgws:space_contains_container]->(conCOCO)
MERGE (conCOCO)-[rccisop:container_contained_in_space {cardinality: "exactly 1"}]->(op)
MERGE (op)-[rsccop:space_contains_container]->(conCOCO)
MERGE (conCOCO)-[rccisus:container_contained_in_space {cardinality: "exactly 1"}]->(us)
MERGE (us)-[rsccus:space_contains_container]->(conCOCO)