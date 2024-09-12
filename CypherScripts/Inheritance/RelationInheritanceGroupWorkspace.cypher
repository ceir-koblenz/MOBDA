MATCH (spa:Space_Concept)
MATCH (gwsc:GroupWorkspace_Concept)
WITH [gwsc, spa] AS ConGWSIN 
UNWIND ConGWSIN as conGWSIN
MATCH (gws:GroupWorkspace)
MERGE (gws)-[rgws:is_a]->(conGWSIN)