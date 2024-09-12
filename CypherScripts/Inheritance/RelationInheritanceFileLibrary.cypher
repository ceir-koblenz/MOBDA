MATCH (coc:Container_Concept)
MATCH (filic:FileLibrary_Concept)
WITH [coc, filic] AS ConFILIC
UNWIND ConFILIC as conFILIC
MATCH (fili:FileLibrary)
MERGE (fili)-[rfili:is_a]->(conFILIC)