MATCH (sy:System_Concept)
MATCH (dw:DigitalWorkspace_Concept)
//MATCH (co:Container_Concept)
//Concept Space
MATCH (spc:Space_Concept)
MATCH (gws:GroupWorkspace_Concept)
MATCH (op:OrganisationalPlatform_Concept)
MATCH (us:UserWorkspace_Concept)
//Relation System_Concept <-> Space_Concept
MERGE (sy)-[rscs:system_contains_space]->(spc)
MERGE (spc)-[rscis:space_contained_in_system {cardinality: "exactly 1"}]->(sy)
//Relation System_Concept <-> DigitalWorspace_Concept
MERGE (sy)-[rscidw:system_contained_in_digital_workspace]->(dw)
MERGE (dw)-[rdwcs:digital_workspace_contains_system]->(sy)
//Relation Container_Concept <-> Space_Concept
MERGE (co)-[rccis:container_contained_in_space {cardinality: "exactly 1"}]->(spc)
MERGE (spc)-[rscc:space_contains_container]->(co)

//VERERBUNGEN
//System_Concept <-> Space_Concept Childs
//UNWIND
WITH [gws, op, us, spc] AS ConSP 
UNWIND ConSP as conSP
MATCH (sy:System_Concept)
MERGE (sy)-[rscs:system_contains_space]->(conSP)
MERGE (conSP)-[rscis:space_contained_in_system {cardinality: "exactly 1"}]->(sy)