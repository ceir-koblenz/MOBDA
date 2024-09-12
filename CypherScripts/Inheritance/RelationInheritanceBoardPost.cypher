//Inheritance of BoadPOst
MATCH (bpc:BoardPost_Concept)
MATCH (itc:Item_Concept)
MATCH (iec:IntellectualEntity_Concept)
WITH [bpc, itc, iec] AS ConBPIN
UNWIND ConBPIN as conBPIN
MATCH (bp:BoardPost)
MERGE (bp)-[rbp:is_a]->(conBPIN)