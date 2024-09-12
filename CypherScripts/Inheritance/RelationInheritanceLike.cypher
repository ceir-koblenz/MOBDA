//Inheritance of Like
MATCH (likec:Like_Concept)
MATCH (itc:Item_Concept)
MATCH (coc:Component_Concept)
MATCH (scc:SimpleComponent_Concept)
WITH [likec, itc, coc, scc] AS ConLIKIN 
UNWIND ConLIKIN as conLIKIN
MATCH (like:Like)
MERGE (like)-[rlike:is_a]->(conLIKIN)