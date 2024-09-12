MATCH (tasc:Task_Concept)
MATCH (itc:Item_Concept)
MATCH (iec:IntellectualEntity_Concept)
WITH [tasc, itc, iec] AS ConTASKIN
UNWIND ConTASKIN as conTASKIN
MATCH (tas:Task)
MERGE (tas)-[rtask:is_a]->(conTASKIN)