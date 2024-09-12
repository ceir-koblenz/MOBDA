//Inheritance of SocialProfile
MATCH (sopc:SocialProfile_Concept)
MATCH (itc:Item_Concept)
MATCH (iec:IntellectualEntity_Concept)
WITH [sopc, itc, iec] AS ConSOPIN
UNWIND ConSOPIN as conSOPIN
MATCH (sop:SocialProfile)
MERGE (sop)-[rsop:is_a]->(conSOPIN)