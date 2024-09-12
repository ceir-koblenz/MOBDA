//Inheritance of MessageBoard
MATCH (coc:Container_Concept)
MATCH (mbc:MessageBoard_Concept)
WITH [coc, mbc] AS ConMBCIN
UNWIND ConMBCIN as conMBCIN
MATCH (mb:MessageBoard)
MERGE (mb)-[rmb:is_a]->(conMBCIN)