//Inheritance of File 
MATCH (fic:File_Concept)
MATCH (itc:Item_Concept)
MATCH (iec:IntellectualEntity_Concept)
WITH [fic, itc, iec] AS ConFIIN
UNWIND ConFIIN as conFIIN
MATCH (fil:File)
MERGE (fil)-[rfil:is_a]->(conFIIN)