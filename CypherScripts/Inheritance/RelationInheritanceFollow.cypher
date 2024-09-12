//Inheritance of Follow 
MATCH (folc:Follow_Concept)
MATCH (itc:Item_Concept)
MATCH (coc:Component_Concept)
MATCH (scc:SimpleComponent_Concept)
WITH [folc, itc, coc, scc] AS ConFOLIN 
UNWIND ConFOLIN as conFOLIN
MATCH (fol:Follow)
MERGE (fol)-[rfol:is_a]->(conFOLIN)