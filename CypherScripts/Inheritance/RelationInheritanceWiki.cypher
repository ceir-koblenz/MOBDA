MATCH (coc:Container_Concept)
MATCH (wikic:Wiki_Concept)
WITH [coc, wikic] AS ConWIKIIN
UNWIND ConWIKIIN as conWIKIIN
MATCH (wiki:Wiki)
MERGE (wiki)-[rwiki:is_a]->(conWIKIIN)