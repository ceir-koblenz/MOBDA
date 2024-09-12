//Inheritance of Comment
MATCH (comc:Comment_Concept)
MATCH (itc:Item_Concept)
MATCH (coc:Component_Concept)
MATCH (icc:IntellectualComponent_Concept)
WITH [comc, itc, coc, icc] AS ConCOIN 
UNWIND ConCOIN as conCOIN
MATCH (com:Comment)
MERGE (com)-[rcom:is_a]->(conCOIN)