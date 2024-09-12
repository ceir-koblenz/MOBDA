//Inheritance of Folder
MATCH (foc:Folder_Concept)
MATCH (itc:Item_Concept)
MATCH (iec:IntellectualEntity_Concept)
WITH [foc, itc, iec] AS ConFOCIN
UNWIND ConFOCIN as conFOCIN
MATCH (fo:Folder)
MERGE (fo)-[rfoc:is_a]->(conFOCIN)