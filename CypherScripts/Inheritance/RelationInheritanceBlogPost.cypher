//Relations is_a zwischen child Nodes und Parent Nodes_Concepts
MATCH (bc:BlogPost_Concept)
MATCH (iec:IntellectualEntity_Concept)
MATCH (itc:Item_Concept)
WITH [bc, itc, iec] AS ConBGIN 
UNWIND ConBGIN as conBGIN
MATCH (b:BlogPost)
MERGE (b)-[rba:is_a]->(conBGIN)



