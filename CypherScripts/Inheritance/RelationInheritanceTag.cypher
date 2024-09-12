MATCH (tagc:Tag_Concept)
MATCH (itc:Item_Concept)
MATCH (scc:SimpleComponent_Concept)
MATCH (comc:Component_Concept)
WITH [tagc, itc, scc, comc] AS ConTAGIN
UNWIND ConTAGIN as conTAGIN
MATCH (tag:Tag)
MERGE (tag)-[rtag:is_a]->(conTAGIN)