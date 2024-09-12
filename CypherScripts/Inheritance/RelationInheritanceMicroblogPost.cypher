MATCH (mbpc:MicroblogPost_Concept)
MATCH (itc:Item_Concept)
MATCH (iec:IntellectualEntity_Concept)
WITH [mbpc, itc, iec] AS ConMBPIN
UNWIND ConMBPIN as conMBPIN
MATCH (mbp:MicroblogPost)
MERGE (mbp)-[rfil:is_a]->(conMBPIN)